from preprocess import DataPreprocessor

FILE_PATH = "Main_Dataset.xlsx"

preprocessor = DataPreprocessor(FILE_PATH)

df = preprocessor.clean_data()

print("\nFirst 5 Rows:\n")

print(df.head())