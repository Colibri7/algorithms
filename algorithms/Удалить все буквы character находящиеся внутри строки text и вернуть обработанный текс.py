# 1. Написать функцию - remove, которая берет два аргумента, text - строка; character - одна буква
# (если character больше чем 1 буква - вывести ошибку).
# Удалить все буквы character находящиеся внутри строки text и вернуть обработанный текст.


def remove():
    text = str(input(f'Enter the text '))
    character = str(input(f'Enter the character '))
    if len(character) == 1:
        for i in text:
            if i == character:
                i.replace(character, '')
                continue
            print(i, end='')


remove()
