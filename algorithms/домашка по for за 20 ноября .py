import math

# 1. Найти числа кратные 7 в промежутке от 1 до 1000, и сумма цифр этого числа должна быть кратная 7.

# a = range(0, 1000, 7)
# b = 7
#
# for i in a:
#     if i % 10 == b or i % 100 == b:
#         print(i)

# 2. Ввести число. Найти сумму квадратов цифр этого числа.
#
# a = int(input('Ввести число '))
#
# for i in range(a):
#     b = a % 10
#     y = a // 10
# print(b ** 2 + y ** 2)

# 3. Найти сумму модулей (math.fabs) нечетных чисел с -100 до 100.
#
# a = range(-100, 100)
# total = 0
#
# for i in a:
#     if i % 2 != 0:
#         b = math.fabs(i)
#         total += b
# print(total)

# 4. В промежутке от 0 до 999 вывести все трехзначные числа, которые кончаются на 3.

# a = range(0, 1000)
#
# for i in a:
#     if i > 100:
#         if i % 100 == 3 or i % 10 == 3:
#             print(i)
