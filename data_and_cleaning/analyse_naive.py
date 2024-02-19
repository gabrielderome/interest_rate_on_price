import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from import_data import load_table

df = load_table("data_and_cleaning\cleaned_data\joined_data.csv")

#print all columns in df
print(df.columns)
