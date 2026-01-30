import pandas as pd
from sklearn.impute import SimpleImputer

def preprocess_raw_data(raw_path, processed_path):
    data = pd.read_csv(raw_path)

    numerical_cols = data.select_dtypes(include="number").columns
    categorical_cols = data.select_dtypes(include="object").columns

    num_imp = SimpleImputer(strategy="mean")
    cat_imp = SimpleImputer(strategy="most_frequent")

    data[numerical_cols] = num_imp.fit_transform(data[numerical_cols])
    data[categorical_cols] = cat_imp.fit_transform(data[categorical_cols])

    # remove ID
    data.drop("Applicant_ID", axis=1, inplace=True)

    # save clean data
    data.to_csv(processed_path, index=False)

    return data
