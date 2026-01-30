# 🏦 CreditWise Loan Approval System

CreditWise Loan Approval System is a machine learning–based web application that predicts whether a loan application is likely to be approved or rejected.  
The system uses applicant profile, employment details, financial health, and loan request information to make risk-aware predictions.

This project is designed for academic, learning, and demonstration purposes using real-world loan approval concepts.

---

## 🔍 Machine Learning Approach

This project is designed as a **binary classification problem**, where the goal is to predict whether a loan application should be **Approved (1)** or **Rejected (0)** based on applicant and financial attributes.

Multiple classification algorithms were trained and evaluated:

- Logistic Regression
- K-Nearest Neighbors (KNN)
- Naive Bayes
- Decision Tree Classifier
- Random Forest Classifier

After comparing performance on test data using **Accuracy, Precision, Recall, and F1-score**,  
the **Random Forest Classifier** was selected as the final model due to its balanced and stable results, especially in handling real-world financial decision factors.

The trained classifier is saved and used directly in the Streamlit application for real-time predictions.

---

## 🧠 Machine Learning Model

- Algorithm Used: **Random Forest Classifier**
- Reason:
  - Handles mixed numerical & categorical data well
  - Reduces overfitting compared to single decision trees
  - Provides strong accuracy and stable predictions

The trained model is saved as:
models/random_forest.pkl

---


## 🎯 Project Objective

The main goal of this project is to:
- Predict loan approval status using historical loan data
- Help users understand their financial eligibility
- Provide an EMI preview before applying for a loan
- Demonstrate end-to-end ML pipeline with UI integration

---


## 📁 Project Folder Structure

```
Loan_approved_system/
│
├── app/
│   └── app.py
│
├── data/
│   ├── raw/
│   │   └── loan_approval_data.csv
│   └── processed/
│       └── loan_approval_cleaned.csv
│
├── models/
│   ├── random_forest.pkl
│   └── scaler.pkl
│
├── src/
│   ├── preprocessing.py
│   ├── encoding.py
│   ├── train_models.py
│   └── evaluate_models.py
│
├── main.py
├── README.md
└── requirements.txt
```




---

## 🔄 Data Processing Flow

1. **Raw Data**
   - Loaded from `data/raw/loan_approval_data.csv`

2. **Preprocessing**
   - Missing values handled
   - Numerical data cleaned
   - Output saved as `loan_approval_cleaned.csv`

3. **Encoding**
   - Categorical features converted into numerical form
   - Same encoding logic used during training and prediction

4. **Model Training**
   - Random Forest trained on processed data
   - Model saved using `joblib`

---

## 🧾 Input Features Used

### Applicant Profile
- Age
- Gender
- Education Level
- Marital Status
- Number of Dependents

### Employment Information
- Employment Status
- Employer Category

### Financial Health
- Applicant Monthly Income
- Coapplicant Income
- Savings
- Credit Score
- Existing Loans
- Debt-to-Income (DTI) Ratio
- Financial Health Score (calculated in UI)

### Loan Request
- Loan Amount
- Loan Term (months)
- Loan Purpose
- Property Area
- Collateral Value

---

## 📊 EMI Preview Logic

The system provides an EMI preview before prediction using the standard EMI formula:

```
EMI = P × r × (1 + r)^n / ((1 + r)^n − 1)
```

Where:
- **P** = Loan Amount  
- **r** = Monthly interest rate  
- **n** = Loan tenure in months  

*(Used only for preview, not for model decision)*

---

## ▶️ How to Run the Project

### 1️⃣ Create Virtual Environment (Recommended)

```
python -m venv venv
source venv/bin/activate        # Linux / Mac
venv\Scripts\activate           # Windows
```

---

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 3️⃣ Run Streamlit App

```
cd app
streamlit run app.py
```

Then open in browser:

```
http://localhost:8501
```

---

---

## ⚠ Important Notes

- The EMI shown is an **estimate**, not a bank guarantee
- Model predictions depend on training data quality
- This project is for **educational purposes only**

---

## 🏁 Conclusion

CreditWise Loan Approval System demonstrates a complete machine learning workflow:
- Data preprocessing
- Feature encoding
- Model training
- Prediction
- User-friendly web interface

It effectively combines **data science + practical finance concepts** in a real-world use case.

---

## 👨‍🎓 Developed By
**[Kunj Vaghani]**  
B.E. IT – Machine Learning Project
