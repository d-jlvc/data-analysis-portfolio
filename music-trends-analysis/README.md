## MUSIC-TRENDS-ANALYSIS ETL

- This is my first project on a path to becoming an employable Data Analyst.
For now, 13/01/2026 I've managed to do the ETL of the spotify-tracks-dataset
downloaded from `kaggle`.

- Further steps will include EDA, as well as ML part where we'll train some 
models using `scikit-learn` library.

---

### Project structure:

```
┌ data/ # folder containing data for the project, raw and processed (ignored on Git.)
├── processed/
└── raw/
├ notebooks/ # not visible for now, empty, will contain .ipynb files for EDA.
├ scripts/ # containing scripts used in main.py 
├── + __init__.py
├── + data_env_setup.py - for downloading dataset and creating folders for this project's enviroment
├── + data_extract.py - for extracting data in downloaded .csv file
└── + data_transform.py - cleaning extracted data preparing it for further use
├ tests/ # empty for now.
|
├─── + main.py - You're running this script!
├─── README.md - You're reading it right now ;)
└─── requirements.txt - Dependencies you'll need to install before using main.py.
```

---

### How to run:

1. Install dependencies: `pip install -r requirements.txt`
2. Run main script: `python main.py`

- **Automatic setup:** If you have a `kaggle API`, you'll notice that the `main` will 
create data folder with all of the subfolders and will download dataset automatically 
using that kaggle API. If you do not have access to Kaggle's API, you will probably get
an error message like `OSError` or `KaggleApiError`. In that case:
- **Manual setup:** Ycan always recreate folder structure manually, download dataset from
Kaggle, add dataset to `./data/raw` and run `main` again. Link: [KaggleDatasetLink](https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset)

---

Thank you for your time, cheers!

---

**. Contact: [LinkedIn](https://www.linkedin.com/in/danilo-jelovac-b1b7a5396/)  
**. GitHub: [GitHub](https://github.com/d-jlvc)