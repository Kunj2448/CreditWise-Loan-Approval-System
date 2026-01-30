from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

def train_models(data):
    X = data.drop("Loan_Approved", axis=1)
    y = data["Loan_Approved"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    models = {
        "Logistic": LogisticRegression(class_weight="balanced"),
        "KNN": KNeighborsClassifier(n_neighbors=9),
        "GNB": GaussianNB(),
        "DT": DecisionTreeClassifier(random_state=42),
        "RF": RandomForestClassifier(
            n_estimators=300,
            max_depth=8,
            min_samples_leaf=8,
            class_weight="balanced",
            random_state=42
        )
    }

    models["Logistic"].fit(X_train_scaled, y_train)
    models["KNN"].fit(X_train_scaled, y_train)
    models["GNB"].fit(X_train_scaled, y_train)
    models["DT"].fit(X_train, y_train)
    models["RF"].fit(X_train, y_train)

    return models, scaler, X_test, X_test_scaled, y_test
