from random import randint


def shift(lst, steps):
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            lst.append(lst.pop(0))
    else:
        for i in range(steps):
            lst.insert(0, lst.pop())


if __name__ == '__main__':
    nums = [4, 5, 6, 7, 8, 9, 0]

    shift(nums, -2)
    print(nums)

    nums = [4, 5, 6, 7, 8, 9, 0]

    shift(nums, 3)
    print(nums)
    list = [1,2,3,4]
    list.append(8)
    print(list.pop(1))

def f(n):
    if n != 0:
        return n * f(n-1)
    else:
        return 1


if __name__ == '__main__':
    print(f(5))

    # f(5) -> 5 * f(4)
    # f(4) -> 4 * f(3)
    # f(3) -> 3 * f(2)
    # f(2) -> 2 * f(1)
    # f(1) -> 1 * f(0)
    # f(0) -> 1

    lst1 = [randint(0, 31) for m in range(1, 31)]
    print(lst1)
    for i in tuple(lst1):
        if 10 <= i <= 25:
            lst1.remove(i)
    print(lst1)


    lst1 = [randint(0, 100) for m in range(1, 21)]
    lst2 = [randint(0, 100) for m in range(1, 11)]
    print(lst1)
    print(lst2)
    for i in tuple(lst1):
        if i not in tuple(lst2):
            lst1.remove(i)
    print(lst1)

    lst1 = [randint(0, 100) for m in range(1, 11)]
    print(lst1)
    while True:
        if int(input()) in tuple(lst1):
            print(True)
        else:
            print(False)
# ЗАДАЧА 1
# создается список из случайных элементов от 0 до 30 из 30
# удалить элементы от 10 до 25


# ЗАДАЧА 2
# Найти пересечение списков


# ЗАДАЧА 3
# Бинарный поиск
# Сортированный список, есть ли число в этом списке
