import streamlit as st
import pandas as pd
import joblib

# -------------------------------------------------
# Page config
# -------------------------------------------------
st.set_page_config(
    page_title="Loan Approval System",
    page_icon="🏦",
    layout="wide"
)

# -------------------------------------------------
# CSS (clean + modern)
# -------------------------------------------------
st.markdown("""
<style>
.block-container { padding: 3rem 7rem; }
.card {
    background: #0f172a;
    padding: 28px;
    border-radius: 20px;
    margin-bottom: 30px;
    border: 1px solid #1f2937;
}
.big-btn button {
    height: 3.5rem;
    font-size: 20px;
}
.approve {
    background: linear-gradient(135deg,#16a34a,#22c55e);
    padding: 45px;
    border-radius: 25px;
    font-size: 34px;
    text-align: center;
    color: white;
}
.reject {
    background: linear-gradient(135deg,#b91c1c,#ef4444);
    padding: 45px;
    border-radius: 25px;
    font-size: 34px;
    text-align: center;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# Load model
# -------------------------------------------------
model = joblib.load("models/random_forest.pkl")

# -------------------------------------------------
# Header
# -------------------------------------------------
st.markdown("""
<h1 style="text-align:center;">🏦 Loan Approval System</h1>
<p style="text-align:center;font-size:20px;color:#94a3b8;">
Instant AI-based loan eligibility check
</p>
""", unsafe_allow_html=True)

st.divider()

# -------------------------------------------------
# Progress Bar (THIS CHANGES FEEL)
# -------------------------------------------------
progress = st.progress(0)

# -------------------------------------------------
# Applicant Profile
# -------------------------------------------------
with st.expander("👤 Applicant Profile", expanded=True):
    col1, col2, col3 = st.columns(3)
    with col1:
        Age = st.slider("Age", 18, 70, 30)
        Gender = st.selectbox("Gender", ["Male", "Female"])
    with col2:
        Education_Level = st.selectbox("Education Level", ["Graduate", "Not Graduate"])
        Marital_Status = st.selectbox("Marital Status", ["Married", "Single"])
    with col3:
        Dependents = st.selectbox("Dependents", [0,1,2,3,4],help="Number of family members financially dependent on you.")

progress.progress(25)

# -------------------------------------------------
# Employment
# -------------------------------------------------
with st.expander("💼 Employment Information", expanded=True):
    col1, col2 = st.columns(2)
    with col1:
        Employment_Status = st.selectbox(
            "Employment Status",
            ["Salaried", "Self-employed", "Unemployed"]
        )
    with col2:
        Employer_Category = st.selectbox(
            "Employer Category",
            ["Government", "Private", "MNC", "Unemployed"],help="Your current working type. Example: salaried job or self business."
        )

progress.progress(50)

# -------------------------------------------------
# Financial Strength (LIVE FEEDBACK)
# -------------------------------------------------
with st.expander("💰 Financial Health", expanded=True):
    col1, col2, col3 = st.columns(3)

    with col1:
        Applicant_Income = st.number_input(
            "Monthly Income (₹)", 5000.0, 500000.0, 40000.0, step=1000.0,help="Your average monthly income before tax. Example: salary or business income."

        )
        Savings = st.number_input(
            "Savings (₹)", 0.0, 2000000.0, 100000.0, step=10000.0,help="Monthly income of co-borrower (spouse or family member). Enter 0 if not applicable."

        )

    with col2:
        Credit_Score = st.slider("Credit Score", 300, 900, 700,help="A number that shows how well you repay loans. Higher score means better chance of approval.")
        Existing_Loans = st.number_input("Existing Loans", 0, 10, 0)

    with col3:
        Coapplicant_Income = st.number_input(
            "Coapplicant Income (₹)", 0.0, 300000.0, 0.0, step=1000.0
        )
        DTI_Ratio = st.slider("DTI Ratio", 0.0, 0.8, 0.3,help="Part of your income already used to pay loans. Lower value means less financial burden.")

    # Live health score
    health = (
        (Credit_Score / 900) * 0.5 +
        max(0, (0.8 - DTI_Ratio)) * 0.3 +
        min(Applicant_Income / 100000, 1) * 0.2
    )

    st.metric(
        "Financial Health Score",
        f"{int(health*100)}/100",
        "Good" if health > 0.6 else "Risky"
    )

progress.progress(75)

# -------------------------------------------------
# Loan Request
# -------------------------------------------------
with st.expander("📄 Loan Request", expanded=True):
    col1, col2, col3 = st.columns(3)

    with col1:
        Loan_Amount = st.number_input(
            "Loan Amount (₹)", 50000.0, 5000000.0, 500000.0, step=10000.0
        )
        Loan_Term = st.number_input(
            "Loan Term (months)", 6, 360, 240, step=6,
            help="Typical ranges: Personal (6–60), Car (12–84), Home (60–360)"

        )

    with col2:
        Loan_Purpose = st.selectbox(
            "Loan Purpose", ["Home", "Education", "Car", "Personal"]
        )
        Property_Area = st.selectbox(
            "Property Area", ["Urban", "Semiurban", "Rural"],help="Location type of the property related to the loan."

        )

    with col3:
        Collateral_Value = st.number_input(
            "Collateral Value (₹)", 0.0, 10000000.0, 0.0, step=50000.0,help="Market value of property or asset you are giving as security. Enter 0 if no collateral."
        )

progress.progress(100)
# =========================================================
# EMI PREVIEW (USER FRIENDLY)
# =========================================================
#st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("<div class='section-title'>📊 EMI Preview</div>", unsafe_allow_html=True)

# Assumed annual interest rate (for preview only)
annual_interest_rate = 0.09  # 9%
monthly_rate = annual_interest_rate / 12

# EMI calculation (safe formula)
if Loan_Term > 0:
    emi = (
        Loan_Amount * monthly_rate * (1 + monthly_rate) ** Loan_Term
    ) / (
        (1 + monthly_rate) ** Loan_Term - 1
    )
else:
    emi = 0

total_income = Applicant_Income + Coapplicant_Income
emi_ratio = emi / total_income if total_income > 0 else 0

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Estimated EMI (₹ / month)",
        f"{emi:,.0f}"
    )

with col2:
    st.metric(
        "Loan Tenure",
        f"{Loan_Term} months"
    )

with col3:
    st.metric(
        "EMI / Income Ratio",
        f"{emi_ratio:.2f}"
    )

# Affordability message (VERY IMPORTANT)
if emi_ratio > 0.5:
    st.warning("⚠️ EMI is high compared to income. Loan approval chances may reduce.")
elif emi_ratio > 0.35:
    st.info("ℹ️ EMI is manageable but slightly high.")
else:
    st.success("✅ EMI looks affordable based on your income.")

st.markdown("</div>", unsafe_allow_html=True)


# -------------------------------------------------
# Encoding (same as training)
# -------------------------------------------------
Education_Level = 1 if Education_Level == "Graduate" else 0

encoded = {
    "Employment_Status_Salaried": Employment_Status == "Salaried",
    "Employment_Status_Self-employed": Employment_Status == "Self-employed",
    "Employment_Status_Unemployed": Employment_Status == "Unemployed",
    "Marital_Status_Single": Marital_Status == "Single",
    "Loan_Purpose_Car": Loan_Purpose == "Car",
    "Loan_Purpose_Education": Loan_Purpose == "Education",
    "Loan_Purpose_Home": Loan_Purpose == "Home",
    "Loan_Purpose_Personal": Loan_Purpose == "Personal",
    "Property_Area_Semiurban": Property_Area == "Semiurban",
    "Property_Area_Urban": Property_Area == "Urban",
    "Gender_Male": Gender == "Male",
    "Employer_Category_Government": Employer_Category == "Government",
    "Employer_Category_MNC": Employer_Category == "MNC",
    "Employer_Category_Private": Employer_Category == "Private",
    "Employer_Category_Unemployed": Employer_Category == "Unemployed"
}

input_data = {
    "Applicant_Income": Applicant_Income,
    "Coapplicant_Income": Coapplicant_Income,
    "Age": Age,
    "Dependents": Dependents,
    "Credit_Score": Credit_Score,
    "Existing_Loans": Existing_Loans,
    "DTI_Ratio": DTI_Ratio,
    "Savings": Savings,
    "Collateral_Value": Collateral_Value,
    "Loan_Amount": Loan_Amount,
    "Loan_Term": Loan_Term,
    "Education_Level": Education_Level
}

input_data.update({k: int(v) for k, v in encoded.items()})
df = pd.DataFrame([input_data])
df = df.reindex(columns=model.feature_names_in_, fill_value=0)

# -------------------------------------------------
# Final Decision (BIG MOMENT)
# -------------------------------------------------
st.divider()

st.markdown('<div class="big-btn">', unsafe_allow_html=True)
check = st.button("🚀 Check Loan Eligibility", use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

if check:
    prob = model.predict_proba(df)[0][1]

    if prob >= 0.5:
        st.markdown(
            f"<div class='approve'>✅ LOAN APPROVED<br>"
            f"<small>Confidence: {prob:.2%}</small></div>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"<div class='reject'>❌ LOAN REJECTED<br>"
            f"<small>Risk Probability: {1-prob:.2%}</small></div>",
            unsafe_allow_html=True
        )
