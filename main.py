import plotly.express as px
import plotly.graph_objects as go
import plotly.graph_objs as go
import matplotlib as plt
from plotly.offline import plot


# Created by marcuslundgren at 2020-05-08

# Class: ( Van )
# Generate Chart:
# Create a chart with plotly.
# Check that correct data gets loaded.
# Generate Graph:
# Create a graph with plotly.
# Check that correct data gets loaded.
# Generate Report:
# Use pd.mean() func to get average sunshine.
#

class Generate:
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


gen = Generate()
gen.generate_chart("2019", "15")

# data_karlskrona = px.data.gapminder().query("country == 'Canada'")
# fig = px.bar(data_karlskrona, x='Month', y='Days')
# fig.write_html('first_figure.html', auto_open=True)


# def generate_graph(self):
#     pass
# def generate_report(self):
#     pass


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


