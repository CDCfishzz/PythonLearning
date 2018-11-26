class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

    def __repr__(self):
        return 'Student object (name: %s)' % self.name

    def __call__(self):
        print('My name is %s' % self.name)

    def __getattr__(self, attr):
        if attr == 'score':
            return 98
        if attr == 'age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)


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


class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    def users(self, user_name):
        return Chain('%s/%s' % (self._path, user_name))
        pass

    # GET / users /: user / repos
    # 调用时，需要把: user替换为实际用户名。如果我们能写出这样的链式调用：
    # Chain().users('michael').repos

    __repr__ = __str__


# for n in Fib():
#     print(n)
f = Fib()
# print(f[0], f[1], f[:6])
# print(Student('Mike'))

s = Student('FishZz')
s()
print(s.score, s.age(), )
print(Chain().status.users('FishZz').timeline.list)
