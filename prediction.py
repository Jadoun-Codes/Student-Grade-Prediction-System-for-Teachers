# prediction.py

import joblib
import pandas as pd


class RiskPredictor:

    def __init__(self):

        self.model = joblib.load(
            "models/risk_model.pkl"
        )

    def predict_single(
        self,
        mte,
        internal,
        ete,
        final
    ):

        data = pd.DataFrame(
            {
                "MTE": [mte],
                "INTERNAL": [internal],
                "ETE": [ete],
                "FINAL": [final]
            }
        )

        prediction = self.model.predict(data)

        return prediction[0]

    def predict_dataframe(self, df):

        features = df[
            [
                "MTE",
                "INTERNAL",
                "ETE",
                "FINAL"
            ]
        ]

        predictions = self.model.predict(
            features
        )

        df["PREDICTED_RISK"] = predictions

        return df