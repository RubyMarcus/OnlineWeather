from data import *
import matplotlib.pyplot as plt


class Generate:
    def __init__(self):
        self.weather_data = data(65090)

    def generate_graph(self, period, condition):
        value, title = condition
        data_ = self.weather_data.get_data(value, period)

        data_.plot(x='date', y='value', title=title)

        plt.show()

    def generate_chart(self, period, condition):
        value, title = condition
        data_ = self.weather_data.get_data(value, period)

        data_.plot(x='date', y='value', title=title, kind='bar')

        plt.show()

    def generate_report(self):
        pass

# 1 lufttemperatur
# 6 daggpunktstemperatur
# 8


# gen.generate_chart("2019", "15")

# data_karlskrona = px.data.gapminder().query("country == 'Canada'")
# fig = px.bar(data_karlskrona, x='Month', y='Days')
# fig.write_html('first_figure.html', auto_open=True)


# gen = Generate()
# gen.generate_chart()


# import plotly.graph_objects as go
# fig = go.Figure(data=go.Bar(y=[2, 3, 1]))
# fig.write_html('first_figure.html', auto_open=True)


# import plotly.express as px
# df = px.data.tips()
# fig = px.histogram(df, x="sex", y="tip", histfunc="avg", color="smoker", barmode="group",
#              facet_row="time", facet_col="day", category_orders={"day": ["Thur", "Fri", "Sat", "Sun"],
#                                                                 "time": ["Lunch", "Dinner"]})
# fig.write_html('first_figure.html', auto_open=True)


# import chart_studio
# import chart_studio.plotly as py
# import chart_studio.tools as tls
# import plotly.graph_objects as go
# from chart_studio.grid_objs import Column, Grid

# from datetime import datetime as dt
# import numpy as np
# from IPython.display import IFrame


# meta = {
#     "Month": "November",
#     "Experiment ID": "d3kbd",
#     "Operator": "James Murphy",
#     "Initial Conditions": {
#           "Voltage": 5.5
#     }
# }

# grid_url = py.grid_ops.upload(grid, filename='grid_with_metadata_'+str(dt.now()), meta=meta)
# print(grid_url)
