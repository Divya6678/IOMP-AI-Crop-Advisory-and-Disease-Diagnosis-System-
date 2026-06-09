import numpy as np
import cv2
from tensorflow.keras.models import load_model

model = load_model("C:/Users/Divya/Desktop/IOMP/mobilenet_model.h5")

class_names = ["Potato___Early_blight",
               "Potato___Late_blight",
               "Potato___healthy"]

img = cv2.imread("C://Users//Divya//Desktop//IOMP//dataset_processed//test//Potato___Early_blight//1d4fc5d0-fee6-40bf-8e7b-e1598ea64161___RS_Early.B 8912.JPG")
img = cv2.resize(img, (224, 224))
img = img / 255.0
img = np.reshape(img, (1, 224, 224, 3))

prediction = model.predict(img)

class_index = np.argmax(prediction)
confidence = float(np.max(prediction) * 100)
class_name = class_names[class_index]

if "healthy" in class_name:
    disease_name = "No Disease"
else:
    disease_name = class_name.split("___")[1].replace("_", " ")

if disease_name == "No Disease":
    severity = "None"
else:
    if confidence > 85:
        severity = "High"
    elif confidence > 60:
        severity = "Moderate"
    else:
        severity = "Low"

print("Class Name:", class_name)
print("Disease Name:", disease_name)
print("Confidence: {:.2f}%".format(confidence))
print("Severity:", severity)