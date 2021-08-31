number = 5
# рекурсия не может вызвать само себя более 1000 раз
def factorial(n):
    if n == 0:
        return 1
    return factorial(n - 1) * n

print(factorial(number))
# с помощью цикла
n = 5
f = 1
i = 0
while i < n:
    i += 1
    f = f * i
print(f)

