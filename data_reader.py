import os
import numpy as np
import pandas as pd
from visuals import map_country

"""Datasets of interest:
big-mac-full-index.csv: Big mac index- The economist
CurrenciesDataBase.db Data collected daily from localbitcoins
country-code: Relation currency & countries
"""
# Defining path to files:

path_to_big_mac = os.path.abspath('./data/big_mac_index/big-mac-full-index.csv')
path_to_currencies = "sqlite:///data/CurrenciesDataBase_V2.db"
path_to_country = os.path.abspath("./data/country-currency_code/country-code-to-currency-code-mapping.csv")


# Reading files:

df_big_mac = pd.read_csv(path_to_big_mac)
df_big_mac["date"] = pd.to_datetime(df_big_mac.date)
df_big_mac = df_big_mac.sort_values(by="date", axis=0)


df_market = pd.read_sql('currencies_vs_btc', path_to_currencies)
df_country = pd.read_csv(path_to_country)


## Merge market data with countries dataset 

df_market_mapping = pd.merge(df_market, df_country, on = 'currency_code', how = 'inner')
df_market_mapping.dropna(inplace=True)

###IGNORING DATA POINTS FOR VENEZUELA
df_market_mapping = df_market_mapping.loc[df_market_mapping["country"] != "Venezuela"]
#####


def pct_change(df, currency_code, date_reference):

    """### Pct performs calculation of percentual variation on exhange rate,
        date_reference = "2021-10-03 First data point on dataset"""
    
    ## Select currency for calculations:
    df_exchange = df[df['currency_code'] == currency_code ]

    ## Select date to calculate reference

    df_date_reference = df_exchange.loc[(df_exchange.date).dt.date == pd.Timestamp(date_reference)]

    ### Averare exchange rate for day of reference:

    implicit_exchange_reference = df_date_reference.implicit_exchange.mean()

    ### Percentual Variation

#     equation = ((df_exchange.implicit_exchange / implicit_exchange_reference)-1)*100
    
    return implicit_exchange_reference

def metrics(df, currency_code):

    implicit_exchange = df[df['currency_code'] == currency_code ]
    
    metric_exchange_rate = round(implicit_exchange["implicit_exchange"].values[-1], 2 )

    metric_pct = round(implicit_exchange["pct"].values[-1], 2)

    metric_volume_btc = round(implicit_exchange['volume_btc'].values[-1], 4)

    return metric_exchange_rate, metric_pct, metric_volume_btc

def top_variation_value(number, columns, df = df_market_mapping):

    """Get the n largest value for a given column on df_market_mapping"""

    top_variations = df_market_mapping[["country",f"{columns}"]].nlargest(n=number, columns=columns)
    top_variations = top_variations.drop_duplicates(subset="country")
    top_variations.set_index("country", inplace=True)

    return top_variations

def summary_metrics(df, currency_code):

    df = df[df['currency_code'] == currency_code ]

    average_pct = df["pct"].mean()
    max_pct = df["pct"].max()
    min_pct = df["pct"].min()

    return average_pct, max_pct, min_pct