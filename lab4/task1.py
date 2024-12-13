from math import *
import datetime as dt

print('квадратный корень: ', sqrt(float(input('Введите число для извлечения квадратного корня: '))))
print('Сегодня:', dt.datetime.now().date() , '\nтекущее время:', str(dt.datetime.now().time())[:8])
