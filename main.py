import numpy as np
import pandas as pd
import datetime
import os
import random
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go


from data_reader import df_big_mac, df_market, df_country, df_market_mapping, pct_change, metrics, top_variation_value, summary_metrics, big_mac_exchange_rate
from visuals import add_trace_big_mac, add_trace_exchange, geo_scatter, plot_big_mac, plot_exchange, update_layout, map_country, world_map


st.title('Inflation detective :sleuth_or_spy:')

# map_options = ["Inflation Hotspots","Volume BTC traded"]
# map_selection = st.sidebar.checkbox("World maps", value=False)

### Selection of countries for line plot of exchange rate:

country_selection = st.sidebar.multiselect('Country of interest', 
            options= df_market_mapping.country.sort_values().unique())

bitcoin_market = st.sidebar.multiselect('Trading of currencies for Bitcoins', options=["Global trade"])

### Columns for layout:

# column_1, column_2, column_3 = st.columns(3)
column_1, column_2 = st.columns(2)


### Global map Volume BTC

if bitcoin_market == ["Global trade"]:
    
    try:
        st.info("Tracking volume of BTC traded globally")

        world_map_volume_btc = df_market_mapping[["country","volume_btc"]]
        st.write(geo_scatter(world_map_volume_btc))

        ## Biggest traders by country:
        top_variation_volume = top_variation_value(50, "volume_btc")

        st.info("Countries moving highest volume on a day:")
        st.table(top_variation_volume)

    except:
        print('Error ploting Volume BTC map')

# World map exchange rate:
if len(country_selection) == 0 and bitcoin_market == []:

    
    world_map_inflation = world_map(df_market_mapping[["country","currency_code", "pct"]])
    
    st.info("Percentual variation on exchange rate by country")
    st.write(world_map_inflation)

    st.info("Countries with highest variation on exchange rate:")
    top_variation_pct = top_variation_value(10, "pct")
    st.table(top_variation_pct)

try:
    
    for index, country in enumerate(country_selection):
        currency_code = map_country(df_country, country)
        last_exchange_rate, pct_delta, metric_volume_btc = metrics(df_market, currency_code )

        if index == 0:

           
            with column_1:

                st.metric("Implicit Exchange rate",
                    f"{last_exchange_rate}"+' ' + currency_code+"/USD",
                    delta = pct_delta,
                    delta_color= "off" )

                dollar_big_mac, date = big_mac_exchange_rate(country)

                st.metric(f"Dollar Big Mac *{date}*", dollar_big_mac)


            with column_2:

                st.metric("BTC traded today", metric_volume_btc)
                
                
            
            graph_exchange = plot_exchange(df_market, currency_code )
            graph_big_mac = plot_big_mac(df_big_mac,"dollar_price", country)
            graph_big_mac_ex = plot_big_mac(df_big_mac,"dollar_ex", country)


        else:

            add_trace_exchange(df_market,currency_code, graph_exchange )
            add_trace_big_mac(df_big_mac,"dollar_price", country, graph_big_mac)
            add_trace_big_mac(df_big_mac,"dollar_ex", country, graph_big_mac_ex)



    # Update layout
    update_layout(graph_big_mac,
            "USD to buy a Big Mac", "time",
            "USD Price","Country")

    update_layout(graph_exchange,
            "Implicit exhange rate", "time",
            "% Variation", "Currency code")

    ### Implicit exchange rate & Big Mac index:
    
    st.write(graph_exchange)

    ### Complementary metrics:

    average, max, min = summary_metrics(df_market, currency_code)
    
    if average > 0:
        st.error(f" The {currency_code} has been devalued in average by {round(average,2)}%")
    else:
        st.info(f"{currency_code} has been appreciated by {abs(round(average,2))}% relative to the USD")
    
    st.write(graph_big_mac)
    st.write(graph_big_mac_ex)

except:
    print('Waiting for country selection')
