"""ТЗ
Сохранить ответ в JSON и изучить его.
Сохранить в  текстовый файл текст 10 случайных шуток

Изучить API проекта и узнать, какие категории шуток бывают https://api.chucknorris.io/
Создать текстовый файл и сохранить в него по 1 шутке из каждой категории (сделать заголовок для категории)
"""
import requests

url = 'https://api.chucknorris.io/jokes/random'
responce = requests.get(url)
print(responce.text)