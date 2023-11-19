import requests
import json

def get_weather(api_key, city):
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    response = requests.get(base_url)

    if response.status_code == 200:
        data = response.json()
        with open("weather.json", "w", encoding="UTF-8") as file_out:
            json.dump(data, file_out, ensure_ascii=False, indent=2)
    else:
        print("Error in the HTTP request")


api_key = "9156c1abecc96917e1e7291bab96b364"
city = "Moscow"

get_weather(api_key, city)