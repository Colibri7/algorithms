from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ['Name', 'Age', 'Country']
table.add_row(['Sasha', 45, 'Russian'])
table.add_row(['Naruto', 31, 'Japan'])
table.add_row(['Alex', 40, 'USA'])
table.add_row(['Bob', 25, 'Canada'])
table.add_row(['Li', 35, 'China'])

# выравнивание таблицы
table.align = 'r'
# сортировка
table.sortby = 'Age'

print(table)
