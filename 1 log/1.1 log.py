# Создание массива вручную
mass = [343,324,234,234,565,4,342,233,999]

# Создание переменных для максимума и минимума в массиве
maxx = 0
minn = 10000000

# Поиск и сохранение в переменные максимального и минимального элемента
for i in mass:
    if i > maxx:
        maxx = i
    elif i < minn:
        minn = i

# Вывод разницы между максимальным и минимальным элементом
print(maxx - minn)
    

