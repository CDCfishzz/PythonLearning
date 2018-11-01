class Student(object):
    def __init__(self):
        self._score = ""
        self._birth = ""

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100!')
        self._score = value

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        if not isinstance(value, int):
            raise ValueError('birth must be integer!')
        self._birth = value

    @property
    def age(self):
        if not isinstance(self._birth, int):
            raise ValueError('score must be set!')
        return 2018 - self._birth

    pass


s = Student()
s.score = 60
print(s.score)
s.score = 100
print(s.score)

# homework


class Screen(object):
    def __init__(self):
        self._width = 0
        self._height = 0

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError('width must be a integer (as \'px\')')
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError('height must be a integer (as \'px\')')
        self._height = value

    @property
    def resolution(self):
        return self._height *self._width

    pass


# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')