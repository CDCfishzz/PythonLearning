# -*- coding: utf-8 -*-
# collections
from collections import namedtuple, deque, defaultdict

# namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)

Circle = namedtuple('Circle', ['x', 'y', 'r'])
c = Circle(3, 4, 5)
print(c)

# deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.popleft()
q.appendleft('y')
print(q)

# default_dict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'], dd['key2'])

# OrderedDict
