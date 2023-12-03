
"""
1)Создать папку IMG и сохранить в нее все посление  фото
2) посмотреть список дат, на которые доступны фото земли https://api.nasa.gov/EPIC/api/natural/all?api_key=DEMO_KEY
Загрузить первую фотографию за каждый год. Файл фотографии доллжен содержать в названии дату, когда она сделана
"""

import requests
import json

API_URL = "https://api.nasa.gov/EPIC/api/natural/images?api_key=" # Сообщает информацию о последних фото земли
API_KEY = "Jh61EnWB52zymVUElf6pIcx96Gf___nxtKTypf4p" # Модифицировать
FULL_URL = API_URL+API_KEY
response = requests.get(FULL_URL)
print(response.text)

data = json.loads(response.text) # Преобразовываем ответ в JSON
with open("NASA.json", "w", encoding="UTF-8") as file_out:
    json.dump(data, file_out, ensure_ascii=False, indent=4)

# Извлекаем имя последнего изображения
image_name = data[0]['image']

# Формируем URL изображения
image_date = data[0]['date'].split()[0].replace('-', '/') # Меняем дефисы на слеши
image_url = f"https://api.nasa.gov/EPIC/archive/natural/{image_date}/png/{image_name}.png?api_key="+API_KEY

# Загружаем изображение
image_response = requests.get(image_url)

with open('img_NASA.png', 'wb') as fn: #Сохраняем фото на диск
    fn.write(image_response.content)
