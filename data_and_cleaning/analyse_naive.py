import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data_and_cleaning\cleaned_data\joined_data.csv", delimiter=',')

#print all columns in df
print(df.columns)


def plot_interest_rate():
    # taux_hypothecaire_terme_5ans over time, and take out the nulls
    df_taux_hypothecaire_terme_5ans = df[['CalendarMonth', 'taux_hypothecaire_terme_5ans']]
    df_taux_hypothecaire_terme_5ans = df_taux_hypothecaire_terme_5ans.dropna().drop_duplicates()
    df_interest = df[['CalendarMonth', "interest_rate_value", "rate_type"]]
    # print all unique values in df_interest['rate_type']
    print(df_interest['rate_type'].unique())
    long_term_benchmark_bond = df_interest[df_interest['rate_type'] == "Selected Government of Canada benchmark bond yields: long term"].dropna().drop_duplicates()
    five_year_benchmark_bond = df_interest[df_interest['rate_type'] == "Selected Government of Canada benchmark bond yields: 5 year"].dropna().drop_duplicates()
    # set the style to dark background
    plt.style.use('dark_background')
    # plot the data from df_taux_hypothecaire_terme_5ans
    plt.plot(df_taux_hypothecaire_terme_5ans['CalendarMonth'], df_taux_hypothecaire_terme_5ans['taux_hypothecaire_terme_5ans'], label='taux hypothecaire terme 5 ans', color='cyan')
    # plot the data from five_year_benchmark_bond
    plt.plot(five_year_benchmark_bond['CalendarMonth'], five_year_benchmark_bond['interest_rate_value'], label='five year benchmark bond', color='yellow')
    # plot the data from long_term_benchmark_bond
    plt.plot(long_term_benchmark_bond['CalendarMonth'], long_term_benchmark_bond['interest_rate_value'], label='long term benchmark bond', color='magenta')
    plt.ylim(0, 10)  # set the limits of y-axis from 0 to 10
    # get the current locations and labels
    locs, labels = plt.xticks()
    # set labels to display only one out of every 24 months and rotate them vertically
    plt.xticks(locs[::48], df_taux_hypothecaire_terme_5ans['CalendarMonth'][::48], color='white')
    # set the color of y-axis labels to white
    plt.yticks(color='white')
    # add a legend with white text
    plt.legend(facecolor='black', edgecolor='white', labelcolor='white')
    # display the plot
    return plt.savefig('interest_rates.png', dpi=300, bbox_inches='tight')  

plot_interest_rate()