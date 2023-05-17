from random import randint

if __name__ == '__main__':
    # ЗАДАЧА 1
    # создается список из случайных элементов от 0 до 30 из 30
    # удалить элементы от 10 до 25
    lst1 = [randint(0, 31) for m in range(1, 31)]
    print(lst1)
    for i in tuple(lst1):
        if 10 <= i <= 25:
            lst1.remove(i)
    print(lst1)

    # ЗАДАЧА 2
    # Найти пересечение списков
    lst1 = [randint(0, 100) for m in range(1, 21)]
    lst2 = [randint(0, 100) for m in range(1, 11)]
    print(lst1)
    print(lst2)
    for i in tuple(lst1):
        if i not in tuple(lst2):
            lst1.remove(i)
    print(lst1)

    # ЗАДАЧА 3
    # Бинарный поиск
    # Сортированный список, есть ли число в этом списке
    lst1 = [randint(0, 100) for m in range(1, 11)]
    print(lst1)
    while True:
        if int(input()) in tuple(lst1):
            print(True)
        else:
            print(False)