class Student(object):

    def __init__(self, name, gender, score):
        self.__name = name
        self.__gender = gender
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_grade(self):
        if self.__score > 90:
            return 'A'
        elif self.__score > 60:
            return 'B'
        else:
            return 'C'

    def get_name(self):
        return self.__name

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        if gender == 'male' or gender == 'female':
            self.__gender = gender
        else:
            raise ValueError("Wrong string, only typing \'female\' or \'male\'.")

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('Bad score')


bart = Student('Bart Simpson', 'male', 59)
lisa = Student('Lisa Simpson', 'female', 87)

bart.print_score()
bart.set_gender('male')
print(lisa.get_name(), lisa.get_grade())

if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')