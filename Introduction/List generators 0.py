import random
from random import randrange

# rangelist = [randrange(20, 51) for i in range(int(input()))]
# print(rangelist)

def list_(c = int(input()), a: int=20, b: int=50):
    lst = [random.randint(a, b) for i in range(c)]
    return lst

def spisok(k: int, a: int = 20, b: int = 50) -> list:
    lst = [random.randint(a, b) for _ in range(k)]
    return lst


if __name__ == '__main__':
    print(spisok(5, b=100))

if __name__ == '__main__':
    print(list_())
