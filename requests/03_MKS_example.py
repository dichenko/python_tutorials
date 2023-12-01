"""for i in range(10):
    response = requests.get(api_url)
    if response.status_code == 200:
        d = json.loads(response.text)

        print(d['iss_position']["longitude"],d['iss_position']["latitude"], f"https://yandex.ru/maps/?ll={d['iss_position']['longitude']}%2C{d['iss_position']['latitude']}&z=4")

    else:
        print("ERROR")
    time.sleep(3)


    def haversine(lat1, lon1, lat2, lon2):
    # Число Радиус Земли в километрах
    R = 6371.0

    #переводим координаты в радианы
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    #вычисляем разницу координат
    dlon = lon2 - lon1
    dlat = lat2 - lat1

    #формула гаверсинусов
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    #находим расстояние
    distance = R * c
    return distance


"""