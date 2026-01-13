# data_env_setup.py -> Script for creating project enviroment and getting .csv file if not existant in project folder.

# Imports:
import zipfile
from pathlib import Path
from kaggle.api.kaggle_api_extended import KaggleApi

# Functions:
def project_env_setup(dataset_slug, target_filename):
    
    # Defining the path for folders:
    BASE_PATH = Path(".")
    RAW_DATA_PATH = BASE_PATH / "data" / "raw"
    PROCESSED_DATA_PATH = BASE_PATH / "data" / "processed"
    
    # Creating structure if non existent:
    RAW_DATA_PATH.mkdir(parents=True, exist_ok=True)
    PROCESSED_DATA_PATH.mkdir(parents=True, exist_ok=True)
    
    # Kaggle API autentification:
    api = KaggleApi()
    api.authenticate()
    
    # Checking and downloading dataset:
    downloaded_csv = RAW_DATA_PATH / target_filename
    
    # Downloading dataset if it does not exist:
    if not downloaded_csv.exists():
        print(f"\n>. Downloading dataset: kaggle.com/datasets/{dataset_slug} ...")
        
        api.dataset_download_files(dataset_slug, path=RAW_DATA_PATH)
        
        # It's downloading .zip file from kaggle...
        zip_file_path = RAW_DATA_PATH / (dataset_slug.split('/')[-1] + ".zip")
        
        # Extracting the .zip file:
        print(f">. Extracting {zip_file_path.name}...")
        with zipfile.ZipFile(zip_file_path, 'r') as zip_f:
            zip_f.extractall(RAW_DATA_PATH)
        
        # Getting only .csv files. [0] -> 1st one gets used and renamed.
        all_files = list(RAW_DATA_PATH.glob("*.csv"))    
        extracted_file = all_files[0]
        extracted_file.rename(downloaded_csv)

        # Deleting the .zip file.
        zip_file_path.unlink()
        print(f"\n>. Dataset '{target_filename}' ready")
        
    else:
        print(f"\n>. Dataset '{target_filename}' already exists!")
        
        
# Main:
def main():
    
    DATASET_SLUG = 'maharshipandya/-spotify-tracks-dataset'
    TARGET_FILENAME = 'spotify_dataset_raw.csv'

    project_env_setup(DATASET_SLUG, TARGET_FILENAME)

if __name__ == "__main__":
    main()