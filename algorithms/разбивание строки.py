import textwrap

def wrap(string, max_width):
    x = textwrap.fill(string, max_width)
    return x

str = input(f'Введите текст: ')
n = int(input(f'на сколько слов хотите разделить: '))
print(wrap(str, n))

# N = 5
# name = ["Geek", "Geeks", "Geeksfor",
#         "GeeksforGeek", "GeeksforGeeks"]
# print(max(name, key=len))