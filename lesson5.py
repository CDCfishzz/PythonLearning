# -*- coding: utf-8 -*-
def power(x, n=2):
    s = 1
    while n >= 1:
        s = s * x
        n -= 1
    return s


def enroll(name, gender, age=6, city="Beijing"):
    print("name:", name)
    print("gender:", gender)
    print("age:", age)
    print("city:", city)


def calc(*number):
    pow_sum = 0
    for n in number:
        pow_sum += n**2
    return pow_sum


def person(name, age, *args, city='Beijing', gender, job, **kw):
    print('name:', name, 'age:', age, 'other:', city, gender, job, args, kw)


def product(x, *args):
    if args == ():
        return x
    for i in args:
        x = x * i
    return x


# print(product(5))
# person('zulu', 45, 'height=175', city='Sanya', gender='M', job='ATControler')
# extra = {'city': 'Haikou', 'gender': 'F', 'job': 'teacher'}
# person('sunny', 24, **extra)

# 递归函数&尾递归优化


def fact(n):
    if n == 1:
        return n
    return n * fact(n-1)


def fact1(n):
    return fact_iter(n, 1)


def fact_iter(num, pro):
    if num == 1:
        return pro
    return fact_iter(num-1, num*pro)


print(fact(10))
print(fact1(11))


def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        return move(n-1, a, c, b), move(1, a, b, c), move(n-1, b, a, c)


move(2, 'A', 'B', 'C')





def makelist(n, x):
    if n == 1:
        return x
    x.append(n-1)
    return makelist(n-1, x)


def moving(a, b, c):
    if (a + b)%2 == 0:
        a -= 1
        b += 1
        print(a, '-->', b)
    pass

