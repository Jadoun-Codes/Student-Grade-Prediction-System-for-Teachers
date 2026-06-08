from preprocess import DataPreprocessor
from analytics import Analytics

FILE_PATH = "Main_Dataset.xlsx"

preprocessor = DataPreprocessor(FILE_PATH)

df = preprocessor.clean_data()

stats = Analytics.get_statistics(df)

print("\n  CLASS STATISTICS \n")

for key, value in stats.items():
    print(f"{key}: {value}")