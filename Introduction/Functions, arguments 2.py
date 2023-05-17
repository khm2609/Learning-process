def func(a, b, c=2):
    return a+b+c
if __name__ == '__main__':
    print(func(1,2,3))

def add_mean(x, *data):
    return x + sum(data) / float(len(data))


if __name__ == "__main__":
    print(add_mean(10, 0, 1, 2, -1, 0, -1, 1, 2))


i = 0


def increment():
    global i
    i += 1


if __name__ == "__main__":
    increment()
    print(i)


def increment():
    i = 3
    i += 1


if __name__ == "__main__":
    i = 0

    increment()
    print(i)

from random import randint


def fill_list(m1, m2, amount, l):
    for i in range(amount):
        l.append(randint(m1, m2))


def analysis(your_list, your_dict):
    for i in your_list:
        if i in your_dict:
            your_dict[i] += 1
        else:
            your_dict[i] = 1


if __name__ == "__main__":
    lst = []
    dct = {}

    mn = int(input('Минимум: '))
    mx = int(input('Максимум: '))
    qty = int(input('Количество элементов: '))

    fill_list(mn, mx, qty, lst)
    analysis(lst, dct)

    print(lst)

    for item in sorted(dct):
        print("'%d':%d" % (item, dct[item]))