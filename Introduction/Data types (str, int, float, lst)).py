#task 1
a = int(input("Начало диапазона:"))
b = int(input("Конец диапазона:"))
c = int(input('Введите шаг:'))
for x in range(a,b + 1,c):
   if x % 2 == 0:
    print(x)



import numpy as np
while True:
   a = int(input("Enter:"))
   b = a % 2
   if b == 0:
       print(a)
   else:
       print('odd')

num = np.append(num, b)
print(num)

num = np.array([])
num = np.append(num,a)
for n in num:
        if n % 2 == 0:
          print(num)

a = int(input("Enter:"))
num = np.array([])
num = np.append(num,a)
for n in num:
   if n % 2 == 0:
       print(num)



#Task 3
from datetime import datetime
import numpy as np
birthdate = input("Enter your birthdate YYYY-MM-DD:")
bd = birthdate.split("-")
bd_array = np.array(bd,int)
today = datetime.now()
datetoday = today.strftime('%Y-%m-%d')
yeartoday = int(today.strftime('%Y'))
monthtoday = int(today.strftime('%m'))
daytoday = int(today.strftime('%d'))
#   print(f'You are {yeartoday - bd_array[0]} years old')

if bd_array[1] > monthtoday:
   print(f'You are {yeartoday - bd_array[0]-1} years old')
elif bd_array[1] == monthtoday and bd_array[2] > daytoday:
   print(f'You are {yeartoday - bd_array[0]-1} years old')
elif bd_array[1] == monthtoday and bd_array[2] <= daytoday:
   print(f'You are {yeartoday - bd_array[0]} years old')



#Task 2
lst = []
for i in range(0,10):
   number = int(input('Enter the number:'))
   lst.append(number)
print(lst)
sum_even = 0
sum_odd = 0
for x in lst:
   if x % 2 == 0:
       sum_even += x
   else:
       sum_odd += x
print(f' Sum of odd numbers: {sum_odd}')
print(f' Sum of even numbers: {sum_even}')
print(f' Difference: {sum_even-sum_odd}')
max = max(lst)
min = min(lst)
print(f' Max*Min: {max*min}')




#Task 4
a = input('Enter string 1:')
b = input('Enter string 2:')
if a in b or b in a:
   print('Substring found')
else:
   print('No substrings')




#Task 5
numlist = []
while True:
   x = int(input('Enter the number:'))
   numlist.append(x)
   if x == 0:
        print(f'Zero found \nSum: {sum(numlist)}')
        break





#Task 6
def divsum(x):
    sum = 0
    for i in range(1,x):
        if x % i == 0:
            sum += i
    return sum
j = 10000
for i in range(1, j + 1):
    if divsum(i) == i:
        print(f' {i} is a perfect number')




#Task 7
a = input('Enter your word:')
if len(set(a.upper())) == len(a.upper()):
    print(f'no duplicates: {a.upper()}')
else:
    print(a.lower())





