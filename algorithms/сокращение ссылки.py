# pip install pyshortenes

import pyshorteners
s = pyshorteners.Shortener()
print('Сокращенная ссылка - ',s.tinyurl.short('http://www.itmathrepetitor.ru/programmirovanie-zadachi-na-spiski/'))



