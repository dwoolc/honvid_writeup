import plotly
import plotly.graph_objects as go
import pandas as pd
from plotly.subplots import make_subplots
import cv2
import numpy as np
import glob
import dataframe_amend

import plotly.express as px

recordings = ['call_id_1',
              'call_id_2',
              'call_id_3',
              'call_id_4']

for j in recordings:
    recording_info = pd.read_csv('dir_expanded_df.csv')

    fps = 15

    header_col = 'white'

    ids = ["dial", "hold", "human", "message_hold", "message_init"]
    marker_color = ['#e4874b', '#cd60d6', '#18e5e7', '#0281f7', '#97c268']
    markers_correct = dict(zip(ids, marker_color))
    tp, tn, fp, fn= 0, 0, 0, 0
    ###WORKING CODE FOR RADIAL AREA PLOT###
    for index, row in recording_info.iterrows():
        r = [row['dial'],
             row['hold'],
             row['human'],
             row['message_hold'],
             row['message_init']]

        this, not_this = divmod(index, fps)
        floor_index = this * fps
        rounding = recording_info.iloc[floor_index]
        rounded_values = [
            rounding['dial'],
             rounding['hold'],
              rounding[ 'human'],
               rounding['message_hold'],
                rounding['message_init']]

        rounded = ["{:.3f}".format(x) for x in rounded_values]
        print(rounded)

        # """Create a canvas with three subplots for predicted bar, labelled bar & polar area for prediction"""
        fig = make_subplots(rows=4, cols=2, vertical_spacing=0.1,horizontal_spacing=0, specs=[
            [{'type': 'polar', 'rowspan': 4}, {'type': 'table', 'rowspan':2}],
            [{}, {'type':'table'}],
            [{}, {}],
            [{}, {}]],
                            row_heights=[11, 8, 1, 1],
                            column_width=[16, 9],
                            subplot_titles=["<b>Current Prediction</b>",
                                            "<b>Prediction Values</b>",  "", "", "",
                                            "<b>Prediction Tracker</b>", "",
                                            "<b>True Label Tracker</b>"])
        if row['pred'] == row ['t_lab']:
            marker_line_color = ["#00b159" if x == row['pred'] else "white" for x in ids]
        else: marker_line_color = ["#d11141" if x == row['pred'] else "white" for x in ids]

        # """Add the polar area chart to the canvas"""

        fig.add_trace(go.Barpolar(
            r= [i + 0.2 for i in r],
            offset=0,
            name='Current Prediction',
            theta=[76 + 72 * x for x in range(5)],
            width=[60],
            marker_color=marker_color,
            selectedpoints='',
            hovertext=[i for i in zip(ids, r)],
            text=["Dial tone", "Hold music", "Human", "Message During Hold", "Initial Recorded Message"],
            marker_line_color=marker_line_color,
            marker_line_width=[3 if x == row['pred'] else 0 for x in ids],
            opacity=1,
            showlegend=True
        ), row=1, col=1)
        options = ["<b>Dial Tone</b>", "<b>Hold</b>", "<b>Human</b>", "<b>Message During Hold</b>", "<b>Initial Recorded Message</b>"]
        #Add the table showing the probabilities assigned to each classification
        fig.add_trace(go.Table(
            columnwidth=[15, 30],
            header=dict(
                values=['<b>Probability</b>', '<b>Classification</b>'],
                line_color='black',
                fill_color=["black"],
                align=['center', 'left'], font=dict(color='white', size=20)
            ),
            cells=dict(
                values=[rounded, options],
                line_color='black',
                fill_color=["black", "black"],
                height=30,
                align=['center', 'left'], font=dict(color='white', size=18)
            )), row=1, col=2)

        #Create the stacked horizontal bars
        for i in range(0, index):
            fig.add_trace(go.Bar(
                x=[1],
                y=[1],
                orientation='h',
                marker=dict(
                    color=markers_correct[recording_info.loc[i]['pred']],
                    line=dict(color='rgb(248, 248, 249)', width=0)
                )
            ), row=3, col=2)

            fig.add_trace(go.Bar(
                x=[1],
                y=[2],
                orientation='h',
                marker=dict(
                    color=markers_correct[recording_info.loc[i]['t_lab']],
                    line=dict(color='rgb(248, 248, 249)', width=0)
                )
            ), row=4, col=2)

        fig.update_xaxes(range=[0, len(recording_info)], )
        fig.update_layout(
            xaxis3=dict(
                showgrid=False,
                showline=False,
                showticklabels=False,
                zeroline=False
            ),
            yaxis3=dict(
                showgrid=False,
                showline=False,
                showticklabels=False,
                zeroline=False
            ),
            xaxis5=dict(
                showgrid=False,
                showline=False,
                showticklabels=False,
                zeroline=False
            ),
            yaxis5=dict(
                showgrid=False,
                showline=False,
                showticklabels=False,
                zeroline=False
            ),
            barmode='stack',
            paper_bgcolor='rgb(0, 0, 0)',
            plot_bgcolor='rgb(0, 0, 0)',
            showlegend=False,

            polar=dict(
                radialaxis=dict(range=[0, 1.2], showticklabels=False, ticks='',color='white', linewidth=0),
                angularaxis=dict(showticklabels=False, ticks='', tickmode='array', tickvals=[0, 72, 144, 216, 288], color='white', rotation=90),
            ),
            template=None,

        )

        fig.update_layout(
            font_family="Rockwell",
            font_color="white",
            title_font_family="Rockwell",
            title_font_color="white",
        )
        for i in fig['layout']['annotations']:
            i['font'] = dict(size=30)

        fig.update_polars(bgcolor='black')


        fig.add_annotation(dict(font=dict(color="white", size=20),
                                x=0.55,
                                y=0.38,
                                showarrow=False,
                                text="Human",
                                xref="paper",
                                yref="paper"))

        fig.add_annotation(dict(font=dict(color="white", size=20),
                                x=0.3,
                                y=-0.05,
                                showarrow=False,
                                text="Hold",
                                xref="paper",
                                yref="paper"))

        fig.add_annotation(dict(font=dict(color="white", size=20),
                                x=0.55,
                                y=.9,
                                showarrow=False,
                                text="Message During Hold",
                                xref="paper",
                                yref="paper"))

        fig.add_annotation(dict(font=dict(color="white", size=20),
                                x=0.0,
                                y=0.9,
                                showarrow=False,
                                text="Initial Recorded Message",
                                xref="paper",
                                yref="paper"))

        fig.add_annotation(dict(font=dict(color="white", size=20),
                                x=0.05,
                                y=0.38,
                                showarrow=False,
                                text="Dial Tone",
                                xref="paper",
                                yref="paper"))

        index = f'{index:04}'
        width = 1600
        height = 900
        fig.show()
        fig.write_image("dir"+j+"/video" + index + ".png",
                         width=width, height=height)

