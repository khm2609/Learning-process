#TASK 1 BEGINNING

from random import *

import math

a = int(input('Введите начало диапазона:'))
b = int(input('Введите конец диапазона:'))
k = int(input('Введите длину диапазона:'))

lst = []
for i in range(k):
    if a < b:
        lst.append(randint(a, b))
    else:
        lst.append(randint(b, a))
print(lst)

total_odd_u, total_even_d, sum_odd_d, multiplied_even_u = 0, 0, 0, 0
for n in lst:
    if lst.count(n) == 1:
        multiplied_even_u = 1
        if n % 2 != 0:
            total_odd_u += 1
        else:
            multiplied_even_u = multiplied_even_u * n
            # multiplied_even_u = math.prod(lst)
    else:
        if n % 2 == 0:
            total_even_d += 1
        else:
            sum_odd_d = sum_odd_d + n

print(f' Количество чётных дупликатов: {total_even_d}')
print(f' Количество нечётных уникальных: {total_odd_u}')
print(f' Произведение чётных уникальных: {multiplied_even_u}')
print(f' Сумма нечётных дупликатов: {sum_odd_d}')



#TASK 2 BEGINNING
digits, letters = 0, 0
digit_lst, alph_lst = [], []

while True:
    st = input('enter:')
    # letters = sum(s.isalpha() for s in st)
    # digits = sum(s.isdigit() for s in st)
    if st == '':
        break
    for s in st:
        digits, letters = 0, 0
        if s.isdigit():
            digits += 1
        elif s.isalpha():
            letters += 1
    if letters > digits:
        alph_lst.append(st)
    else:
        digit_lst.append(st)

digit_lst.pop(-1)
print(max(alph_lst, key=len))
print(min(digit_lst, key=len))


#TASK 3 BEGINNING
from random import randint
a = input('Введите "1" - Орёл или "2" - Решка')
while a.lower() not in ['', 'no', 'stop', 'нет', 'стоп']:
    outcome = randint(1, 2)
    if str(outcome) == a:
        print('Good guess')
        break
    else:
        print('You lost')
        a = input('Enter "1" - Heads or "2" - Tails')





