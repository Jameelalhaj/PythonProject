import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from PIL import Image

import matplotlib.pyplot as plt
import json
import matplotlib.dates as mdates

header = st.container()
crisis_indicator = st.container()
dataset = st.container()


@st.cache
def get_data(filename):
    stock_data = pd.read_csv(filename, sep=',')
    return stock_data


image = Image.open('resources/Three Buttons.png')
st.sidebar.image(image, width=300, output_format='PNG')


with header:
    st.title('Welcome to the Amman Stock Exchange Free Float 2021 indexes')
    st.text('The Objective of this project is to analyse the monthly development of Amman Stock Exchange indexes')
    st.text('According to the Following')
    st.text('')


with crisis_indicator:
    # st.header("1. Let's analyze the amman stock exchange indexes")

    st.text('')

    # cp = pd.read_csv('data/crisis_probability.txt', sep=" ", header=None)
    # x = cp.values[0]
    # if x == 1:
    #     st.success(
    #         'The probability of a severe econonomic crisis within the next six months is minimal')
    # else:
    #     st.error(
    #         '! The probability of a severe econonomic crisis within the next six months is substantial !')

    # st.text('')


with dataset:
    st.header("1. Let's analyze the amman stock exchange indexes")
    st.text('')

    sel_col, disp_col = st.columns(2)
    region = sel_col.selectbox('Which region do you want to analyze?', options=[
                               'General Index', 'Financials', 'Services', 'Industries'], index=0)
    quartile = None
    if region == 'Financials':
        quartile = sel_col.selectbox('Which sector do you want to analyze?', options=[
            'None', 'Banks',
            'Financial Services', 'Real Estate', 'Insurance', 'All'], index=0)

    st.text('')
    st.text('')

    loading_text = st.text('Loading...')

    stock_data = pd.read_excel(
        'data/Index_2021_41.xlsx')

    json_data = stock_data.to_json(orient='records')

    json_data = json.loads(json_data)

    json_data = json_data[2:]

    for i in range(len(json_data)):
        json_data[i] = {k: v for k, v in json_data[i].items() if v != None}
        json_data[i] = {k: v for k, v in json_data[i].items() if v != ''}

    for i in range(len(json_data)):
        json_data[i] = {v: k for k, v in json_data[i].items()}

    new_data = []

    for j in range(len(json_data)):
        if j == 0:
            continue
        Object = json_data[j]

        ObjectValues = {}
        for k in Object:
            for i in json_data[0]:
                key = i
                value = json_data[0][i]

                if Object[k] == value:
                    ObjectValues[key] = k
        new_data.append(ObjectValues)

    DataFrame = pd.DataFrame(
        new_data, columns=['Date', 'General Index',
                           'Financials',
                           'Services',
                           'Industries', 'Banks', 'Financial Services', 'Real Estate', 'Insurance'])

    DataFrame['Date'] = pd.to_datetime(
        DataFrame['Date'], dayfirst=True)

    plt.xlabel('Dates')

    plt.gca().xaxis.set_major_formatter(
        mdates.DateFormatter('%Y-%m'))

    plt.gca().xaxis.set_major_locator(
        mdates.DayLocator(interval=31))

    plt.rcParams['font.size'] = 30

    plt.rcParams['savefig.facecolor'] = 'white'

    if region == 'General Index':

        DataFrame.plot(x='Date', y=[
            'General Index',
        ],
            figsize=(40, 20),
            grid=True,
            title='Index',
            fontsize=35,
            x_compat=True
        )

    if region == 'Services':

        DataFrame.plot(x='Date', y=[
            'Services',
        ],
            figsize=(40, 20),
            grid=True,
            title='Index',
            fontsize=35,
            x_compat=True
        )
    if region == 'Industries':

        DataFrame.plot(x='Date', y=[
            'Industries',
        ],
            figsize=(40, 20),
            grid=True,
            title='Index',
            fontsize=35,
            x_compat=True
        )

    if region == 'Financials':
        if quartile == 'Banks':
            DataFrame.plot(x='Date', y=[
                'Financials',
                'Banks'
            ],
                figsize=(40, 20),
                grid=True,
                title='Index',
                fontsize=35,
                x_compat=True
            )
        elif quartile == 'Financial Services':
            DataFrame.plot(x='Date', y=[
                'Financials',
                'Financial Services'
            ],
                figsize=(40, 20),
                grid=True,
                title='Index',
                fontsize=35,
                x_compat=True
            )
        elif quartile == 'Real Estate':
            DataFrame.plot(x='Date', y=[
                'Financials',
                'Real Estate'
            ],
                figsize=(40, 20),
                grid=True,
                title='Index',
                fontsize=35,
                x_compat=True
            )
        elif quartile == 'All':
            DataFrame.plot(x='Date', y=[
                'Financials',
                'Banks',
                'Financial Services',
                'Real Estate',
                'Insurance'
            ],
                figsize=(40, 20),
                grid=True,
                title='Index',
                fontsize=35,
                x_compat=True
            )
        elif quartile == 'Insurance':
            DataFrame.plot(x='Date', y=[
                'Financials',
                'Insurance'
            ],
                figsize=(40, 20),
                grid=True,
                title='Index',
                fontsize=35,
                x_compat=True
            )
        elif quartile == 'Insurance':
            DataFrame.plot(x='Date', y=[
                'Financials',
                'Insurance'
            ],
                figsize=(40, 20),
                grid=True,
                title='Index',
                fontsize=35,
                x_compat=True
            )
        else:
            DataFrame.plot(x='Date', y=[
                'Financials',
            ],
                figsize=(40, 20),
                grid=True,
                title='Index',
                fontsize=35,
                x_compat=True
            )

    st.pyplot(
        fig=plt.gcf(),
    )
    loading_text.text('')
