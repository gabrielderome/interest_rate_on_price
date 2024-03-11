import pandas as pd
import os


def agg_pib(df):
    # print all the unique values in industry
    # print(df["industry"].unique())
    categories = [
        "All industries [T001]",
        "Energy sector [T016]",
        "Public Sector [T018]",
        "Construction [23]",
        'Transportation and warehousing [48-49]',
        "Real estate and rental and leasing [53]",
        "Finance and insurance [52]"
        ]
    # i want to take this df which has one entry per categories per month and make it so for that for each month, i only have one entry with columns for each of the categories
    df = df[df["industry"].isin(categories)]
    df = df.pivot(index="CalendarMonth", columns="industry", values="PIB_par_industrie")
    df = df.reset_index()
    return df

def agg_investissement(df):
    # keep only the records where structure_type == "Résidentiel et non résidentiel" AND work_type == "Total"
    df = df[(df["structure_type"] == "Résidentiel et non résidentiel") & (df["work_type"] == "Total")]
    df = df.reset_index()
    # drop index column
    df = df.drop(columns=["structure_type", "work_type", "index"])
    return df

def agg_construction(df):
    df = df[(df["construction_status"] == "Logements (achèvements)") & (df["construction_unit_type"] == "Total d'unités")]
    df = df.drop(columns=["construction_status", "construction_unit_type"])
    return df

def agg_price_index(df):
    df = df.pivot(index="CalendarMonth", columns="new_housing_price_index", values="indice_de_prix_logements")
    df = df.reset_index()
    return df

def agg_demo(df):
    # df = df.drop(columns=['GEO', 'DGUID', 'UOM', 'UOM_ID', 'SCALAR_FACTOR', 'SCALAR_ID', 'VECTOR', 'COORDINATE', 'STATUS', 'SYMBOL', 'TERMINATED', 'DECIMALS'])
    # in the df we have 1 entry per REF_DATE per Components of population growth. i would like to have only 1 entry per ref_date, with columns for each values of 'Components of population growth'
    df = df.pivot(index='REF_DATE', columns='Components of population growth', values='VALUE')
    # can we drop GEO, DGUID, UOM, UOM_ID, SCALAR_FACTOR, SCALAR_ID, VECTOR, COORDINATE, STATUS, SYMBOL, TERMINATED, DECIMALS
    df = df.reset_index()
    df = df.drop(columns=['Net emigration', 'Net interprovincial migration', 'Net non-permanent residents', 'Net temporary emigration', 'Non-permanent residents, inflows', 'Non-permanent residents, outflows', 'Residual deviation', 'Returning emigrants'])
    # rename REF_DATE to CalendarYear
    df = df.rename(columns={'REF_DATE': 'CalendarYear'})
    # take only the 4 last digits of the CalendarYear
    df['CalendarYear'] = df['CalendarYear'].str[-4:].astype(int)
    return df