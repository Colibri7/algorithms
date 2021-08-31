str1 = str(input())
str2 = str(input())
arr1 = []
arr2 = []




for i in str1:
    arr1.append(str(ord(i) - 97))

for j in str2:
    arr2.append(str(ord(j) - 97))
result1 = int(''.join(arr1))
result2 = int(''.join(arr2))
print(result1 + result2)
