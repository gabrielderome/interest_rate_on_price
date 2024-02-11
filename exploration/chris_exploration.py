import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

# Load the data
def load_table(path, delimiter=','):
    df = pd.read_csv(f"{path}", delimiter=delimiter)
    print(df.head(100))
    return df

path = r"data_and_cleaning\data\stats_can\pib_par_industrie.csv"

df = load_table(path, delimiter=';')

