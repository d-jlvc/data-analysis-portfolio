# data_extract.py -> Script for extracting data from .csv file.

# Imports:
import pandas as pd

# Functions:
def load_raw_data(file_path) -> pd.DataFrame | None:
    """Function for extracting data from .csv file."""
    
    try:
        df = pd.read_csv(file_path)
        
        print(f"\n>. File read successfuly! Printing an example...", "\n", "-"*50)
        print(df.head(5))
        print("\n>. Columns:", list(df.columns))
        print(">. Shape (rows, cols):", df.shape, "\n")
        print(">. Dataframe information:")
        print(df.info())
        
        return df
        
    except FileNotFoundError:
        print(f"\n>. File does not exist on given path: {file_path}")
        return None
    except ModuleNotFoundError:
        print(">. \nRequired module for loading file does not exist...")
        print(">. Try 'pip install pandas' and importing it for loading this dataset.")
        return None
    except Exception as e:
        print(f"Something went wrong: {e}")
        return None


# Main:   
def main():
    
    test_path = "./data/raw/spotify_dataset_raw.csv"
    load_raw_data(test_path)
    
if __name__ == "__main__":
    main()