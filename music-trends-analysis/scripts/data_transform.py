# data_transform.py -> Functions for data cleaning and transformation.

# Imports:
import pandas as pd
from scripts.data_extract import load_raw_data

# Functions:
def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Function for cleaning raw data and preparing it for analysis"""
    
    # Creating a copy of an original df.
    df_cleaned = df.copy()
    
    # Removing duplicates:
    print("\n>. Checking for duplicates...")
    if df_cleaned.duplicated().sum() == 0:
        print(">. No duplicates found!")
    else:
        print(">. Duplicates found:", df_cleaned.duplicated().sum())
        print(">. Handling duplicates...")
        df_cleaned = df_cleaned.drop_duplicates(keep='first')
        print(">. Duplicates dropped!")
    
    # Handling NaNs:
    print("\n>. Missing values count:")
    print(df_cleaned.isna().sum())
    print(">. Handling missing values...")
    df_cleaned = df_cleaned.dropna(axis='index')
    print(">. Missing values handled successfuly!")
    print(df_cleaned.isna().sum())
    
    # Keeping neccessary columns:
    cols_to_keep = ['artists', 'track_name', 'popularity', 'danceability', 'energy', 'loudness', 'tempo', 'mode', 'explicit']
    print("\n>. Keeping neccessary columns for analysis:", cols_to_keep)
    df_cleaned = df_cleaned[cols_to_keep]
    print("\n>. Dataframe optimized. Printing an example...", "\n", "-"*50)
    print(df_cleaned.head(5))
    print("\n>. Shape (rows, cols):", df_cleaned.shape, "\n")
    print(">. Dataframe information:")
    print(df_cleaned.info())
    
    return df_cleaned
    
    
# Main:
def main():
    
    # Loading data:
    test_path = "./data/raw/spotify_dataset_raw.csv"
    df = load_raw_data(test_path)
    
    # Cleaning data:
    df_cleaned = clean_data(df)

if __name__ == "__main__":
    main()
    
   