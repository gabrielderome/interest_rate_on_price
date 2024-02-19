import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data_and_cleaning\cleaned_data\joined_data.csv", delimiter=',')

#print all columns in df
print(df.columns)

# interest_rate over time, and take out the nulls

df_interest_rate = df[['CalendarMonth', 'interest_rate_value']]
df_interest_rate = df_interest_rate.dropna().drop_duplicates()
# display the dataframe
print(df_interest_rate)
