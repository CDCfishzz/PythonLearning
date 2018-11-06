class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

    def __repr__(self):
        return 'Student object (name: %s)' % self.name


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):  # create a iteration
        return self

    def __next__(self):  # return next one
        self.a, self.b = self.b, self.a + self.b
        if self.a > 10000:
            raise StopIteration()
        return self.a

    def __getitem__(self, item):  # become a list
        if isinstance(item, int):
            a, b = 1, 1
            for x in range(item):
                a, b = b, a + b
            return a
        if isinstance(item, slice):  # do thing like a slice list
            start, stop = item.start, item.stop
            if start is None:
                start = 0
            if stop is None:
                raise ValueError('Must get a stop Num in slice to avoid crash')
            a, b = 1, 1
            item_list = []
            for x in range(stop-1):
                if x >= start:
                    item_list.append(a)
                a, b = b, a + b
            return item_list
# create a iteration


for n in Fib():
    print(n)
f = Fib()
print(f[0], f[1], f[:6])
print(Student('Mike'))


