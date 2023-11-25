"""
TODO
Создать таблицу Excel и заполнить ее информацией о погоде в 12 столицах (температура, влажность, осадки)
['Moscow','Tokyo','Tbilisi','Yerevan','Washington','Beijing','Canberra','Kyiv','İstanbul','Jerusalem','Paris','Berlin']

"""

import requests
import json


def get_weather(api_key, city):
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"

    response = requests.get(base_url)

    if response.status_code == 200:
        data = response.json()
        with open("weather.json", "w", encoding="UTF-8") as file_out:
            json.dump(data, file_out, ensure_ascii=False, indent=2)
    else:
        print("Error in the HTTP request")


api_key = "9156c-_____c96917e1e_________4"
city = "Moscow"

get_weather(api_key, city)
