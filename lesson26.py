# -*- coding: utf-8 -*-

import pickle
import json
d = dict(name='Bob', age=20, score=88)
pickle.dumps(d)
print(d, 'test base')
f_path = 'D:/Users/fishzz/test2.txt'
f = open(f_path, 'wb')
pickle.dump(d, f)
f.close()

f = open(f_path, 'rb')
d = pickle.load(f)
f.close()
print(d, 'pickle load')

json_str = json.dumps(d)
print(json.loads(json_str), 'json')


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


def s2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }


s = Student('小鱼', 24, 98)
print(json.dumps(s, default=lambda obj: obj.__dict__, ensure_ascii=False), 'json class')
