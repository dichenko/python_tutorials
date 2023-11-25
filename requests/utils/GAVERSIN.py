import math

# Радиус Земли в км
R = 6371

# Координаты точек в градусах
lat1, lon1 = 55.751244, 37.618423
lat2, lon2 = 59.938633, 30.315868

# Переводим координаты в радианы
lat1 = math.radians(lat1)
lon1 = math.radians(lon1)

lat2 = math.radians(lat2)
lon2 = math.radians(lon2)

# Вычисляем координаты на сфере радиуса R
x1 = R * math.cos(lat1) * math.cos(lon1)
y1 = R * math.cos(lat1) * math.sin(lon1)
z1 = R * math.sin(lat1)

x2 = R * math.cos(lat2) * math.cos(lon2)
y2 = R * math.cos(lat2) * math.sin(lon2)
z2 = R * math.sin(lat2)

# Вычисляем расстояние между точками
d = math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)

print(f"Расстояние: {d} км")