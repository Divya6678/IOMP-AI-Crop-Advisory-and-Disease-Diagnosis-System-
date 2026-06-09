import numpy as np
import cv2
import json
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.mobilenet import preprocess_input
from recommendations import RECOMMENDATIONS
from PIL import Image

# ---------------------------------------
# LEAF VALIDATION FUNCTION
# ---------------------------------------
def is_leaf_image(image_path):
    try:
        img = cv2.imread(image_path)
        if img is None:
            return False
            
        img = cv2.resize(img, (128, 128))
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        
        # Define ranges for plant colors (green, yellow, brown) in HSV
        lower_color = np.array([5, 20, 20])
        upper_color = np.array([105, 255, 255])
        
        mask = cv2.inRange(hsv, lower_color, upper_color)
        
        # Calculate percentage of pixels within the plant color range
        ratio = cv2.countNonZero(mask) / (128.0 * 128.0)
        
        if ratio < 0.03:  # at least 3% of the image should be plant-colored

            return False
            
        return True
    except Exception as e:
        return False


# ---------------------------------------
# LOAD MODEL + CLASSES (only once)
# ---------------------------------------
model = load_model("mobilenet_model.h5", compile=False)

# WARMUP to prevent Flask thread deadlock on Windows
dummy_img = np.zeros((1, 224, 224, 3), dtype=np.float32)
model.predict(dummy_img)

with open("class_indices.json", "r") as f:
    class_indices = json.load(f)

class_names = list(class_indices.keys())


# ---------------------------------------
# IMAGE PREPROCESSING
# ---------------------------------------
def preprocess(image_path):
    img = cv2.imread(image_path)

    if img is None:
        return None

    img = cv2.resize(img, (224, 224))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = preprocess_input(img)
    img = np.expand_dims(img, axis=0)

    return img


# ---------------------------------------
# SEVERITY LOGIC
# ---------------------------------------
def get_severity(confidence):
    if confidence >= 85:
        return "High"
    elif confidence >= 70:
        return "Medium"
    else:
        return "Low"


# ---------------------------------------
# MAIN PREDICTION FUNCTION
# ---------------------------------------
def predict_disease(image_path, selected_crop="Unknown"):

    # 1️⃣ Check if leaf image
    if not is_leaf_image(image_path):
        return {
            "Crop": "Unknown",
            "Disease": "Invalid Image",
            "Confidence": 0,
            "Severity": "None",
            "Organic": "N/A",
            "Chemical": "N/A",
            "Advice": "Please upload a clear crop leaf image."
        }

    # 2️⃣ Preprocess image
    img = preprocess(image_path)

    if img is None:
        return {
            "Crop": "Unknown",
            "Disease": "Image Read Error",
            "Confidence": 0,
            "Severity": "None",
            "Organic": "N/A",
            "Chemical": "N/A",
            "Advice": "Could not process the image."
        }

    # 3️⃣ Model Prediction
    prediction = model.predict(img)[0]

    # Find valid indices for the selected crop
    valid_indices = []
    for idx, name in enumerate(class_names):
        if name.startswith(selected_crop + "___") or name == selected_crop:
            valid_indices.append(idx)
            
    if not valid_indices:
        return {
            "Crop": selected_crop,
            "Disease": "Model Not Retrained",
            "Confidence": 0,
            "Severity": "None",
            "Organic": "N/A",
            "Chemical": "N/A",
            "Advice": f"Please retrain your AI model to include '{selected_crop}' diseases. The current model lacks this class."
        }

    best_idx = valid_indices[0]
    best_conf = prediction[best_idx]
    
    for i in range(1, len(valid_indices)):
        idx = valid_indices[i]
        if prediction[idx] > best_conf:
            best_conf = prediction[idx]
            best_idx = idx

    confidence = float(best_conf * 100)
    class_name = class_names[best_idx]

    # 4️⃣ Confidence Check
    if confidence < 40:
        return {
            "Crop": "Unknown",
            "Disease": "Unclear Image / Low Confidence",
            "Confidence": round(confidence, 2),
            "Severity": "None",
            "Organic": "N/A",
            "Chemical": "N/A",
            "Advice": "The AI could not confidently detect the disease. Please upload a clearer crop leaf image."
        }

    # 5️⃣ Extract crop & disease
    if "___" in class_name:
        crop, disease = class_name.split("___")
    else:
        crop = "Unknown"
        disease = class_name

    severity = get_severity(confidence)

    # 6️⃣ Get recommendations safely
    recommendation = {
        "organic": "Consult agricultural expert.",
        "chemical": "Use crop-specific fungicide.",
        "advice": "Maintain plant hygiene and monitor regularly."
    }

    disease_data = RECOMMENDATIONS.get(disease)

    if disease_data and severity in disease_data:
        recommendation = disease_data[severity]

    # 7️⃣ Final Response
    return {
        "Crop": crop,
        "Disease": disease,
        "Confidence": round(confidence, 2),
        "Severity": severity,
        "Organic": recommendation["organic"],
        "Chemical": recommendation["chemical"],
        "Advice": recommendation["advice"]
    }