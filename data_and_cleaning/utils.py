import pandas as pd
import os

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

def save_table(df, name):
    file_path = os.path.join("cleaned_data", f"{name}.csv")
    if name in os.listdir(os.path.dirname(file_path)):
        os.remove(file_path)
    df.to_csv(file_path, index=False)
    return f"{name} saved at {file_path}"

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

def get_nulls(df):
    return df.isnull().mean()

def get_nans(df):
    return df.isna().mean()
