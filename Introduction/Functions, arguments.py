def tree_shape1(rows: int):
    for row in range(0, rows):
        print(' ' * (rows - row + 20), end='')
        print('* ' * (row + 1))


def tree_shape_(rows: int):
    for row in range(0, rows):
        print(' ' * (rows - row + 20), end='')
        print('/', end='')
        print('--' * row, end='')
        print('\\')


def tree_shape2(rows: int):
    for i in range(1, rows + 1):
        print(f"{i * '* ' : ^50}")


def add_(x, y):
    return x + y


def substract_(x, y):
    return x - y


def multiply_(x, y):
    return x * y


def divide_(x, y):
    return x / y


def power_(x, y):
    return x ** y


if __name__ == '__main__':
    tree_shape2(7)
    tree_shape1(7)
    tree_shape_(7)
    a = float(input('enter:'))
    b = float(input('enter:'))
    print(add_(a, b))
    print(substract_(a, b))
    print(multiply_(a, b))
    print(divide_(a, b))
    print(power_(a, b))
    print(add_(multiply_(a, power_(a, divide_(1, b))), divide_(add_(a, b), substract_(a, b))))

#theory
a = 5
b = 3
c = 6
print("{1}, {0}, {2}".format(a, b, c))
print("{:^10}".format(10))
print('hello', 'hi', 'fbdfbf', sep='*')
def sum_values(*values):
    return


if __name__ == '__main__':
    print(sum_values(10, 4, 5, 6, 7, 20))
#returns a tuple = non-changeable list

# def sum_values(*values):


if __name__ == '__main__':
    print(sum_values(10, 4, 5, 6, 7, 20))

def mult_values(*values) -> int:
    p = 1
    for item in values:
        p *= item

    return p


if __name__ == '__main__':
    print(mult_values(10, 4, 5, 6, 7, 20))

# обязательные / необязательные аргументы
def pow_(value: int, k: int = 2) -> float:
    return pow(value, k)


if __name__ == '__main__':
    print(sum_values(10, 4, 5, 6, 7, 20))
    print(pow_(5))

def pow_(value: int, k: int = 2, s: int = 0) -> int:
    print(s)
    return value ** k


if __name__ == '__main__':
    print(sum_values(10, 4, 5, 6, 7, 20))
    print(pow_(k=7, value=3, s=10))
    print(sum_values(10, 4, 5, 6, 7, 20))
    v = 10
    print(pow_(12, k=v, s=10))
    func(a=1, b=2, c=3)


if __name__ == '__main__':
    print(sum_values(10, 4, 5, 6, 7, 20))
    v = 10
    print(pow_(12, k=v, s=10))
    func(v=1, c=2, e=3)


# именованные аргументы
def func(**values):
    print(values)


# позиционные аргументы
def sum_values(*values) -> int:
    p = 0
    for item in values:
        p += item

    return p


# обязательные / необязательные аргументы
def pow_(value: int, k: int = 2, s: int = 0) -> int:
    print(s)
    return value ** k


if __name__ == '__main__':
    print(sum_values(10, 4, 5, 6, 7, 20))
    v = 10
    print(pow_(12, k=v, s=10))
    func(v=1, c=2, e=3)