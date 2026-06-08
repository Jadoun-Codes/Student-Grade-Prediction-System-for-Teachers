

class Analytics:

    @staticmethod
    def get_highest_marks(df):
        return df["FINAL"].max()

    @staticmethod
    def get_lowest_marks(df):
        return df["FINAL"].min()

    @staticmethod
    def get_average_marks(df):
        return round(df["FINAL"].mean(), 2)

    @staticmethod
    def get_total_students(df):
        return len(df)

    @staticmethod
    def get_statistics(df):

        stats = {
            "Highest Marks": Analytics.get_highest_marks(df),
            "Lowest Marks": Analytics.get_lowest_marks(df),
            "Average Marks": Analytics.get_average_marks(df),
            "Total Students": Analytics.get_total_students(df)
        }

        return stats