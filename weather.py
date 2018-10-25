import requests

class Weather:
    def __init__(self, city, key):
        self.city = city
        self.key = key
        self.url = "http://api.openweathermap.org/data/2.5/weather?q={place}&APPID={ID}".format(place=self.city,ID=self.key)
        self.weather_info = requests.get(self.url).json()
        self.current = self.ktof(self.weather_info['main']['temp'])
        self.high = self.ktof(self.weather_info['main']['temp_max'])
        self.low = self.ktof(self.weather_info['main']['temp_min'])
        self.condition = self.weather_info['weather'][0]['description']

    def ktof(self, k):
        return int(((9/5)*(k-273))+32)
