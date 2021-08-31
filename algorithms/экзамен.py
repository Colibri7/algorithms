# 1. Написать функцию - remove, которая берет два аргумента, text - строка;
# character - одна буква (если character больше чем 1 буква - вывести ошибку).
# Удалить все буквы character находящиеся внутри строки text и вернуть обработанный текст.
#
# def remove():
#     text = str(input('введите текст '))
#     if len(text) == 1:
#         print('Ошибка')
#     character = str(input('введите букву '))
#
#     for i in text:
#         if i == character:
#             i.replace(character, '')
#             continue
#
#         print(i, end='')
#
# remove()

#


# 2. Написать функцию - generate_list, которая принимает аргументы n - int, start - int, end - int.
# Сгенерировать массив из n рандомных элементов в промежутке от start до end.
# Использовать list comprehension для генерации массива.

# import random
# #
# #
# def generate_list():
#     mas = []
#     start = int(input('начало '))
#     end = int(input('конец '))
#     mas.append(random.randint(start,end))
#
#
#     return mas
#
#
# a = generate_list()
# print(a)

# 3. Написать функцию - contains, которая принимает аргументы: arr - массив из чисел, x - int.
# Вернуть True, если массив содержит в себе x, иначе False.
# Использовать вспомогательные функции - нельзя.

# import random
# def contains():
#     arr = []
#     count = 0
#     while count < 5:
#         arr.append(random.randint(1, 100))
#         count += 1
#
#
#     return arr
#
# a = contains()
# print(a)
# x = int(input('введите число '))
#
# if x in a :
#     print('true')
# else:
#     print("false")


# 4. Написать функцию - count_unique.
# Принимает массив и возвращает количество различных элементов массива.
# Пример: для [1, 4, 5, 1, 1, 3] ответ 4.

#
# def  count_unique():
#     mas = []
#     count = 0
#     while count < 20:
#         mas.append(random.randint(1, 100))
#         count += 1
#     return mas
#
#
# a = randomfun()
# print(a)


# 5. Компьютер загадывает число от 1 до n. У пользователя k попыток отгадать.
# После каждой неудачной попытки компьютер сообщает меньше или больше загаданное число.
# В конце игры текст с результатом (или “Вы угадали”, или “Попытки закончились”).
