number = int(input())
dupn = str(number)
summ = 0
for i in range(len(dupn)):
    summ += int(dupn[i]) ** len(dupn)
print(summ)
if summ == number:

    print(f'Armstrong')
else:
    print(f'Not')
