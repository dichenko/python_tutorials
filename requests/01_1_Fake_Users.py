# Сайт: https://jsonplaceholder.typicode.com/ создан специально для обучения работы с GET-запросами.
# Возвращает список из 10 случайных пользователей.
# TODO
# Сохранить в текстовый файл список из 10 пользователей, отсортировать их по фамилии
# Petrov Ivan | Moscow | +79263451881

import requests

url = 'https://jsonplaceholder.typicode.com/users'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Список пользователей:", data)

else:
    print("Ошибка при выполнении запроса. Код состояния:", response.status_code)

