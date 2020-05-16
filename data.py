import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# karlskrona station id 65090


class data:

    def __init__(self, station):
        self.response = None
        self.station = station
        self.data = None

    def get_data(self, parameter, period):
        url = "https://opendata-download-metobs.smhi.se/api/version/1.0/parameter/" \
              "{parameter}/station/65090/period/{period}/data.json".format(parameter=parameter, period=period)

        try:
            self.response = requests.get(url, timeout=2)

            print(self.response.content)

            return self.prepare_data()
        except requests.exceptions.RequestException:
            raise Exception('Connection failed.') from None

    def prepare_data(self):
        self.data = self.response.json()['value']

        df = pd.DataFrame.from_dict(self.data)

        df['date'] = pd.to_datetime(df['date'], unit='ms')

        return df


weather_data = data(65090)

# 1 lufttemperatur
# 6 daggpunktstemperatur
# 8

data = weather_data.get_data(1, 'latest-day')

print(data)

data['value'] = data['value'].astype(float)

data.plot(x='date', y='value')

plt.show()

