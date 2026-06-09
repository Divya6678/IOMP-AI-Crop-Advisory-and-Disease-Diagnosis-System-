# AgroMind - AI Crop Disease Diagnosis System

AgroMind is a full-stack web application designed to help farmers and gardeners identify crop diseases from images. Using a pre-trained **MobileNetV2** deep learning model, it detects leaf diseases and provides actionable recommendations for treatment.

---

## 🚀 Key Features

-   **AI Disease Diagnosis**: Upload crop leaf images for real-time analysis.
-   **Treatment Recommendations**: Get organic, chemical, and preventive measures for diagnosed issues.
-   **User Dashboard**: Clean, intuitive interface with glassmorphism design.
-   **Persistent History**: Secure login/signup to track all your past diagnoses.
-   **Leaf Validation**: Smart filtering to ensure uploaded images are plant leaves.

---

## 🛠️ Technology Stack

-   **Backend**: Python, Flask
-   **Frontend**: HTML5, CSS3 (Glassmorphism), JavaScript
-   **Database**: SQLite
-   **Machine Learning**: TensorFlow/Keras, MobileNetV2
-   **Processing**: OpenCV, NumPy

---

## 📂 Project Structure

```text
├── app.py              # Main Flask application
├── database.py         # SQLite database management
├── predict.py          # AI inference logic and preprocessing
├── recommendations.py  # Dictionary of disease treatments
├── static/             # CSS, images, and user uploads
├── templates/          # HTML pages (Dashboard, History, etc.)
├── history.db          # Persistent database (Generated)
└── requirements.txt    # Project dependencies
```

---

## ⚡ Setup & Run

### 1. Prerequisites
Ensure you have **Python 3.10+** installed on your system.

### 2. Install Dependencies
Open your terminal in the project directory and run:
```powershell
pip install -r requirements.txt
```

### 3. Run the Application
Start the Flask server:
```powershell
python app.py
```
By default, the app will run at: `http://127.0.0.1:5001` or `http://localhost:5001`.

---

## 🔒 Security
-   **Password Salting**: Passwords are hashed before storage in the database.
-   **Authentication**: Protected routes ensure only logged-in users can access the diagnosis features.

---

## 🛡️ Disclaimer
*AgroMind provides recommendations based on AI predictions. Always consult with a certified agricultural expert before applying intensive chemical treatments.*
