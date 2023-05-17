from datetime import date, datetime, time, timedelta

current = datetime.today()
print(current)
day2 = timedelta(weeks=2)
print(day2)
day3 = current + day2
print(day3)
print(day3.strftime("%y %A %d %B"))
stroka = day3.strftime("%y %A %d %B")
print(datetime.strptime(stroka, "%y %A %d %B"))

day = datetime(2002, 9, 6)
print(day)
d = "07/23/19"
print(datetime.strptime(d, "%x"))
print(datetime.strptime(d, "%m/%d/%y"))

from dateparser import parse
#HW Ввод начало подписки на нетфликс и количество дней на сколько действиует.
# Работае ли подписка сейчас? Формат ввода даты выбираем сами. Вводим количество дней сами
# dateparser
from dateparser.search import search_dates
print(parse("10小时前"))
