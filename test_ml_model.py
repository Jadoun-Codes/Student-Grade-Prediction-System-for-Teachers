from preprocess import DataPreprocessor
from grading import GradeManager
from ml_model import RiskModel

FILE_PATH = "Main_Dataset.xlsx"

preprocessor = DataPreprocessor(FILE_PATH)

df = preprocessor.clean_data()

grade_rules = [
    (85, 100, "O"),
    (75, 84, "A"),
    (65, 74, "B"),
    (50, 64, "C"),
    (40, 49, "D"),
    (0, 39, "F")
]

df = GradeManager.apply_grades(
    df,
    grade_rules
)

df = GradeManager.generate_risk(df)

print(df.columns.tolist())
print("\nCOLUMN NAMES:")
for col in df.columns:
    print(repr(col))
risk_model = RiskModel()

risk_model.train(df)

risk_model.feature_importance(df)

risk_model.save_model()