from prediction import RiskPredictor

predictor = RiskPredictor()

risk = predictor.predict_single(
    mte=20,
    internal=18,
    ete=15,
    final=53
)

print(
    f"Predicted Risk: {risk}"
)