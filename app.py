from flask import Flask, render_template, request, send_from_directory
import sqlite3
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('index.html')

# Upload Resume Route
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'resume' not in request.files:
        return "No file uploaded", 400

    file = request.files['resume']
    if file.filename == '':
        return "No selected file", 400

    if not (file.filename.endswith('.pdf') or file.filename.endswith('.docx')):
        return "File not uploaded, upload PDF or DOCX file", 400

    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    return "File uploaded successfully!"

# Route to Fetch and Display Resumes
@app.route('/dashboard')
def dashboard():
    conn = sqlite3.connect('resumes.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM resumes")  
    resumes = cursor.fetchall()  
    conn.close()

    return render_template('dashboard.html', resumes=resumes)

# Serve Uploaded Resume Files
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
