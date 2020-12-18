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


with open("atlas.pickle", 'rb') as f:
    df_ward_atlas = pickle.load(f)

nutrients = ['energy_protein', 'energy_carb', 'energy_fibre', 'energy_fat', 'energy_alcohol',
             'h_nutrients_calories_norm']
label_nutrients = ['Energy Protein', 'Energy Carbs', 'Energy Fibre', 'Energy Fat', 'Energy Alcohol',
                   'Entropy Nutrients Calories']


def hist_no_log():
    # # https://plotly.com/python/subplots/#setting-subplots-on-a-figure-directly
    # fig = go.Figure()
    # trace = go.Histogram2d(y=df_ward_atlas['Aged 0-15'], x=df_ward_atlas['energy_carb'], opacity=0.6, marker_color='blue')
    # fig.add_traces(trace)
    # # buttons for atlas
    # buttons_atlas = []
    # for column in df_atlas.columns.values[2:]:
    #     # buttons_atlas.append(dict(method='update',
    #     #                           label=column,
    #     #                           visible=True,
    #     #                           args=[{'y': [df_ward_atlas[column].values]}],
    #     #                           )
    #     #                      )
    #     buttons_atlas.append(dict(method='update',
    #                               label=column,
    #                               visible=True,
    #                               args=[{'y': [df_ward_atlas[column].values]}],
    #                               )
    #                          )
    # # button for wards
    # buttons_wards = []
    # for column in nutrients:
    #     # buttons_wards.append(dict(method='update',
    #     #                           label=column,
    #     #                           visible=True,
    #     #                           args=[{'y': [df_ward_atlas[column].values], 'x': [df_ward_atlas[column].values]}],
    #     #                           )
    #     #                      )
    #     buttons_atlas.append(dict(method='update',
    #                               label=column,
    #                               visible=True,
    #                               args=[{'y': [df_ward_atlas[column].values]}],
    #                               )
    #                          )
    # # List for menus
    # updatemenu = []
    # # add dict for buttons
    # atlas_menu = dict()
    # updatemenu.append(atlas_menu)
    # ward_menu = dict()
    # updatemenu.append(ward_menu)
    # # Fill dict
    # updatemenu[0]['buttons'] = buttons_atlas
    # updatemenu[0]['x'] = 0.15  # Some styling
    # updatemenu[0]['y'] = 1.12  # Some styling
    # updatemenu[1]['buttons'] = buttons_wards
    # updatemenu[1]['x'] = 0.33  # Some styling
    # updatemenu[1]['y'] = 1.12  # Some styling
    # # add dropdown menus to the figure
    # fig.update_layout(showlegend=True, updatemenus=updatemenu)
    # # construct menus
    # # updatemenus = [{'buttons': buttons_atlas,
    # #                 'direction': 'down',
    # #                 'showactive': True, },
    # #                {'buttons': buttons_ward,
    # #                 'direction': 'down',
    # #                 'showactive': True, }
    # #                ]
    # #
    # # # update layout with buttons, and show the figure
    # # fig.update_layout(
    # #     updatemenus=updatemenus,
    # #     title_text='Histograms of Demographics',  # title of plot
    # #     xaxis_title_text='Count',
    # #     yaxis_title_text='Value',
    # #     bargap=0.2,
    # #     bargroupgap=0.1
    # # )
    # fig.show()
    # # to = py.plot(fig, filename="demograph_hist", auto_open=True)
    # # print(to)
    import plotly.express as px

    # fig = px.scatter(df_ward_atlas, x='Aged 0-15', y='energy_carb')#, marginal_x="histogram", marginal_y="histogram")
    fig = go.Figure()
    trace = go.Scatter(y=df_ward_atlas['Aged 0-15'], x=df_ward_atlas['energy_protein'], mode='markers')
    fig.add_traces(trace)
    # buttons for atlas
    buttons_atlas = []
    for column in df_atlas.columns.values[2:]:
        buttons_atlas.append(dict(method='update',
                                  label=column,
                                  visible=True,
                                  args=[{'x': df_ward_atlas[column]}],
                                  )
                             )
    # button for wards
    buttons_wards = []
    for column in nutrients:
        buttons_wards.append(dict(method='update',
                                  label=column,
                                  visible=True,
                                  args=[{'y': df_ward_atlas[column]}],
                                  )
                             )
    # # List for menus
    updatemenu = []

    # add dict for buttons
    atlas_menu = dict()
    updatemenu.append(atlas_menu)
    ward_menu = dict()
    updatemenu.append(ward_menu)

    # Fill dict
    updatemenu[0]['buttons'] = buttons_atlas
    updatemenu[0]['x'] = 0.15  # Some styling
    updatemenu[0]['y'] = 1.12  # Some styling

    updatemenu[1]['buttons'] = buttons_wards
    updatemenu[1]['x'] = 0.33  # Some styling
    updatemenu[1]['y'] = 1.12  # Some styling

    # add dropdown menus to the figure
    fig.update_layout(showlegend=True, updatemenus=updatemenu)

    # construct menus
    # updatemenus = [{'buttons': buttons_atlas,
    #                 'direction': 'down',
    #                 'showactive': True, },
    #                {'buttons': buttons_ward,
    #                 'direction': 'down',
    #                 'showactive': True, }
    #                ]
    #
    # # update layout with buttons, and show the figure
    # fig.update_layout(
    #     updatemenus=updatemenus,
    #     title_text='Histograms of Demographics',  # title of plot
    #     xaxis_title_text='Count',
    #     yaxis_title_text='Value',
    #     bargap=0.2,
    #     bargroupgap=0.1
    # )
    fig.show()
    # to = py.plot(fig, filename="demograph_hist", auto_open=True)
    # print(to)


