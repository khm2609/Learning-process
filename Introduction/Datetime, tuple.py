import random
from datetime import date, datetime, time, timedelta

d, m, y = map(int, input('Enter start date in dd-mm-yyyy format:').split('-'))
sd = datetime.date(d, m, y)
print(sd)

sd = datetime.strptime(input("enter start date in dd-mm-yyyy format:"), "%d-%m-%Y")
print(sd)
delta = timedelta(days=int(input("Enter subscription period in days:")))
if sd + delta >= datetime.today():
    print("still valid")
else:
    print('already invalid')

b = {1, 3, 9, 10}
a = {1, 2}
a.add(3)
print(a.update([1,2]))
print(a|b)
a.union(b)
print(a&b)
print(a-b)
a.symmetric_difference(b)
a.intersection(b)
print(a^b)
a.difference(b)
print(a>=b)

a.discard(2)
a.pop()
a.remove(3)

lst1 = [random.randint(0, 50) for i in range(20)]
print(lst1)
lst2 = [random.randint(0, 50) for i in range(20)]

print(lst2)
print(set(lst1).symmetric_difference(set(lst2)))
print(set(lst1).intersection(set(lst2)))
print(set(lst1+lst2))




