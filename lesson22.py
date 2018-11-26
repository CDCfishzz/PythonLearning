# -*- coding: utf-8 -*-
from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))


@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


@unique
class Gender(Enum):
    male = 0
    female = 1


class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s' % name)


bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')

# for name, member in Month.__members__.items():
#     print(name, '=>', member, ',', member.value)
