import random


def randomfun():
    mas = []
    count = 0
    while count < 20:
        mas.append(random.randint(1, 100))
        count += 1
    return mas


a = randomfun()
print(a)


# 1. Создать произвольный массив из 20 элементов. Найти максимальный четный элемент массива.

def max_chet(arr):
    max = 0
    for i in arr:
        if i % 2 == 0 and i > max:
            max = i

    return max


print('макс четный', max_chet(a))


# 2. Создать произвольный массив из 20 элементов. Найти минимальный нечетный элемент массива.
def min_nechet(www):
    min = www[0]

    for i in www:
        if i < min and i % 2 != 0:
            min = i
    return min


print('минимальный нечетный', min_nechet(a))


# 3. Создать произвольный массив из 20 элементов.
# Найти все элементы, значение которых больше значения числа который лежит в самом начале (0 индекс).

def index0(qwerty):
    el = qwerty[0]
    for i in qwerty:
        if i > el:
            print('значение которых больше значения числа который лежит в самом начале (0 индекс)', i)


index0(a)


# 4. Создать произвольный массив из 20 элементов.
# Найти среднее значение(САЗ) массива.
# Показать каждый элемент массива, разделив его на САЗ

def saz(ab):
    average = sum(ab) / len(ab)

    for i in ab:
        print('каждый элемент массива, разделив его на САЗ', i / average)


saz(a)


# 5. Создать произвольный массив из 20 элементов.
# Найти сумму всех четных и нечетных элементов по отдельности.
# Вывести какая сумма больше.


def proiz(ba):
    even_sum, odd_sum = 0, 0

    for i in ba:
        if i % 2 == 0:
            even_sum += i
        else:
            odd_sum += i

    if even_sum > odd_sum:
        print('Сумма четных больше', even_sum)
    else:
        print('Сумма нечетных больше', odd_sum)


proiz(a)


# 6. Создать произвольный массив из 20 элементов.
# Найти минимальный элемент и его сумму с его индексом.

def minindex(ca):
    min_element = min(ca)
    min_index = ca.index(min_element)

    print('минимальный элемент и его сумму с его индексом',min_element + min_index)


minindex(a)



# 7. Создать произвольный массив из 20 элементов.
# Найти количество четных, нечетных, положительных, отрицательных чисел в массиве.

def naborchisel(nabor):
    positive, negative, even, odd = 0, 0, 0, 0

    for i in nabor:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1

        if i > 0:
            positive += 1
        else:
            negative += 1

    print('четных', even)
    print('нечетных', odd)
    print('положительных', positive)
    print('отрицательных', negative)


naborchisel(a)


# 8. Создать произвольный массив из 20 элементов.
# Вывести числа кратные 5 И значение индекса кратно 3.


def kratniy(zzz):
    index = 0

    for i in zzz:
        if i % 5 == 0 and index % 3 == 0:
            print('числа кратные 5 И значение индекса кратно 3',i)
        index += 1

kratniy(a)



# 9. Создать произвольный массив из 20 элементов.
# Найти нечетный элемент с максимальным значением,
# и найти его индекс.

def maxindex(maxi):
    max_element = 0
    max_index = 0

    for i in maxi:
        if i > max_element and i % 2 != 0:
            max_element = i
        max_index += 1
    print('найти его индекс',max_index,'нечетный элемент с максимальным значением' ,max_element)


maxindex(a)


# 10. Создать произвольный массив из 20 элементов.
# Найти сумму всех отрицательных нечетных чисел.

def sumnegative(negative):
    odd_sum = 0

    for i in negative:
        if i < 0 and i % 2 != 0:
            odd_sum += i

    print('сумму всех отрицательных нечетных чисел',odd_sum)

sumnegative(a)
