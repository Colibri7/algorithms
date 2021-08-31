f1 = f2 = 1
n = 10

print(f1,end=' ')
print(f2,end=' ')

for i in range(n):
    f1, f2 = f2, f1 + f2
    print(f2,end=' ')
