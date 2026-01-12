# main.py -> Main script for loading and data transformation.

# Imports:
import pandas as pd

from scripts.data_extract import load_raw_data
from scripts.data_transform import clean_data

# Paths:
LOAD_FILE_PATH = "./data/raw/spotify_dataset_raw.csv"
SAVE_FILE_PATH = "./data/processed/spotify_dataset_processed.csv"

# Main program:
raw_df = load_raw_data(LOAD_FILE_PATH)
clean_df = clean_data(raw_df).to_csv(SAVE_FILE_PATH, index=False)
