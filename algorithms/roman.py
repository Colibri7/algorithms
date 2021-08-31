import math


# Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True, если год високосный, и False иначе.


# Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа): периметр квадрата, площадь квадрата и диагональ квадрата.


# Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую время года, которому этот месяц принадлежит (зима, весна, лето или осень).

# Пользователь делает вклад в размере a рублей сроком на years лет под 10% годовых (каждый год размер его вклада увеличивается на 10%.
# Эти деньги прибавляются к сумме вклада, и на них в следующем году тоже будут проценты).
# Написать функцию bank, принимающая аргументы a и years, и возвращающую сумму, которая будет на счету пользователя.

# Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000, и возвращающую True, если оно простое, и False - иначе
class IsLeap():
    def is_year_leap(self, x):
        if x % 4 == 0:
            return f'leap'
        return f'not leap'

    def square(self, x):
        d = x * math.sqrt(2)
        p = 4 * x
        s = d * d / 2
        return f'Diagonal is {d}\nPerimetr is {p}\nSquare is {s}'

    def season(self, y):

        if y <= 3:
            return f'Winter'
        elif y <= 6:
            return f'Spring'
        elif y <= 9:
            return f'Summer'
        elif y <= 12:
            return f'Autumn'
        else:
            return False

    def bank(self, x, y):
        for i in range(y):
            x += x * 0.1
        return x

    def is_prime(self, x):
        if x / x and x / 1:
            return True
        else:
            return False

    def date(self, d, m, y):
        if d <= 31 and m <= 12 and y <= 2021:
            return True
        else:
            return False


obj = IsLeap()
print(obj.date(31, 2, 2010))
