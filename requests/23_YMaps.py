from requests import get, ConnectionError

params = {"pt": "37.677751,55.757718"}
try:
    response = get("https://static-maps.yandex.ru/1.x?l=28.98624,41.043451&pt=28.98624,41.043451")
except ConnectionError:
    print("Проверьте подключение к сети.")
else:
    print(response.text)
    with open("map.png", "wb") as file:
        file.write(response.content)