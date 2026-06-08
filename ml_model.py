# ml_model.py

import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)


class RiskModel:

    def __init__(self):
        self.model = RandomForestClassifier(
            n_estimators=100,
            random_state=42
        )

    def prepare_data(self, df):

        # Clean column names
        df.columns = df.columns.str.strip()

        print("\nAvailable Columns:")
        print(df.columns.tolist())

        required_columns = [
            "MTE",
            "INTERNAL",
            "ETE",
            "FINAL",
            "RISK"
        ]

        missing_columns = [
            col for col in required_columns
            if col not in df.columns
        ]

        if missing_columns:
            raise ValueError(
                f"Missing Columns: {missing_columns}"
            )

        X = df[
            [
                "MTE",
                "INTERNAL",
                "ETE",
                "FINAL"
            ]
        ]

        y = df["RISK"]

        return X, y

    def train(self, df):

        X, y = self.prepare_data(df)

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.20,
            random_state=42,
            stratify=y
        )

        self.model.fit(
            X_train,
            y_train
        )

        predictions = self.model.predict(X_test)

        accuracy = accuracy_score(
            y_test,
            predictions
        )

        print("\n========== MODEL RESULTS ==========\n")

        print(f"Accuracy: {accuracy:.2f}")

        print("\nClassification Report:\n")

        print(
            classification_report(
                y_test,
                predictions
            )
        )

        print("\nConfusion Matrix:\n")

        print(
            confusion_matrix(
                y_test,
                predictions
            )
        )

    def feature_importance(self, df):

        X, _ = self.prepare_data(df)

        importance_df = pd.DataFrame(
            {
                "Feature": X.columns,
                "Importance":
                self.model.feature_importances_
            }
        )

        importance_df = importance_df.sort_values(
            by="Importance",
            ascending=False
        )

        print("\n========== FEATURE IMPORTANCE ==========\n")

        print(importance_df)

    def save_model(self):

        os.makedirs(
            "models",
            exist_ok=True
        )

        joblib.dump(
            self.model,
            "models/risk_model.pkl"
        )

        print(
            "\n✅ Model Saved Successfully"
        )