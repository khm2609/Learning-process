n = input()
nrs = n.replace(' ', ',').split(',')
x = float(nrs[0])
y = float(nrs[1])
x1 = float(nrs[2])
y1 = float(nrs[3])
x2 = float(nrs[4])
y2 = float(nrs[5])
r = float(nrs[6])
s = nrs[7]
incircle = x ** 2 + y ** 2 <= r ** 2
insquare = x1 <= x <= x2 and y1 <= y <= y2
if int(s) == 0:
    print(incircle or insquare)
elif int(s) == 1:
    print(incircle and insquare)
if incircle and insquare and int(nrs[7]) == 1:
    print('True')
elif (incircle or insquare) and int(nrs[7]) == 0:
    print('True')
else:
    print('False')
l = list(input())
l.pop(0)
print(l.count('a'))


import sys
import numpy as np
import array as arr

a = np.array([[1, 2, 3], [4, 5, 6]], int)

a.reshape(3, 2)

print(a.flatten())
countstr = 0
lst = []
lst1 = [1, 2, 3]
lst2 = ['r', 3, 'e']
lst3 = [lst1, lst2]
print(lst3)
while True:
    line = input("Enter:")
    countstr = countstr + 1
    print(countstr)
    lstinp = line.split(' ')
    lstinp1 = [int(x) for x in lstinp]
    print(lstinp1)
    fullst = [lstinp1]
    print(fullst)
    matrix = np.array([fullst]).reshape(countstr, len(lstinp1))
    print(matrix)

matrix = []
countstr = 0
for line in sys.stdin:
    countstr = countstr + 1
    matrix.append([float(i) for i in line.split()])
    matrix1 = np.array([matrix]).reshape(countstr, len(line.split()))
    result = np.all((matrix1 == 0), axis=0)
    print(result)
    count = np.sum(result)
    print(count)
    for [i] in result:
        if i:
            result.cou
            count(result, i)
            print(result.count(i))
a = np.array([[1, 2, 3], [4, 5, 6]], int)

a.reshape(3, 2)

a.flatten()
b = np.sum(a, axis=1)
c = np.sum(b)
print(b)
print(c)
print(a.shape)
e = a - 0.5
print(e)

import pandas as pd
import numpy as np
df = pd.DataFrame(data=np.arange(20).reshape(4, 5), columns=list('abcde'))
df['f'] = df['a'] + df['b'] + df['c'] + df['d'] + df['e']
print(df)
print(df['f'])
import random
from random import randint

import numpy as np

import pandas as pd

df = pd.read_csv

n = 8
s = 10
b = np.random.randint(1, s + 1, size=n)


prob = [0 for i in range(s)]
print(prob)
print(range(s))
print(b)

for i in range(s):
  print([b == (i + 1)])
  print(b[b == (i + 1)])
  # len(b[b == (i + 1)])
  print(len(b[b == (i + 1)]))
  prob[i] = len(b[b == (i + 1)])/ n
#  print(i, '\n', prob, '\n','\n')
if n <= 25:
  print('\n\n', f'S = {s}. N = {n}', np.sort(b), '\n', prob)
else:
  print('\n', '***** ***** *****', '\n', f'S = {s}. N = {n}\n', prob)

x = random.choice([1, 1, 2, 5, 6, 7, 3, 4, 5, 6])
print(x)








