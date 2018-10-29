from collections import Iterable

# 生成器, generator

L = [x * x for x in range(1, 11)]
print(L)
G = (x * x for x in range(1, 11))
for x in G:
    print(x)


def fib(max):
    n, a, b = 0, 0, 1
    ll = []
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'


def odd():
    print(1)
    yield 2
    print(3)
    yield 4
    print(5)
    yield 6


def triangles():
    l = [1]
    while True:
        yield l
        l = [1] + [l[x]+l[x+1] for x in range(0, len(l)-1)] + [1]


n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 9:
        break

print(isinstance(results, Iterable))
