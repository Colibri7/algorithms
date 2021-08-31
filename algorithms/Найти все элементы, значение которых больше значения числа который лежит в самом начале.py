import random


# 3. Создать произвольный массив из 20 элементов.
# Найти все элементы, значение которых больше значения числа который лежит в самом начале (0 индекс).
def ran():
    mas = []
    count = 20
    while count != 0:
        mas.append(random.randint(1, 100))
        count -= 1
    for i in mas:
        if i > mas[0]:
            print(i)
    return mas


a = ran()
print(a)
