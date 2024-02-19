import pandas as pd
import numpy as np
import os


import os

data_dict = {
    "pib_par_industrie": {
        "path": os.path.join("data_and_cleaning", "data", "stats_can", "pib_par_industrie.csv"),
        "gran:": "industrie and monthly",
        "date_range": ["200501", "202312"],
        "nom": "pib_par_industrie",
        "delimiter": ";",
        "select": {
            "PÉRIODE DE RÉFÉRENCE": "CalendarMonth",
            "Système de classification des industries de l'Amérique du Nord (SCIAN)": "industry",
            "VALEUR": "PIB_par_industrie",
        }
    },
    "investissement_construction": {
        "path": os.path.join("data_and_cleaning", "data", "stats_can", "investissement_construction.csv"),
        "gran:": "monthly",
        "date_range": ["201701", "202312"],
        "nom": "investissement_construction",
        "delimiter": ";",
        "select": {
            "PÉRIODE DE RÉFÉRENCE": "CalendarMonth",
            "Type de structure": "structure_type",
            "Type de travaux": "work_type",
            "VALEUR": "inverstissement_construction"
        }
    },
    "construction_par_region": {
        "path": os.path.join("data_and_cleaning", "data", "stats_can", "construction_par_region.csv"),
        "gran:": "yearly, par region",
        "date_range": ["200501", "202312"],
        "nom": "construction_par_region",
        "delimiter": ";",
        "select": {
            "PÉRIODE DE RÉFÉRENCE": "CalendarYear",
            "Estimations de logement": "construction_status",
            "Type d'unité": "construction_unit_type",
            "VALEUR": "PIB_par_secteur_construction",
            "GÉO": "region",
        }
    },
    "indice_de_prix_logements": {
        "path": os.path.join("data_and_cleaning", "data", "stats_can", "indice_de_prix_logements.csv"),
        "gran:": "monthly",
        "date_range": ["200501", "202312"],
        "nom": "indice_de_prix_logements",
        "delimiter": ";",
        "select": {
            "PÉRIODE DE RÉFÉRENCE": "CalendarMonth",
            "Indices des prix des logements neufs": "new_housing_price_index",
            "VALEUR": "indice_de_prix_logements",
        }
    },
    "taux_hypothecaire_terme_5ans": {
        "path": os.path.join("data_and_cleaning", "data", "stats_can", "taux_hypothecaire_terme_5ans.csv"),
        "gran:": "monthly",
        "date_range": ["200501", "202312"],
        "nom": "taux_hypothecaire_terme_5ans",
        "delimiter": ";",
        "select": {
            "PÉRIODE DE RÉFÉRENCE": "CalendarMonth",
            "VALEUR": "taux_hypothecaire_terme_5ans",
        }
    },
    "interest_rates_bank_of_can": {
        "path": os.path.join("data_and_cleaning", "data", "stats_can", "interest_rates_bank_of_can.csv"),
        "gran:": "monthly",
        "date_range": ["200501", "202312"],
        "nom": "interest_rates_bank_of_can",
        "delimiter": ",",
        "select": {
            "REF_DATE": "CalendarMonth",
            "Rates": "rate_type",
            "VALUE": "interst_rate_value",
        }
    },
}

def save_table(df, name):
    file_path = os.path.join("data_and_cleaning", "cleaned_data", f"{name}.csv")
    if name in os.listdir(os.path.dirname(file_path)):
        os.remove(file_path)
    df.to_csv(file_path, index=False)
    return f"{name} saved at {file_path}"

def load_table(path, delimiter=',', print=False):
    df = pd.read_csv(path, delimiter=delimiter)
    if print:
        print(df.head(100))
    return df

def select_rename_columns(df, select):
    df = df.rename(columns=select)
    df = df[list(select.values())]
    return df

def extract_year(df):
    if "month_year" in df.columns:
        df["year"] = df["month_year"].str.extract(r"(\d{4})")
        df["month"] = df["month_year"].str.extract(r"-(\d{2})")
    return df

output_dict = {}

for table, table_info in data_dict.items():
    df = load_table(table_info["path"], table_info["delimiter"])
    df = select_rename_columns(df, table_info["select"])
    df = extract_year(df)
    output_dict[table] = df

def get_date_range(df):
    if "CalendarMonth" in df.columns:
        min_date = df["CalendarMonth"].min()
        max_date = df["CalendarMonth"].max()
        return f"Date range: {min_date} to {max_date}"
    elif "CalendarYear" in df.columns:
        min_date = df["CalendarYear"].min()
        max_date = df["CalendarYear"].max()
        return f"Date range: {min_date} to {max_date}"
    #print the number of records (size of the dataframe
    return f"Number of records: {df.shape[0]}"

for table, df in output_dict.items():
    print(table)
    print(get_date_range(df))

joined_df = output_dict["pib_par_industrie"].merge(
    output_dict["investissement_construction"], on=["CalendarMonth"], how="left"
).merge(
    output_dict["indice_de_prix_logements"], on=["CalendarMonth"], how="left"
).merge(
    output_dict["taux_hypothecaire_terme_5ans"], on=["CalendarMonth"], how="left"
).merge(
    output_dict["interest_rates_bank_of_can"], on=["CalendarMonth"], how="left"
)

# display the joined dataframe (fully: all columns and rows)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
print(joined_df.head(100))

save_table(joined_df, "joined_data")
