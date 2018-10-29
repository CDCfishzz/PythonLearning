class Student(object):

    @property
    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100!')
        self._score = value

    pass


s = Student()
s.name = 'fishzz'
print(s.name)
s.set_score(60)
print(s.get_score())
s.set_score(100)
