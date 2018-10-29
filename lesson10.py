# -*- coding: utf-8 -*-
from functools import reduce


def add(x, y, f):
    return f(x) + f(y)


print(add(-5, -11, abs))


def ff(x):
    return x * x


r = map(ff, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))


def fn(x, y):
    return x * 10 + y


ra = reduce(fn, [1, 2, 3, 4, 5])
s = '123456'


def char2int(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
              '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


print(reduce(fn, map(char2int, s)))
s = 'a'
print(ord(s))


def normalize(name):
    def upper2lower(s):
        if ord(s) >= 65 and ord(s) <= 90:
            return chr(ord(s) + 32)
        return s
    def lower2upper(z):
        if ord(z) >= 97 and ord(z) <= 122:
            return chr(ord(z) - 32)
        return z
    def str2add(x, y):
        return str(x) + str(y)
    if name == '':
        return name
    elif len(name) == 1:
        return lower2upper(name[0])
    return lower2upper(name[0]) + reduce(str2add, map(upper2lower, name[1:]))


print(normalize('fishzz'))


def prod(L):
    def fn2times(x, y):
        return x * y
    return reduce(fn2times, L)


print(prod([3, 5, 7, 9]))
print('12'.find('.'))


def str2float(s):
    digits2 = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
               '7': 7, '8': 8, '9': 9}

    def change2digit(x):
        return digits2[x]

    def str2int(a):
        if a == '':
            return 0
        return reduce(fn, map(change2digit, a))

    i = s.find('.')
    if i == -1:
        return str2int(s)

    return str2int(s[:i]) + str2int(s[i+1:]) / 10 ** (len(s) - i - 1)


print(str2float('1.231'))
