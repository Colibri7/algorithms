from passwordmeter import test
from urllib.request import urlopen
from os.path import isfile
from random import choice, randint

from pip._vendor.urllib3.connectionpool import xrange

if not isfile('words.txt'):
    print(f'Downloading text.txt ...')
    url = 'https://docs.google.com/document/d/1uyBHRd-QqOZ40_n_nEC9SmItNxqhA1lHerhJplg2LaM/edit?usp=sharing'
    with open('text.txt', 'w') as f:
        f.write(urlopen(url).read())

words = open('text.txt', 'r').read().split('\n')
special_chars = ['!', '?']

def create_password(num_words=2,num_numbers=4,num_special=1):
    pass_str=''

    for _ in xrange(num_words):
        pass_str+=choice(words).lower().capitalize()

    for _ in xrange(num_numbers):
        pass_str+=str(randint(0,9))

    for _ in xrange(num_special):
        pass_str +=choice(special_chars)

    return pass_str


def main():
    pass_str = create_password()
    strength, _ = test(pass_str)
    print(f'\nPassword: %s' % pass_str)
    print(f'Strenght: %0,5' % pass_str)


if __name__ == '__main__':
    main()
