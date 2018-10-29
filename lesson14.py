import functools

int2 = functools.partial(int, base=2)

print(int2('10'), int2('10', base=10))