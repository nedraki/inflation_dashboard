import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
# from streamlit.secrets import Secrets

## Country selection:
def plot_big_mac(df, values_y, country_selected):

    """Plot for Bic Mac Index price vs time

        values: 'dollar_price' or 'dollar_ex'"""

    #[docs plot](https://plotly.com/python/plotly-express/) 

    if country_selected in df.values:

        df_by_country = df[df['country'] == f'{country_selected}']
        df = df_by_country
        values = df[f'{values_y}']

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df.date, y=values,
                mode='lines+markers',
                name=country_selected))

        return fig

    else:

        return "Country not available in Big Mac Data Base"

def add_trace_big_mac(df,values_y,country_selected, fig):

    if country_selected in df.values:

        df_by_country = df[df['country'] == f'{country_selected}']
        df = df_by_country
        values = df[f'{values_y}']


        fig.add_trace(go.Scatter(x=df.date, y=values,
                mode='lines+markers',
                name=country_selected))

        return fig

    else:

        return None


def plot_exchange(df, currency_code):

    """ Calculates % variation of implicit exchange rate
    for a given fiat currency
    df: CurrenciesDataBase.db
    """
    
    df_plot = df[df['currency_code'] == currency_code ]
    df_plot.sort_values(by = 'date', inplace = True)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df_plot.date, y=df_plot.pct,
                    mode='lines+markers',
                    name=currency_code))
    
    return fig

def map_country(df, country):
    # Mapping country with currency code
    return df[df.country == country].currency_code.values[0]

def add_trace_exchange(df, currency_code, fig):

    df_plot = df[df['currency_code'] == currency_code ]
    df_plot.sort_values(by = 'date', inplace = True)


    fig.add_trace(go.Scatter(x=df_plot.date, y=df_plot.pct,
                    mode='lines+markers',
                    name=currency_code))
    return fig


def update_layout(fig, title, x_axis, y_axis, legend):
    try:
        fig.update_layout(
        title=title,
        xaxis_title=x_axis,
        yaxis_title=y_axis,
        legend_title=legend)
    except:
        "fig object does not exist"

@st.cache()
def geo_scatter(df):

    df = df[["country","volume_btc"]]

    fig = px.scatter_geo(df, locations="country", 
                     locationmode= "country names", 
                     size = "volume_btc",
                     color= "volume_btc",
                     projection="natural earth",
                     #animation_frame= df['date'].dt.isocalendar().week,
                     title= "Volume BTC")

    return fig

@st.cache()
def world_map(df, average = False):

    if average == False:
        df = df.loc[df.pct > 0]
    else:
        df = df.groupby(["country","currency_code"]).mean().reset_index()
        df = df.loc[df.pct > 0]

    
    fig = px.scatter_geo(df, locations="country", 
                        locationmode= "country names", 
                        size = "pct",
                        color= "pct",
                        projection="natural earth",
                        title = "% Variation of foreign exchange rate"
    #                      animation_frame= df['date'].dt.isocalendar().week
                        )

    return fig

