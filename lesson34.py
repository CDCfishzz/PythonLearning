# -*- coding: utf-8 -*-
# collections
import argparse
import collections
import os

from collections import ChainMap
from collections import Counter
# namedtuple

Point = collections.namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)

Circle = collections.namedtuple('Circle', ['x', 'y', 'r'])
c = Circle(3, 4, 5)
print(c)

# deque
q = collections.deque(['a', 'b', 'c'])
q.append('x')
q.popleft()
q.appendleft('y')
print(q)

# default_dict
dd = collections.defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'], dd['key2'])

# OrderedDict
d0 = dict([('a', 1), ('c', 2), ('b', 3)])
print('d0:', d0)
od = collections.OrderedDict()
od['z'] = 1
od['a'] = 2
od['s'] = 3
print(list(od.keys()))
# ordered dict 实现FIFO


class LastUpdatedOrderedDict(collections.OrderedDict):
    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        contains_key = 1 if key in self else 0
        if len(self) - contains_key >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if contains_key:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        collections.OrderedDict.__setitem__(self, key, value)


# chainMap
# 构造缺省参数
defaults = {
    'color': 'red',
    'user': 'guest'
}

# 构造命令行参数
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
command_line_args = {k: v for k, v in vars(namespace).items() if v}

# 组合成chain map
combined = ChainMap(command_line_args, os.environ, defaults)

# 打印参数
print('color=%s' % combined['color'])
print('user=%s' % combined['user'])

# counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
