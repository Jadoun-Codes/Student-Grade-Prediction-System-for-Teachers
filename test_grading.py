from preprocess import DataPreprocessor
from grading import GradeManager

FILE_PATH = "Main_Dataset.xlsx"

preprocessor = DataPreprocessor(FILE_PATH)

df = preprocessor.clean_data()

# Teacher-defined grading scheme
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

print(
    df[
        [
            "NAME",
            "FINAL",
            "GRADE",
            "RISK"
        ]
    ].head(10)
)