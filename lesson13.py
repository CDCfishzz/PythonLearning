import functools,time


def log(txt='call'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (txt, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log()
def now():
    print('2018-09-16')


def metric(fn):
    @functools.wraps(fn)
    def wppr(*args, **kw):
        st = time.time()
        fn(*args, **kw)
        et = time.time()
        t = (et - st) * 1000
        print('%s executed in %.1f ms' % (fn.__name__, t))
        return fn(*args, **kw)
    return wppr


@metric
def youuu():
    time.sleep(0.2)
    print('text in here')


def deco(txt='call'):
    def log(func):
        @functools.wraps(func)
        def warpper(*args, **kw):
            print('%s begin' % txt)
            st = time.time()
            func(*args, **kw)
            et = time.time()
            at = (et - st) * 1000
            print('%s call in %.2f ms' %(func.__name__, at))
            print('%s end' % txt)
            return func(*args, **kw)
        return warpper
    return log


@deco()
def meme(name='fishzz'):
    time.sleep(0.2)
    return name


@deco()
def fast(x, y):
    time.sleep(0.0012)
    return x + y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!', f)
elif s != 7986:
    print('测试失败!!', s)
else:
    print('成功', fast.__name__, s)

print(meme())
