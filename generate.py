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
