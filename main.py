import numpy as np
import pandas as pd
import datetime
import os
import random
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

from about import message_users
from utils.visuals import Visuals
from utils.data_reader import (
    DataReader,
    df_big_mac,
    df_market,
    df_country,
    df_market_mapping,
)


st.title("Inflation detective :sleuth_or_spy:")

plot = Visuals()
read = DataReader()

### Selection of countries for line plot of exchange rate:

country_selection = st.sidebar.multiselect(
    "Country of interest", options=df_market_mapping.country.sort_values().unique()
)

bitcoin_market = st.sidebar.multiselect(
    "Trading of currencies for Bitcoins", options=["Global trade"]
)

# Sidebar message:
st.sidebar.write(
    "An effort to track real variance on the exchange rate of currencies against the USD"
)
download_data = st.sidebar.button("Download the data")
message = st.sidebar.button("About the project")

### Columns for layout:

# column_1, column_2, column_3 = st.columns(3)
column_1, column_2 = st.columns(2)


if message:
    st.markdown(message_users)
if download_data:
    st.markdown(
        "[Download link](https://github.com/nedraki/inflation_dashboard/tree/main/data)"
    )


### Global map Volume BTC

elif bitcoin_market == ["Global trade"]:

    try:
        st.info("Tracking volume of BTC traded globally")

        world_map_volume_btc = df_market_mapping[["country", "volume_btc"]]
        st.write(plot.geo_scatter(world_map_volume_btc))

        ## Biggest traders by country:
        top_variation_volume = read.top_variation_value(50, "volume_btc")

        st.info("Countries moving highest volume on a day:")
        st.table(top_variation_volume)

    except:
        print("Error ploting Volume BTC map")

# World map exchange rate:
elif len(country_selection) == 0 and bitcoin_market == []:

    world_map_inflation = plot.world_map(
        df_market_mapping[["country", "currency_code", "pct"]]
    )

    st.info("Percentual variation on exchange rate by country")
    st.write(world_map_inflation)
    st.write(
        "The variation on exchange rate allows us to identify hotspots where citizens are selling off the local currency in exchange for other currencies perceived as stronger. Events with a significant increase in the exchange rate can be an indicator of distrust of the local currency or devaluations"
    )

    st.info(
        f"Countries with highest variation on exchange rate during last {read.days_counter()} days:"
    )
    top_variation_pct = read.top_variation_value(10, "pct")
    st.table(top_variation_pct)

try:

    complementary_metrics = []

    for index, country in enumerate(country_selection):

        currency_code = plot.map_country(df_country, country)
        last_exchange_rate, pct_delta, metric_volume_btc, last_update = read.metrics(
            df_market_mapping, currency_code
        )
        dollar_big_mac, date = read.big_mac_exchange_rate(country)
        complementary_metrics.append(
            read.write_summary_metrics(df_market_mapping, currency_code)
        )
        if index == 0:

            with column_1:

                st.metric(
                    "Implicit Exchange rate",
                    f"{last_exchange_rate}" + " " + currency_code + "/USD",
                    delta=pct_delta,
                    delta_color="off",
                )
                st.metric(f"BTC traded", metric_volume_btc)

            with column_2:

                st.metric(f"Dollar Big Mac *{date}*", dollar_big_mac)
                st.metric(f"Last update", last_update)

            graph_exchange = plot.plot_exchange(df_market_mapping, currency_code)

            graph_big_mac_ex = plot.plot_big_mac(df_big_mac, "dollar_ex", country)
            graph_big_mac = plot.plot_big_mac(df_big_mac, "dollar_price", country)

        else:

            plot.add_trace_exchange(df_market_mapping, currency_code, graph_exchange)
            plot.add_trace_big_mac(df_big_mac, "dollar_ex", country, graph_big_mac_ex)
            plot.add_trace_big_mac(df_big_mac, "dollar_price", country, graph_big_mac)

    ### Update layout

    plot.update_layout(
        graph_exchange, "Implicit exhange rate", "time", "% Variation", "Currency code"
    )

    plot.update_layout(
        graph_big_mac, "USD to buy a Big Mac", "time", "USD Price", "Country"
    )

    plot.update_layout(
        graph_big_mac_ex,
        "Historical exhange rate",
        "time",
        "Exchange rate",
        "Currency code",
    )

    ### Implicit exchange rate:

    st.write(graph_exchange)

    for metric in complementary_metrics:
        if metric[1] == "devaluation":
            st.error(metric[0])
        else:
            st.info(metric[0])

    ### Big Mac visuals:
    st.write(graph_big_mac_ex)
    st.write(graph_big_mac)


except:
    print("Waiting for country selection")
