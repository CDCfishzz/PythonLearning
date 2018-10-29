# -*- coding: utf-8 -*-
dict0 = {'Michael': 95,
         'Bob': 75,
         'Tracy': [2, 2]}
dict0['Tracy'][1] = 3
print(dict0['Tracy'])
a = abs
print(a(-1))

n1 = 255
n2 = 1000
print(hex(n1), hex(n2))


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-19))
