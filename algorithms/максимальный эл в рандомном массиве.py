def max_random_mas():
    import random
    arr = []
    count = 0
    while count != 20:
        arr.append(random.randrange(1, 1000))
        count += 1
    return f'The array : {arr}\nThe length of array : {len(arr)}\nThe max element in array : {max(arr)}'


a = max_random_mas()
print(a)
