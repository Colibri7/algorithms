def abbreviation(text):
    a = text.split(' ')
    for i in a:
        print(i[0].upper(), end='')


a = input()
abbreviation(a)
