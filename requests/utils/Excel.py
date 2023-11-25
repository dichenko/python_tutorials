import openpyxl

# Создаем новую книгу Excel
wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = 'Пользователи'

# Записываем заголовки столбцов
sheet['A1'] = 'Имя'
sheet['B1'] = 'Возраст'
sheet['C1'] = 'Город'

# Вставляем данные
users = (
    ('Иван', 28, 'Москва'),
    ('Петр', 31, 'Санкт-Петербург'),
    ('Сидоров', 18, 'Казань')
)

for i, user in enumerate(users, start=2):
    sheet[f'A{i}'] = user[0]
    sheet[f'B{i}'] = user[1]
    sheet[f'C{i}'] = user[2]

wb.save('users.xlsx')