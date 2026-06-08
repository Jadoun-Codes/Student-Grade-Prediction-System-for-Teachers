"""
preprocess.py

This module handles:
1. Loading the Excel dataset
2. Removing unwanted columns
3. Checking missing values
4. Converting marks columns to numeric
5. Basic data validation
"""

import pandas as pd


class DataPreprocessor:

    def __init__(self, file_path):
        """
        Constructor
        """
        self.file_path = file_path
        self.df = None

    def load_data(self):
        """
        Load Excel file
        """
        try:
            self.df = pd.read_excel(self.file_path)

            print("✅ Dataset Loaded Successfully")
            print(f"Rows: {self.df.shape[0]}")
            print(f"Columns: {self.df.shape[1]}")

            return self.df

        except Exception as e:
            print(f"❌ Error Loading Dataset: {e}")
            return None

    def remove_unnamed_columns(self):
        """
        Remove columns like:
        Unnamed: 0
        Unnamed: 1
        """
        self.df = self.df.loc[
            :,
            ~self.df.columns.str.contains("^Unnamed")
        ]

        print("✅ Unnamed Columns Removed")

        return self.df

    def convert_marks_to_numeric(self):
        """
        Convert marks columns to numeric datatype
        """

        mark_columns = [
            "MTE",
            "INTERNAL",
            "ETE",
            "FINAL"
        ]

        for column in mark_columns:

            if column in self.df.columns:

                self.df[column] = pd.to_numeric(
                    self.df[column],
                    errors="coerce"
                )

        print("✅ Marks Converted To Numeric")

        return self.df

    def check_missing_values(self):
        """
        Display missing values
        """

        print("\n========== MISSING VALUES ==========\n")

        print(self.df.isnull().sum())

        print("\n===================================\n")

    def validate_marks(self):
        """
        Check for invalid marks
        """

        mark_columns = [
            "MTE",
            "INTERNAL",
            "ETE",
            "FINAL"
        ]

        for column in mark_columns:

            if column in self.df.columns:

                invalid_rows = self.df[
                    self.df[column] < 0
                ]

                if len(invalid_rows) > 0:
                    print(
                        f"⚠ Invalid values found in {column}"
                    )

        print("✅ Marks Validation Completed")

    def show_columns(self):
        """
        Display all column names
        """

        print("\n COLUMN NAMES n")

        for column in self.df.columns:
            print(column)

        print("\n \n")

    def clean_data(self):
        """
        Run complete preprocessing pipeline
        """

        self.load_data()

        self.remove_unnamed_columns()

        self.convert_marks_to_numeric()

        self.check_missing_values()

        self.validate_marks()

        self.show_columns()
        
        self.df.columns = (
    self.df.columns
    .astype(str)
    .str.strip()
    .str.upper()
)
        return self.df 