'''
http://pythontutor.ru/lessons/int_and_float/problems/percents/
Процентная ставка по вкладу составляет P процентов годовых, которые прибавляются к сумме вклада.
Вклад составляет X рублей Y копеек.
Определите размер вклада через год.
Программа получает на вход целые числа P, X, Y и должна вывести два числа: величину вклада через год в рублях и копейках.
Дробная часть копеек отбрасывается.
'''

P = int(input())
X = int(input())
Y = int(input())

after_year = int(X * 100 + Y) * (100 + P) / 100

print(int(after_year // 100), int(after_year % 100))
