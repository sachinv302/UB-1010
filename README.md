# 🏙 Smart City Seva Portal
## AI-Powered Civic Complaint Prioritization System

---

## 📌 1. Project Overview

Smart City Seva Portal is an intelligent civic complaint management system designed to automatically classify and prioritize public issues using Machine Learning.

Unlike traditional portals that process complaints in the order they are received, this system evaluates:

- 🚨 Urgency (ML-based text classification)
- 🏷 Category severity
- 📍 Location sensitivity
- 📊 Weighted priority score

The system ensures that critical public safety issues are addressed first, improving city governance efficiency.

---

## 🎯 2. Problem Statement

Traditional complaint systems:

- Work on First-Come-First-Serve basis
- Do not evaluate severity
- Do not consider public impact
- Lack intelligent prioritization

This leads to delays in resolving critical issues like:
- Electric wire accidents
- Fire hazards
- Hospital area problems
- Public safety emergencies

---

## 💡 3. Proposed Solution

Our system introduces:

✔ AI-based urgency detection  
✔ Smart location keyword analysis  
✔ Weighted priority scoring engine  
✔ Automated complaint sorting  
✔ Admin dashboard for quick decisions  

This enables smart cities to take action based on urgency and impact rather than submission time.

---

## 🧠 4. Machine Learning Model

### Algorithm Used:
- Logistic Regression (Supervised Learning)

### Feature Extraction:
- TF-IDF (Term Frequency–Inverse Document Frequency)

### Classification Type:
- Multi-class Text Classification

### Output Classes:
- Critical
- High
- Medium
- Low

### Priority Formula:

Priority Score =
(Urgency × 0.6)
+ (Category Weight × 0.3)
+ (Location Weight × 0.1)

This ensures urgency has the highest influence.

---

## 🏗 5. System Architecture

User → Flask Backend → ML Model → Priority Engine → SQLite Database → Admin Dashboard

Flow:
1. User submits complaint
2. ML model predicts urgency
3. Location keywords detected
4. Weighted priority calculated
5. Complaint stored in database
6. Admin dashboard auto-sorts by priority

---

## 🔄 6. System Workflow

### 👤 User Side

1. Register / Login
2. Submit complaint
3. Enter category and manual location
4. ML predicts urgency
5. System calculates priority
6. View complaint status

### 🛡 Admin Side

1. Secure admin login
2. View all complaints
3. Automatically sorted by priority score
4. Update complaint status
5. Monitor resolution progress

---

## 🚀 7. Features

### User Module
- User Registration & Login
- Submit Complaint
- Manual Location Entry
- AI-based Urgency Detection
- View Complaint Status

### Admin Module
- Secure Admin Login
- Priority-Based Sorting
- Status Update System
- Dashboard Analytics

### AI Intelligence
- Text-based urgency prediction
- Keyword-based location importance detection
- Weighted scoring engine

---

## 🛠 8. Tech Stack

Backend:
- Python
- Flask
- SQLite

Machine Learning:
- Scikit-learn
- Pandas
- TF-IDF
- Logistic Regression

Frontend:
- HTML
- CSS (Glassmorphism UI)
- FontAwesome Icons

---

## 📂 9. Project Structure

smart_city_seva/
│
├── app.py
├── train_model.py
├── requirements.txt
├── README.md
│
├── models/
│     └── urgency_model.pkl
│
├── utils/
│     ├── db_setup.py
│     └── priority_engine.py
│
├── templates/
├── static/

---

## ⚙ 10. Installation & Setup Guide

### Step 1: Clone Repository

git clone https://github.com/<YourUsername>/<YourTeamID>.git

### Step 2: Navigate to Folder

cd <YourTeamID>

### Step 3: Create Virtual Environment

python -m venv venv  
venv\Scripts\activate

### Step 4: Install Dependencies

pip install -r requirements.txt

### Step 5: Train ML Model

python train_model.py

### Step 6: Run Application

python app.py

Open browser:
http://127.0.0.1:5000

---

## 🔐 11. Admin Credentials

Email: admin@smartcity.com  
Password: admin123  

---

## 🎬 12. Demo Flow (For Hackathon Presentation)

1. Register a new user
2. Submit a dangerous complaint (e.g., "Live electric wire near hospital")
3. Show urgency prediction (Critical)
4. Show calculated priority score
5. Login as admin
6. Show automatic sorting
7. Update complaint status

Explain:

"Our system uses supervised machine learning to classify complaint urgency and dynamically prioritizes civic issues based on severity and geo-context intelligence."

---

## 🏆 13. Innovation Highlights

- AI-powered complaint prioritization
- Dynamic location keyword detection
- Weighted scoring mechanism
- Automated admin sorting
- Clean modern UI
- Lightweight and scalable

---

## 📈 14. Future Enhancements

- Complaint Heatmap Visualization
- Real-time Analytics Charts
- Duplicate Complaint Detection
- Cloud Deployment
- Mobile Application
- GPS-based auto location detection

---

## 👨‍💻 15. Developed For

Hackathon Submission  
Team ID: <YourTeamID>  

---
