'''
http://pythontutor.ru/lessons/int_and_float/problems/raznost_vremen/
Даны значения двух моментов времени, принадлежащих одним и тем же суткам: часы, минуты и секунды для каждого из моментов времени. Известно, что второй момент времени наступил не раньше первого. Определите, сколько секунд прошло между двумя моментами времени.

Программа на вход получает три целых числа: часы, минуты, секунды, задающие первый момент времени и три целых числа, задающих второй момент времени.

Выведите число секунд между этими моментами времени.
'''

h_start = int(input())
m_start = int(input())
s_start = int(input())
h_end = int(input())
m_end = int(input())
s_end = int(input())

print((h_end * 3600 + m_end * 60 + s_end) - (h_start * 3600 + m_start * 60 + s_start))
#print((h_end - s_start) * 3600 + (m_end - m_start) * 60 + s_end - s_start)
