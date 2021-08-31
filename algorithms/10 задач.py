# 1. How do you find the missing number in a given integer array of 1 to 100?
# 2. How do you find the duplicate number on a given integer array?
# 3. How do you find the largest and smallest number in an unsorted integer array?
# 4. How do you find all pairs of an integer array whose sum is equal to a given number?
# 5. How do you find duplicate numbers in an array if it contains multiple duplicates?
# 6. How do you remove duplicates from an array in place?
# 7. How are duplicates removed from an array without using any library?
# 8. How do you count the occurrence of a given character in a string?
# 9. How are duplicate characters found in a string?
# 10. How do you check if two strings are anagrams of each other?


# 1
limit = 20
mas = [1, 5, 20]
missingNum1 = list(set(range(1, limit + 1)) - set(mas))
missingNum2 = [i for i in range(20) if i not in mas]

print(missingNum1)
print(missingNum2)

# 2
mas = [4, 6, 7, 8, 4, 3, 2, 3, 4, 5, 6, 7, 7, 8]
arr = [ ]
for i in range(len(mas)):
    for j in range(i+i,len(mas)):
        if mas[i]==mas[j] and mas[i] not in arr:
            arr.append(mas[i])
print(arr)


# 3
import random
arr = []
count = 0
while count < 20:
    arr.append(random.randint(0, 20))
    count += 1
for i in range(len(arr) - 1):
    for j in range(len(arr) - i - 1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)

# 4
sum_ = int(input())
count=0
mas = [4, 5, 6, 7, 2, 5, 6]
for i in range(0,len(mas)):
    for j in range(i+1,len(mas)):
        if mas[i]+mas[j]==sum_:
            print(f'{mas[i]} and {mas[j]}')
            count+=1
print(f'pairs : {count}')


# 5
from collections import Counter

a = [1, 3, 4, 5, 6, 7, 5, 4, 3, 2, 4, 5, 7, 8, 9, 7]
print(Counter(a).most_common(len(a)))

# 6
a = [1,1,1, 3, 4, 5, 6, 7, 5, 4, 3, 2, 4, 5, 7, 8, 9, 7]
arr = []
for i in a :
    if i not in arr:
        arr.append(i)
print(arr)

# 8
string = input()
character = input()
count = 0
for i in string:
    if i ==character:
        count+=1
print(count)



# 10
string = input()
if list(string)==list(string[::-1]):
    print(f'yes')
else:
    print(f'not')

print(list(string))
print(list(string[::-1]))