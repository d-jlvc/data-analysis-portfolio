# main.py -> Main script for loading and data transformation.

# Imports:
from scripts.data_extract import load_raw_data
from scripts.data_transform import clean_data
from scripts.data_env_setup import project_env_setup

# Paths:
DATASET_SLUG = 'maharshipandya/-spotify-tracks-dataset'
FILENAME = 'raw_data.csv'
RAW_FILE_PATH = f'./data/raw/{FILENAME}'
SAVE_FILE_PATH = "./data/processed/processed_data.csv"


# Main program:
project_env_setup(DATASET_SLUG, FILENAME)

raw_df = load_raw_data(RAW_FILE_PATH)
clean_df = clean_data(raw_df).to_csv(SAVE_FILE_PATH, index=False)
