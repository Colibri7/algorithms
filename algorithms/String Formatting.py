integ = int(input())
for i in range(1,integ+1):
    print(f'{i}{hex(i).upper()[2:]}   {oct(i)[2:]}   {bin(i)[2:]}')