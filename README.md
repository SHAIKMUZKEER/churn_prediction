# 🚀 Customer Churn Prediction System

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20App-black?logo=flask)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange?logo=scikitlearn)
![Random Forest](https://img.shields.io/badge/Model-Random%20Forest-success)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple?logo=bootstrap)
![License](https://img.shields.io/badge/License-MIT-green)

</p>

---

# 📌 Project Overview

Customer churn is one of the biggest challenges faced by telecom companies. Losing existing customers directly affects revenue and business growth.

This project uses **Machine Learning** to predict whether a telecom customer is likely to **leave (Churn)** or **stay**, based on customer subscription details, service usage, and billing information.

The project includes an end-to-end ML pipeline, from data preprocessing and model training to deployment through a Flask web application.

---

# 🎯 Objective

The goal of this project is to:

- Predict customer churn using historical telecom data.
- Help companies identify customers who are likely to leave.
- Support customer retention strategies.
- Demonstrate an end-to-end Machine Learning workflow suitable for production environments.

---

# ✨ Features

- End-to-End Machine Learning Pipeline
- Data Ingestion Module
- Data Transformation Pipeline
- Feature Engineering
- Random Forest Classification Model
- Model Serialization using Pickle
- Flask Web Application
- Professional Responsive UI
- Logging and Exception Handling
- Production Ready Project Structure

---

# 📊 Dataset

The project uses a Telecom Customer Churn dataset containing customer demographic and service information.

### Selected Features

| Feature | Description |
|----------|-------------|
| tenure | Customer subscription duration |
| MonthlyCharges | Monthly bill amount |
| TotalCharges | Total amount charged |
| Contract | Contract type |
| InternetService | Internet service type |
| TechSupport | Technical support availability |
| PaymentMethod | Payment method |
| Dependents | Whether customer has dependents |

### Target Variable

```
Churn
```

- Yes → Customer will leave
- No → Customer will stay

---

# 🧠 Machine Learning Pipeline

```
Dataset
      │
      ▼
Data Ingestion
      │
      ▼
Data Cleaning
      │
      ▼
Feature Engineering
      │
      ▼
Preprocessing Pipeline
      │
      ▼
Random Forest Classifier
      │
      ▼
Model Evaluation
      │
      ▼
Model Saving
      │
      ▼
Flask Web Application
      │
      ▼
Prediction
```

---

# 🏗 Project Structure

```
churn_prediction/
│
├── artifacts/
│   ├── model.pkl
│   ├── preprocessor.pkl
│   ├── train.csv
│   ├── test.csv
│   └── raw.csv
│
├── logs/
│
├── notebook/
│   ├── data/
│   ├── EDA_transformation.ipynb
│   └── model_trainer.ipynb
│
├── src/
│   │
│   ├── components/
│   │     ├── data_ingestion.py
│   │     ├── data_transformation.py
│   │     └── model_trainer.py
│   │
│   ├── pipeline/
│   │     ├── train_pipeline.py
│   │     └── predict_pipeline.py
│   │
│   ├── exception.py
│   ├── logger.py
│   └── utils.py
│
├── static/
│   ├── css/
│   └── images/
│
├── templates/
│   ├── index.html
│   └── home.html
│
├── app.py
├── setup.py
├── requirements.txt
├── Procfile
├── runtime.txt
├── README.md
└── .gitignore
```

---

# 🛠 Technologies Used

### Programming Language

- Python

### Machine Learning

- Scikit-Learn
- Random Forest Classifier

### Data Processing

- Pandas
- NumPy

### Data Visualization

- Matplotlib
- Seaborn

### Backend

- Flask

### Frontend

- HTML5
- CSS3
- Bootstrap 5
- JavaScript
- Jinja2 Templates

### Development Tools

- VS Code
- Git
- GitHub

---

# 🤖 Machine Learning Model

### Algorithm Used

```
Random Forest Classifier
```

### Why Random Forest?

- Handles both numerical and categorical data effectively.
- Reduces overfitting through ensemble learning.
- Provides high accuracy and robustness.
- Performs well on structured telecom datasets.

---

# ⚙ Feature Engineering

The following preprocessing steps were performed:

- Missing Value Handling
- Feature Selection
- One-Hot Encoding
- Standard Scaling
- Data Transformation Pipeline
- Train-Test Split

---

# 🌐 Web Application

The Flask web application allows users to:

- Enter customer information.
- Predict whether the customer is likely to churn.
- Display prediction results in real time.

---

# 📷 Application Workflow

```
User

↓

Enter Customer Details

↓

Flask Backend

↓

Load Preprocessor

↓

Transform Features

↓

Load Random Forest Model

↓

Predict

↓

Display Result
```

---

# 🚀 Installation Guide

## 1 Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/churn_prediction.git
```

---

## 2 Move into Project

```bash
cd churn_prediction
```

---

## 3 Create Virtual Environment

Windows

```bash
python -m venv venv
```

Linux / Mac

```bash
python3 -m venv venv
```

---

## 4 Activate Environment

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

---

## 5 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 6 Run the Flask Application

```bash
python app.py
```

---

## 7 Open Browser

```
http://127.0.0.1:5000/
```

---

# 💻 Example Prediction

Input

```
Tenure : 24

Monthly Charges : 75.5

Total Charges : 1812

Contract : Month-to-month

Internet Service : Fiber Optic

Tech Support : No

Payment Method : Electronic Check

Dependents : No
```

Output

```
Customer is Likely to Churn
```

---

# 📈 Future Improvements

- Deploy on Microsoft Azure
- Docker Containerization
- CI/CD using GitHub Actions
- Model Monitoring
- Explainable AI (SHAP)
- REST API Documentation
- User Authentication
- Database Integration

---

# 📚 Learning Outcomes

This project demonstrates practical knowledge of:

- Machine Learning
- Feature Engineering
- Data Preprocessing
- Random Forest Classification
- Flask Development
- Modular Python Programming
- Object-Oriented Programming
- Logging
- Exception Handling
- Git & GitHub
- Deployment Concepts

---

# 👨‍💻 Author

**Shaik Muzkeer**

Computer Science Engineering Student

Machine Learning & AI Enthusiast

GitHub:
https://github.com/SHAIKMUZKEER

LinkedIn:
(Add Your LinkedIn URL)

---

# ⭐ If you found this project useful

Please consider giving it a ⭐ on GitHub.

It motivates me to build more AI and Machine Learning projects.

---

## 📄 License

This project is licensed under the MIT License.

