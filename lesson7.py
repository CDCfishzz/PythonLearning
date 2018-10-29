# -*- coding: utf-8 -*-

a = list(range(1, 11))
print(a)

print([x * x for x in range(1, 11) if x % 2 == 0])
print([m + n for m in 'ABC' for n in 'XYZ'])

dic = {'x': 'A',
       'y': 'B',
       'z': 'C'}
print([k + '=' + v for k, v in dic.items()])

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if isinstance(x, str)]
print(L2)
