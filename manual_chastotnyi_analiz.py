import re
import string
from pymorphy2 import MorphAnalyzer
from nltk.corpus import stopwords
#nltk.download("stopwords") запустить один раз для обновления словаря стоп-слов


# 1__ Берем текстовый файл и считываем из него  текст
with open("input.txt", encoding="UTF-8") as f:
    text = f.read()

def hands_re(text):
    """
    Разбивает текст на слова регулярками
    :param text: Входной текст
    :return: список слов
    """
    # собираем символы которые будем отбрасывать
    punctuation = string.punctuation + '\u2014\u2013\u2012\u2010\u2212' + '«»‹›‘’“”„`'
    word_tokenize = re.compile(r"([^\w_\u2019\u2010\u002F-]|[+])")
    words = []
    for token in word_tokenize.split(text):
        # если слово не попадает в те которые мы исключаем
        if token and not token.isspace() and not token in punctuation:
            # добавляем слово в список
            words.append(token.lower())
    # возвращаем список слов
    return words


# 2__ Получаем массив слов без пунктуации и непечатных символов
words = hands_re(text)
print(len(words), words[:20])

# 3__ Нормализуем слова
def to_normal_form(words):
    """
    Приводит слова к нормальным формам
    :param words: список слов
    :return: список нормальных форм
    """
    result = []
    # создаем анализатор
    morph = MorphAnalyzer()
    # перебираем слова
    for word in words:
        # получаем нормальную форму
        normal = morph.parse(word)[0].normal_form
        # добавляем в новый список
        result.append(normal)
    #возвращаем нормальные формы
    return result

words = to_normal_form(words)
print(len(words), words[:20])



# 4__ Очищаем слова от стоп-слов
stop = stopwords.words("russian")
def no_stop(words):
    """
    Убираем из списка стоп слова
    :param words: входной список слов со стоп словами
    :return: новый список слов без стоп слов
    """
    # получаем русские стоп слова и по желанию добавляем свои
    stop_words = stopwords.words('russian') + ["…", "это", "всё", "свой", "весь", "который",
                                               "ещё", "очень", "какой-то", "какой-нибудь"]
    without_stop = []
    # перебираем слова
    for word in words:
        # если это не стоп слово
        if word not in stop_words:
            # записываем в список
            without_stop.append(word)
    # возвращаем слова без стоп слов
    return without_stop

words = no_stop(words)
print(len(words), words[:20])

# 5__ Создаем словарь и считаем сколько раз в тексте встретилось нам каждое слово
d = dict()
for k in words:
    d[k] = d.get(k, 0) + 1

# 6__ Сортируем словарь и записываем результаты в файл
with open("output.txt", "w", encoding="UTF-8") as f:
    le = len(d)
    f.write(f"Всего слов после очистки: {le}\n")
    for k,v in sorted(d.items(), key=lambda x: (-x[1], x[0])):
        f.writelines(f"{k} {v}шт ({round(v * 100 / le, 2)})%\n")