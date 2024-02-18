import pandas as pd
import numpy as np
import os


data_dict = {
    "pib_par_industrie": {
        "path": r"data_and_cleaning\data\stats_can\pib_par_industrie.csv",
        "gran:": "industrie and monthly",
        "date_range": ["200501", "202312"],
        "nom": "pib_par_industrie",
        "delimiter": ";",
        "select": {
            "Prix": "price",
            "PÉRIODE DE RÉFÉRENCE": "month_year",
            "Système de classification des industries de l'Amérique du Nord (SCIAN)": "industry",
        }
    },
    "investissement_construction": {
        "path": r"data_and_cleaning\data\stats_can\investissement_construction.csv",
        "gran:": "monthly",
        "date_range": ["201701", "202312"],
        "nom": "investissement_construction",
        "delimiter": ";",
        "select": {
            "PÉRIODE DE RÉFÉRENCE": "month_year",
            "Type de structure": "structure_type",
            "Type de travaux": "work_type",
            "VALEUR": "inverstissement_construction"
        }
    },
    "construction_par_region": {
        "path": r"data_and_cleaning\data\stats_can\construction_par_region.csv",
        "gran:": "yearly, par region",
        "date_range": ["200501", "202312"],
        "nom": "construction_par_region",
        "delimiter": ";",
        "select": {
            "PÉRIODE DE RÉFÉRENCE": "year",
            "Estimations de logement": "construction_status",
            "Type d'unité": "construction_unit_type",
            "VALEUR": "PIB_par_secteur_construction",
            "GÉO": "region",
        }
    },
    "indice_de_prix_logements": {
        "path": r"data_and_cleaning\data\stats_can\indice_de_prix_logements.csv",
        "gran:": "monthly",
        "date_range": ["200501", "202312"],
        "nom": "indice_de_prix_logements",
        "delimiter": ";",
        "select": {
            "PÉRIODE DE RÉFÉRENCE": "month_year",
            "Indices des prix des logements neufs": "new_housing_price_index",
            "VALEUR": "indice_de_prix_logements",
        }
    },
    "taux_hypothecaire_terme_5ans": {
        "path": r"data_and_cleaning\data\stats_can\taux_hypothecaire_terme_5ans.csv",
        "gran:": "monthly",
        "date_range": ["200501", "202312"],
        "nom": "taux_hypothecaire_terme_5ans",
        "delimiter": ";",
        "select": {
            "PÉRIODE DE RÉFÉRENCE": "month_year",
            "VALEUR": "taux_hypothecaire_terme_5ans",
        }
    },
    "interest_rates_bank_of_can": {
        "path": r"data_and_cleaning\data\stats_can\interest_rates_bank_of_can.csv",
        "gran:": "monthly",
        "date_range": ["200501", "202312"],
        "nom": "interest_rates_bank_of_can",
        "delimiter": ",",
        "select": {
            "REF_DATE": "month_year",
            "Rates": "rate_type",
            "VALUE": "interst_rate_value",
        }
    },
}

def save_table(df, name):
    if name in os.listdir("data_and_cleaning/cleaned_data"):
        os.remove(f"data_and_cleaning/cleaned_data/{name}.csv")
    df.to_csv(f"data_and_cleaning/cleaned_data/{name}.csv", index=False)
    return f"{name} saved at data_and_cleaning/cleaned_data/{name}.csv"

def load_table(path, delimiter=',', print = False):
    df = pd.read_csv(f"{path}", delimiter=delimiter)
    if print == True:
        print(df.head(100))
    return df

def select_rename_columns(df, select):
    df = df.rename(columns=select)
    df = df[select.values()]
    return df

def extract_year(df):
    #if month_year column exists, extract year and month (the format that is already in the column: "yyyy-mm")
    if "month_year" in df.columns:
        df["year"] = df["month_year"].str.extract(r"(\d{4})")
        df["month"] = df["month_year"].str.extract(r"-(\d{2})")
    return df


output_dict = {}

for table in data_dict:
    df = load_table(data_dict[table]["path"], data_dict[table]["delimiter"])
    df = select_rename_columns(df, data_dict[table]["select"])
    #if month_year column exists, print the df[month_year]
    df = extract_year(df)
    # save the df in the output dict
    output_dict[table] = df
    
def get_date_range(df):
    if "month_year" in df.columns:
        min = df["month_year"].min()
        max = df["month_year"].max()
        return f"Date range: {min} to {max}"
    
# for table in output_dict, print the first 5 rows for all columns and print a summary of each column and its datatype
# for table in output_dict:
#     print(table)
#     print(output_dict[table].head(5))
#     print(output_dict[table].info())




# for all tables in output_dict, get the date range
for table in output_dict:
    print(table)
    print(get_date_range(output_dict[table]))


     



            