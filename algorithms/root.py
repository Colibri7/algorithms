def findroot(n):
    root = n / 2
    for _ in range(10):
        root = (root + n / root) / 2
    print(root)


n = 56
findroot(49)
