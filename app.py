from flask import Flask, render_template, request, jsonify, session, redirect, url_for, flash
import os
from functools import wraps
from predict import predict_disease
from database import init_db, insert_history, get_history, register_user, verify_user

app = Flask(__name__)
app.secret_key = "agrovision_secret_key_123" # Change this for production

# ==============================
# CONFIGURATION
# ==============================

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Initialize Database
init_db()

# ==============================
# AUTH DECORATOR
# ==============================

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# ==============================
# PAGE ROUTES
# ==============================

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template("dashboard.html")

@app.route('/history')
@login_required
def history():
    return render_template("history.html")

@app.route('/contact')
@login_required
def contact():
    return render_template("contact.html")

# ==============================
# AUTH ROUTES
# ==============================

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = verify_user(email, password)
        if user:
            session['user_id'] = user['id']
            session['user_name'] = user['name']
            return redirect(url_for('dashboard'))
        else:
            flash("Invalid email or password", "error")
            
    return render_template("login.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        
        if register_user(name, email, password):
            flash("Account created! Please log in.", "success")
            return redirect(url_for('login'))
        else:
            flash("Email already registered", "error")
            
    return render_template("signup.html")

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

# ==============================
# AI PREDICTION ROUTE
# ==============================

@app.route('/predict', methods=['POST'])
@login_required
def predict():

    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    crop_selected = request.form.get("crop", "Unknown")

    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    # ✅ Allow only specific formats
    allowed_extensions = ['.jpg', '.jpeg', '.png']
    file_ext = os.path.splitext(file.filename)[1].lower()

    if file_ext not in allowed_extensions:
        return jsonify({
            "error": "Only JPG, JPEG and PNG images are allowed."
        }), 400

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    result = predict_disease(filepath, crop_selected)

    if result["Crop"] == "Unknown":
        return jsonify({
            "disease": result["Disease"],
            "confidence": result["Confidence"],
            "severity": "None",
            "organic": "N/A",
            "chemical": "N/A",
            "prevention": result.get("Advice", "No prevention advice available.")
        })

    insert_history(
        session['user_id'],
        result["Crop"],
        result["Disease"],
        result["Confidence"],
        result["Severity"],
        file.filename
    )

    return jsonify({
        "disease": result["Disease"],
        "confidence": result["Confidence"],
        "severity": result["Severity"],
        "organic": result["Organic"],
        "chemical": result["Chemical"],
        "prevention": result["Advice"]
    })

# ==============================
# HISTORY DATA API
# ==============================

@app.route('/history-data')
@login_required
def history_data():
    records = get_history(session['user_id'])

    data = []
    for row in records:
        data.append({
            "date": row[0],
            "disease": row[1],
            "severity": row[2],
            "confidence": row[3],
            "image": row[4] if len(row) > 4 else "default.png"
        })

    return jsonify(data)

# ==============================
# RUN APP
# ==============================

if __name__ == "__main__":
    app.run(debug=True, port=5001)