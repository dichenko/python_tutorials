"""ТЗ
Сохранить ответ в JSON и изучить его.
Сохранить в  текстовый файл текст 10 случайных шуток

Изучить API проекта и узнать, какие категории шуток бывают https://api.chucknorris.io/
Для каждой категории создать текстовый файл и сохранить туда 5 случайных шуток. Проверить, чтобы шутки не повторялись.
"""
import requests

url = 'https://api.chucknorris.io/jokes/random'
responce = requests.get(url)
print(responce.text)