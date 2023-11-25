# pip install Pillow
from PIL import Image
import itertools


# Функция разбиения изображения на части
def split_image(img, parts=3):
    width, height = img.size
    subheight = height // parts
    images = []

    for i in range(parts):
        area = (0, i * subheight, width, (i + 1) * subheight)
        img_crop = img.crop(area)
        images.append(img_crop)

    return images


# Открываем изображение
img = Image.open('14.jpg')

# Разбиваем на 3 части
images = split_image(img)

# Сохраняем части как отдельные изображения
for i, img in enumerate(images):
    img.save(f'piece{i}.png')

# Составляем из частей гифку
frame_durations = [100 for img in images]+[100]
frames = itertools.cycle(images)

images[0].save('gif.gif', format='GIF', append_images=images,
               save_all=True, duration=frame_durations, loop=0)