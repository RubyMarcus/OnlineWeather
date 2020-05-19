import plotly.express as px
import plotly.graph_objects as go
import plotly.graph_objs as go
import matplotlib as plt
from plotly.offline import plot
from data import data
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


class Generate:
    def __init__(self):
        self.weather_data = data(65090)

    def generate_chart(self, year, days):
        year_lst = [2016, 2018]
        days_lst = [10, 5]
        year_lst.append(year)
        days_lst.append(days)
        fig = go.Figure([go.Bar(x=year_lst, y=days_lst)])

        fig.update_layout(
            title="Plot Title",
            xaxis_title="x Axis Title",
            yaxis_title="y Axis Title",
            font=dict(
                family="Courier New, monospace",
                size=18,
                color="#7f7f7f"
            )
            # plot = plot( dict(data=fig, layout=go.Layout(xaxis = {"type": "category"} )))
        )

        # fig.show()
        fig.write_html('first_figure.html', auto_open=True)



    def generate_graph(self,period, condition):

        data = self.weather_data.get_data(condition, period)



        data.plot(x='date')
        set(0,'defaultTextFontName','Courier')

        plt.show()

    def generate_report(self, period, condition):
        value,title = condition
        
        data = self.weather_data.get_data(value, period)
        print(period, "are" ,title , " approximately ",  data['value'].mean())