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

    def generate_chart(self):
        ...

    def generate_graph(self, period, condition):

        data = self.weather_data.get_data(condition, period)

        data.plot(x='date')
        plt.show()

    def generate_report(self, period, condition):
        value,title = condition
        
        data = self.weather_data.get_data(value, period)
        print(period, "are" ,title , " approximately ",  data['value'].mean())