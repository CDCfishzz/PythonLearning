def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax += n
        return ax
    return sum


f = lazy_sum(1, 2, 3, 4, 5)
f2 = lazy_sum(1, 2, 3, 4, 5)
print(f(), f == f2)


def count():
    def ff(j):
        def g():
            return j * j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(ff(i))
    return fs


f1, f2, f3 = count()
print(f1(), f2(), f3())


def create_counter():
    n = [0]

    def counter():
        n[0] += 1
        return n[0]
    return counter


counterA = create_counter()
print(counterA(), counterA(), counterA(), counterA(), counterA())


def is_odd(n):
    return n % 2 == 1


L = list(filter(lambda x: x % 2 == 1, range(1, 20)))
print(L)
