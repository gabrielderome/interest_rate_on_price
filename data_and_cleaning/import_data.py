import pandas as pd
import numpy as np
import os


data_dict = {
    "pib_par_industrie": {
        "path": r"data_and_cleaning\data\stats_can\pib_par_industrie.csv",
        "gran:": "industrie and monthly",
        "date_range": ["200501", "202312"],
        "nom": "pib_par_industrie",
        "delimiter": ";"
    },
    "investissement_construction": {
        "path": r"data_and_cleaning\data\stats_can\investissement_construction.csv",
        "gran:": "monthly",
        "date_range": ["201701", "202312"],
        "nom": "investissement_construction",
        "delimiter": ";"
    },
    "construction_par_region": {
        "path": r"data_and_cleaning\data\stats_can\construction_par_region.csv",
        "gran:": "yearly, par region",
        "date_range": ["200501", "202312"],
        "nom": "construction_par_region",
        "delimiter": ";"
    },
    "indice_de_prix_logements": {
        "path": r"data_and_cleaning\data\stats_can\indice_de_prix_logements.csv",
        "gran:": "monthly",
        "date_range": ["200501", "202312"],
        "nom": "indice_de_prix_logements",
        "delimiter": ";"
    },
    "taux_hypothecaire_terme_5ans": {
        "path": r"data_and_cleaning\data\stats_can\taux_hypothecaire_terme_5ans.csv",
        "gran:": "monthly",
        "date_range": ["200501", "202312"],
        "nom": "taux_hypothecaire_terme_5ans",
        "delimiter": ";"
    },
    "interest_rates_bank_of_can": {
        "path": r"data_and_cleaning\data\stats_can\interest_rates_bank_of_can.csv",
        "gran:": "monthly",
        "date_range": ["200501", "202312"],
        "nom": "interest_rates_bank_of_can",
        "delimiter": ";"
    },
}

def save_table(df, name):
    if name in os.listdir("data_and_cleaning/cleaned_data"):
        os.remove(f"data_and_cleaning/cleaned_data/{name}.csv")
    df.to_csv(f"data_and_cleaning/cleaned_data/{name}.csv", index=False)
    return f"{name} saved at data_and_cleaning/cleaned_data/{name}.csv"

def load_table(path, delimiter=','):
    df = pd.read_csv(f"{path}", delimiter=delimiter)
    print(df.head(100))
    return df

for table in data_dict:
    name = data_dict[table]["nom"]
    data_dict[name]["df"] = load_table(data_dict[table]["path"], delimiter = ";")
    df = data_dict[table]["df"]
    print(f"Table: {name}")
    #for each columns in the dataframe print each columns and if they are a string print all possible values
    for col in df.columns:
        print(f"Column: {col}")
        if df[col].dtype == np.dtype('O'):
            print(f"Unique values: {df[col].unique()}")
            