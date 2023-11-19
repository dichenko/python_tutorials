# Сервис предоставляет информацию о странах
# Напишите программу, в которой пользователь вводит название страны, а программа произносит её название на эстонском языке
# Используй gtts

import requests

url = 'https://restcountries.com/v3.1/name/Russia'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    countries = data
    for country in countries:
        print(f"Название страны: {country['name']['common']}")
        print(f"Столица: {country['capital'][0]}\n")
else:
    print("Ошибка при выполнении запроса. Код состояния:", response.status_code)


