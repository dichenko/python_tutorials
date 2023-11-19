from gtts import gTTS
import os

# Текст, который нужно озвучить
text_to_speak = "Привет! Как дела?"

# Указываем язык (по умолчанию 'en')
language = 'ru'

# Создаем объект gTTS
tts = gTTS(text=text_to_speak, lang=language, slow=False)

# Сохраняем озвученный текст в файл
tts.save("output.mp3")

# Открываем файл и проигрываем его (может потребоваться установка плеера)
os.system("start output.mp3")
