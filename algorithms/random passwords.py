chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

number = int(input(f'Кол-во паролей: '))
lenght = int(input(f'Длина строки: '))
import random

for x in range(number):
    password = ''

    for i in range(lenght):
        password += random.choice(chars)

    print(password)
