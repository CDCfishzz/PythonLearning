# -*- coding: utf-8 -*-
# 单元测试


class Dict(dict):
    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError("'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score < 0 or self.score > 100:
            raise ValueError("score must be between 0 and 100")
        if self.score >= 80:
            return 'A'
        if self.score >= 60:
            return 'B'
        return 'C'
