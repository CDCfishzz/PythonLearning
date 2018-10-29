# -*- coding: utf-8 -*-


def is_odd(num):
    return num % 2 == 1


def not_empty(str):
    return str and str.strip()


a = list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(a)
print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))


def _odd_iter():
    n = 1
    while True:
        n += 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)


# for n in primes():
#     if n < 1000:
#         print(n)
#     else:
#         break


def is_palindrome(num):
    return str(num) == str(num)[::-1]


output = filter(is_palindrome, range(1, 1000))

li = [5, -12, 9, 23, 7, -1]
mi = ['bob', 'about', 'Zoo', 'Credit']
print(sorted(li))
print(sorted(li, key=abs))
print(sorted(mi), sorted(mi, key=str.lower, reverse=True))

LL = [('Bob', 75), ('Adam', 92), ('bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[0].lower()


def by_score(t):
    return -t[1]


print(sorted(LL, key=by_name), sorted(LL, key=by_score))
