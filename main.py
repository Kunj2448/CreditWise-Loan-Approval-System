import joblib
from src.preprocessing import preprocess_raw_data
from src.encoding import encode_clean_data
from src.train_models import train_models
from src.evaluate_models import evaluate

RAW_PATH = "data/raw/loan_approval_data.csv"
PROCESSED_PATH = "data/processed/loan_approval_cleaned.csv"

# Step 1: Clean raw data
clean_data = preprocess_raw_data(RAW_PATH, PROCESSED_PATH)

# Step 2: Encode clean data
featured_data = encode_clean_data(clean_data)

# Step 3: Train models
models, scaler, X_test, X_test_scaled, y_test = train_models(featured_data)

# Step 4: Evaluate all models
print("\nModel Evaluation Results:\n")

for name, model in models.items():
    if name in ["Logistic", "KNN", "GNB"]:
        metrics = evaluate(model, X_test_scaled, y_test)
    else:
        metrics = evaluate(model, X_test, y_test)

    print(f"{name}: {metrics}")

# Step 5: Save best model (Random Forest)
joblib.dump(models["RF"], "models/random_forest.pkl")
joblib.dump(scaler, "models/scaler.pkl")

print("\n✅ Pipeline completed successfully")
