# imports
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import pandas as pd
import chart_studio
import chart_studio.plotly as py
import chart_studio.tools as tls
import plotly.express as px

user = 'aglavac'
api_key = 'lpP9z6IX6CU3tX81DJD2'
chart_studio.tools.set_credentials_file(username=user, api_key=api_key)

import pickle
from os.path import join

with open("ward_atlas.pickle", 'rb') as f:
    df_ward_atlas = pickle.load(f)
with open("atlas.pickle", 'rb') as f:
    df_atlas = pickle.load(f)

nutrients = ['energy_protein', 'energy_carb', 'energy_fibre', 'energy_fat', 'energy_alcohol',
             'h_nutrients_calories_norm']
label_nutrients = ['Energy Protein', 'Energy Carbs', 'Energy Fibre', 'Energy Fat', 'Energy Alcohol',
                   'Entropy Nutrients Calories']
labels_demographics = [
    "Aged 0-15 [%]",
    "Aged 16-64 [%]",
    "Aged 65+ [%]",
    "White [%]",
    "Mixed [%]",
    "Asian or Asian British [%]",
    "Black or Black British [%]",
    "Other [%]",
    "Christian [%]",
    "Buddhist [%]",
    "Hindu [%]",
    "Jewish [%]",
    "Muslim [%]",
    "Sikh  [%]",
    "Other religions [%]",
    "No religion [%]",
    "Religion not stated [%]",
    "Born in UK [%]",
    "Not Born in UK [%]",
    "Household Income Mean [£]",
    "Household Income Median [£]",
    'No qualifications [%]',
    'Level 1 qualifications [%]',
    'Level 2 qualifications [%]',
    'Apprenticeship qualifications [%]',
    'Level 3 qualifications [%]',
    'Level >=4 qualifications [%]',
    'Other qualifications [%]',
    'Bad Health [%]',
    'Limited activities [%]',
    "Well-Being [-]",
    "IOD AVG [-]"
]


def hist():
    # creating plot
    fig = px.density_contour(x=df_ward_atlas["energy_carb"], y=df_ward_atlas["Aged 0-15"])
    fig.update_traces(contours_coloring="fill", contours_showlabels=True, colorscale='Blues')
    fig.add_trace(go.Scatter(
        x=df_ward_atlas["energy_carb"],
        y=df_ward_atlas["Aged 0-15"],
        mode='markers',
        marker=dict(
            color='rgba(0,0,0,0.3)',
            size=7
        )
    ))
    # creating buttons
    # atlas
    buttons_atlas = []
    for idx, column in enumerate(df_atlas.columns.values[2:]):
        buttons_atlas.append(dict(method='update',
                                  label=labels_demographics[idx],
                                  visible=True,
                                  args=[{'y': [df_ward_atlas[column], df_ward_atlas[column]], }],
                                  )
                             )
    # wards
    buttons_wards = []
    for idx, column in enumerate(nutrients):
        buttons_wards.append(dict(method='update',
                                  label=label_nutrients[idx],
                                  visible=True,
                                  args=[{'x': [df_ward_atlas[column], df_ward_atlas[column]], }],
                                  )
                             )
    updatemenus = [{'buttons': buttons_atlas,
                    'direction': 'down',
                    'showactive': True,
                    'pad': {'r': 10, 't': 10},
                    'x': 0.3,
                    'xanchor': 'left',
                    'y': 1.05,
                    'yanchor': 'top', },
                   {'buttons': buttons_wards,
                    'direction': 'down',
                    'showactive': True,
                    'pad': {'r': 10, 't': 10},
                    'x': 0.0,
                    'xanchor': 'left',
                    'y': 1.05,
                    'yanchor': 'top', },
                   ]
    fig.update_layout(

        template="simple_white",
        updatemenus=updatemenus,
        title_text='Contour Plot Demographics vs. Nutrients',  # title of plot
        xaxis_title_text='Energy Content of Nutrient in Average Product [kcal]',
        yaxis_title_text='Demographic',
        title_x=0.5,
        title_y=1
    )
    # fig.show()
    # to = py.plot(fig, filename="demograph_vs_atlas", auto_open=False)  # use auto_open=False for plot to be able to be embedded
    fig.write_html("demo_vs_nutrients.html")


if __name__ == "__main__":
    hist()