def hist():
    # creating plot
    fig = px.density_contour(x=df_ward_atlas["energy_carb"], y=df_ward_atlas["Aged 0-15"])
    fig.update_traces(contours_coloring="fill", contours_showlabels=True)
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
    for column in df_atlas.columns.values[2:]:
        buttons_atlas.append(dict(method='update',
                                  label=column,
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
    # updatemenu[0]['buttons'] = buttons_atlas
    # updatemenu[0]['x'] = 0.15  # Some styling
    # updatemenu[0]['y'] = 1.12  # Some styling
    # updatemenu[1]['buttons'] = buttons_wards
    # updatemenu[1]['x'] = 0.33  # Some styling
    # updatemenu[1]['y'] = 1.12  # Some styling
    updatemenus = [{'buttons': buttons_atlas,
                    'direction': 'down',
                    'showactive': True,
                    'x': 0.5,
                    'y': 1.05, },
                   {'buttons': buttons_wards,
                    'direction': 'down',
                    'showactive': True,
                    'x': 0.5,
                    'y': 1.05
                    }
                   ]
    fig.update_layout(

        template="simple_white",
        updatemenus=updatemenus,
        title_text='Contour Plot Demographics vs. Nutrients',  # title of plot
        xaxis_title_text='Average Nutrient Energy Content [kcal]',
        yaxis_title_text='Demographic',
        title_x=0.5,
        title_y=1
    )
    # fig.show()
    to = py.plot(fig, filename="demograph_vs_atlas", auto_open=False)  # use auto_open=False for plot to be able to be embedded
    # print(to)


def corrs_heatmap():
    # https://plotly.com/python/subplots/#setting-subplots-on-a-figure-directly
    from plotly.subplots import make_subplots
    fig = make_subplots(1, 2, horizontal_spacing=0.1)
    corrs = go.Heatmap(z=corr_selected)
    corrs_p = go.Heatmap(z=corr_p_selected)
    fig.add_trace(corrs, row=1, col=1)
    fig.add_trace(corrs_p, row=1, col=2)

    # update layout with buttons, and show the figure
    fig.update_layout(
        title_text='Histograms of Demographics',  # title of plot
        xaxis_title_text='Count',
        yaxis_title_text='Value',
        bargap=0.2,
        bargroupgap=0.1
    )
    fig.show()
    # to = py.plot(fig, filename="demograph_hist", auto_open=True)
    # print(to)


if __name__ == "__main__":
    # corrs_heatmap()
    hist()
