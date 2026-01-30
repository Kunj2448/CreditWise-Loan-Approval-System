import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

def encode_clean_data(data):
    le = LabelEncoder()

    data["Education_Level"] = le.fit_transform(data["Education_Level"])
    data["Loan_Approved"] = le.fit_transform(data["Loan_Approved"])

    cols = [
        "Employment_Status",
        "Marital_Status",
        "Loan_Purpose",
        "Property_Area",
        "Gender",
        "Employer_Category"
    ]

    ohe = OneHotEncoder(
        drop="first",
        sparse_output=False,
        handle_unknown="ignore"
    )

    encoded = ohe.fit_transform(data[cols])

    encoded_df = pd.DataFrame(
        encoded,
        columns=ohe.get_feature_names_out(cols),
        index=data.index
    )

    data = pd.concat(
        [data.drop(columns=cols), encoded_df],
        axis=1
    )

    return data
