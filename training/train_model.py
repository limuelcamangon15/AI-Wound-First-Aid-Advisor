import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
import joblib
import os

data = [
    # bleeding, depth, pain, swelling, redness, pus, risk
    ("none", "surface", 2, False, False, False, "LOW"),
    ("mild", "surface", 3, False, False, False, "LOW"),
    ("mild", "moderate", 5, True, True, False, "MODERATE"),
    ("continuous", "deep", 8, True, True, False, "HIGH"),
    ("none", "moderate", 4, False, True, False, "MODERATE"),
    ("continuous", "deep", 9, True, True, True, "HIGH"),
    ("mild", "moderate", 6, True, False, False, "MODERATE"),
    ("none", "surface", 1, False, False, False, "LOW"),
    ("mild", "surface", 4, False, True, False, "MODERATE"),
    ("continuous", "moderate", 7, True, True, False, "HIGH"),
]

columns = [
    "bleeding",
    "depth",
    "pain_level",
    "swelling",
    "redness",
    "pus",
    "risk"
]

df = pd.DataFrame(data, columns=columns)

X = df.drop(columns=["risk"])
y = df["risk"]

categorical_features = ["bleeding", "depth"]
numerical_features = ["pain_level", "swelling", "redness", "pus"]

preprocessor = ColumnTransformer(
    transformers=[
        ("categorical", OneHotEncoder(), categorical_features),
        ("numerical", "passthrough", numerical_features)
    ]
)

model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("classifier", LogisticRegression(max_iter=200))
    ]
)

model.fit(X,y)

os.makedirs("model", exist_ok=True)