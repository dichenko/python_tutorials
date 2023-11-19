# OpenTrivia Database это база вопросов для викторины на любые темы
# Создайте игру-викторину, где пользователю предлагают выбрать уровень сложности и ответить на 5 вопросов
# категории "Computer Science"

import requests

url = 'https://opentdb.com/api.php'
params = {
    'amount': 5,
    'category': '27',  # Категория "Animals"
    'difficulty': 'easy',
    'type': 'multiple'
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    questions = data['results']
    for i, question in enumerate(questions, start=1):
        print(f"Вопрос {i}: {question['question']}")
        print(f"Варианты ответов: {', '.join(question['incorrect_answers'] + [question['correct_answer']])}\n")
else:
    print("Ошибка при выполнении запроса. Код состояния:", response.status_code)
