# grading.py

class GradeManager:

    @staticmethod
    def assign_grade(mark, grade_rules):
        """
        Assign grade based on teacher-defined rules

        grade_rules format:
        [
            (85, 100, "O"),
            (75, 84, "A"),
            (65, 74, "B")
        ]
        """

        for min_marks, max_marks, grade in grade_rules:

            if min_marks <= mark <= max_marks:
                return grade

        return "NA"

    @staticmethod
    def apply_grades(df, grade_rules):
        """
        Apply grades to all students
        """

        df["GRADE"] = df["FINAL"].apply(
            lambda mark: GradeManager.assign_grade(
                mark,
                grade_rules
            )
        )

        return df

    @staticmethod
    def generate_risk(df):
        """
        Generate risk labels from grades
        """

        risk_mapping = {
            "O": "Low",
            "A": "Low",
            "B": "Medium",
            "C": "Medium",
            "D": "High",
            "F": "High"
        }

        df["RISK"] = df["GRADE"].map(risk_mapping)

        return df