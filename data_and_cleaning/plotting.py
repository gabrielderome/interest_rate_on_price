import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import ticker
import os
from utils import load_table, select_rename_columns, extract_year, save_table, get_date_range, get_nulls, get_nans
import seaborn as sns
from scipy.stats import spearmanr, pearsonr


def plot_spearman_corr(df, save=False):
    plt.figure(figsize=(10, 10))
    sns.heatmap(df.corr(method='spearman'), annot=True, fmt=".2f", cmap='coolwarm')
    plt.title("Spearman correlation")
    if save:
        plt.savefig("plots\\spearman_corr.png")
    plt.show()
    return

def plot_pearson_corr(df, save=False):
    corr = df.corr()
    fig, ax = plt.subplots(figsize=(10, 10))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap='coolwarm', ax=ax)
    plt.title("Pearson Correlation")
    plt.tight_layout()
    if save:
        plt.savefig('plots\\pearson_corr.png')
    plt.show()
    return

def plot_interest_rate(df, save=False):
    df_interest_rate = df[['CalendarMonth', 'taux_hypothecaire_terme_5ans']]
    df_interest_rate = df_interest_rate.dropna()
    df_interest_rate = df_interest_rate.sort_values(by='CalendarMonth')
    df_interest_rate['CalendarMonth'] = pd.to_datetime(df_interest_rate['CalendarMonth'])
    df_interest_rate = df_interest_rate.set_index('CalendarMonth')
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df_interest_rate.index, df_interest_rate['taux_hypothecaire_terme_5ans'])
    ax.set_title('Interest Rate Over Time')
    ax.set_xlabel('Date')
    ax.set_ylabel('Interest Rate')
    ax.set_facecolor('black')
    fig.patch.set_facecolor('black')
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.spines['bottom'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.title.set_color('white')
    if save == False:
        return plt.show()
    else:
        return plt.savefig('plots\\interest_rates.png', dpi=300, bbox_inches='tight')
    
def plot_new_price_index_and_rate(df, save=False):
    # i want to create a plot where the x axis is the date(calendarmonth) and where there are two y axis one for the new housing price index and one for the interest rate
    df_interest_rate = df[['CalendarMonth', 'taux_hypothecaire_terme_5ans', 'price_index_total']]
    df_interest_rate = df_interest_rate.dropna()
    df_interest_rate = df_interest_rate.sort_values(by='CalendarMonth')
    df_interest_rate['CalendarMonth'] = pd.to_datetime(df_interest_rate['CalendarMonth'])
    df_interest_rate = df_interest_rate.set_index('CalendarMonth')
    fig, ax1 = plt.subplots(figsize=(10, 5))
    ax2 = ax1.twinx()
    ax1.plot(df_interest_rate.index, df_interest_rate['taux_hypothecaire_terme_5ans'], 'g-')
    ax2.plot(df_interest_rate.index, df_interest_rate['price_index_total'], 'b-')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Interest Rate', color='g')
    ax2.set_ylabel('Price Index Total', color='b')
    ax1.set_facecolor('black')
    fig.patch.set_facecolor('black')

    ax1.tick_params(axis='x', colors='white')
    ax1.tick_params(axis='y', colors='white')
    ax2.tick_params(axis='x', colors='white')
    ax2.tick_params(axis='y', colors='white')
    ax1.spines['bottom'].set_color('white')
    ax1.spines['left'].set_color('white')
    ax2.spines['bottom'].set_color('white')
    ax2.spines['right'].set_color('white')
    ax2.spines['left'].set_color('white')
    ax1.title.set_color('white')
    if save == False:
        return plt.show()
    else:
        return plt.savefig('plots\\interest_rates_and_price_index.png', dpi=300, bbox_inches='tight')

def plot_inv_and_rate(df, save=False):
    # i want to plot the investment in construction ("inverstissement_construction") and the interest rate ("Calendarmonth") on the same plot as y axis and the date as the x axis
    df_interest_rate = df[['CalendarMonth', 'taux_hypothecaire_terme_5ans', 'inverstissement_construction']]
    df_interest_rate = df_interest_rate.dropna()
    df_interest_rate = df_interest_rate.sort_values(by='CalendarMonth')
    df_interest_rate['CalendarMonth'] = pd.to_datetime(df_interest_rate['CalendarMonth'])
    df_interest_rate = df_interest_rate.set_index('CalendarMonth')
    fig, ax1 = plt.subplots(figsize=(10, 5))
    ax2 = ax1.twinx()
    ax1.plot(df_interest_rate.index, df_interest_rate['taux_hypothecaire_terme_5ans'], 'g-')
    ax2.plot(df_interest_rate.index, df_interest_rate['inverstissement_construction'], 'b-')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Interest Rate', color='g')
    ax2.set_ylabel('Investment in Construction', color='b')
    ax1.set_facecolor('black')
    fig.patch.set_facecolor('black')
    # set the axis and label colors
    ax1.tick_params(axis='x', colors='white')
    ax1.tick_params(axis='y', colors='white')
    ax2.tick_params(axis='x', colors='white')
    ax2.tick_params(axis='y', colors='white')
    ax1.spines['bottom'].set_color('white')
    ax1.spines['left'].set_color('white')
    ax2.spines['bottom'].set_color('white')
    ax2.spines['right'].set_color('white')
    ax2.spines['left'].set_color('white')
    ax1.title.set_color('white')
    
    if save == False:
        return plt.show()
    else:
        return plt.savefig('plots\\interest_rates_and_invest.png', dpi=300, bbox_inches='tight')