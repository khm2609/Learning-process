def slice_sum(list_, start=None, end=None) -> int:
    slice_ = list_[start: end]
    sum_ = 0
    for i in slice_:
        sum_ += i
    return sum_


def some_date(day: int, month: int, year: int) -> bool:
    nonexistent = [[30, 2], [31, 2], [31, 4], [31, 6], [31, 9], [31, 11]]
    if 1 <= day <= 31 and 1 <= month <= 12 and [day, month] not in nonexistent:
        return True
    else:
        return False


def prime_nums_count(*nums):
    count = 0
    for num in nums:
        c = 0
        for n in range(1, num + 1):
            if num % n == 0:
                c += 1
        if c <= 2:
            count += 1
    return count



if __name__ == '__main__':
    lst = [1, 5, 9, 6, 349, 22, 40]
    print(slice_sum(lst, start=2, end=4))
    print(some_date(3, 4, 2022))
    print(prime_nums_count(2, 4, 5, 6, 7, 9, 9, 9, 3, 1, 1, 3))

def sum_list(*args):
    count = 0
    print(args)
    for item in args:
        if type(item) != int:
            continue

        k = 0
        for i in range(2, item // 2 + 1):
            if item % i == 0:
                k += 1

        if k == 0:
            count += 1

    return count


if __name__ == "__main__":
    i = 0
    lst = tuple([int(i) for i in input().split()])
    print(sum_list(*lst))
