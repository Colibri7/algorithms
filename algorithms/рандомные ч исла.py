import random


def randomic():
    arr = []
    count = 0
    while count < 20:
        arr.append(random.randint(0, 20))
        count += 1
    return arr


a = randomic()
print(a)

print(list(random.randint(1, 100) for _ in range(10)))
