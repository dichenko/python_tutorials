import requests
import json
import time
api_url = 'http://api.open-notify.org/iss-now.json'

for i in range(10):
    response = requests.get(api_url)
    if response.status_code == 200:
        d = json.loads(response.text)

        print(d['iss_position']["longitude"],d['iss_position']["latitude"], f"https://yandex.ru/maps/?ll={d['iss_position']['longitude']}%2C{d['iss_position']['latitude']}&z=4")

    else:
        print("ERROR")
    time.sleep(3)