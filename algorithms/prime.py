def is_prime_1(num):
    for i in range(2, int(num ** 0.5)):
        if num % i == 0:
            print(i)
            print(num, 'is not prime')
            break
    else:
        print(f'is a prime')


def is_prime_2(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(num, f'is not prime')
                break
        else:
            print(num, f'is a prime')
    else:
        print(num, f'is not prime')
