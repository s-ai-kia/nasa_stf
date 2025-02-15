# -*- coding: utf-8 -*-
"""SUOMI_VIIRS_C2_Global_7d.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cqyiyklyiMLmPl_IJBsryJdYPtWhbQo8

Author @ Amartya | Nasa International Space App Challenge 2020
"""

import plotly.graph_objects as go

import pandas as pd

df = pd.read_csv('./SUOMI_VIIRS_C2_Global_7d.csv')

df

df['text'] = 'Date and Time:' + df['acq_date'].astype(str) + ':' + df['acq_time'].astype(str) + ', ' + df['satellite'].astype(str) + ', ' + df['daynight'].astype(str)

df['text']

fig = go.Figure(data=go.Scattergeo(
        locationmode = 'USA-states',
        lon = df['longitude'],
        lat = df['latitude'],
        text = df['text'],
        mode = 'markers',
        marker = dict(
            size = 8,
            opacity = 0.8,
            reversescale = True,
            autocolorscale = False,
            symbol = 'square',
            line = dict(
                width=1,
                color='rgba(102, 102, 102)'
            ),
            colorscale = 'Blues',
            cmin = 0,
            color = df['bright_ti4'],
            cmax = df['bright_ti4'].max(),
            colorbar_title="Incoming flights<br>February 2011"
        )))

fig.update_layout(
        title = 'Most trafficked US airports<br>(Hover for airport names)',
        geo = dict(
            scope='usa',
            projection_type='albers usa',
            showland = True,
            landcolor = "rgb(250, 250, 250)",
            subunitcolor = "rgb(217, 217, 217)",
            countrycolor = "rgb(217, 217, 217)",
            countrywidth = 0.5,
            subunitwidth = 0.5
        ),
    )

fig.show()