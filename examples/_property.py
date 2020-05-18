import time
from datetime import datetime


class Student:

    def __init__(self, name, birth=0):
        self.name = name
        self.score = 0
        self.birth = birth

    @property
    def age(self):
        return datetime.now().second - self.birth

    # def set_score(self, new_score):
    #     if not isinstance(new_score, int):
    #         raise ValueError('score must be int')
    #
    #     if 0 <= new_score <= 100:
    #         self.score = new_score
    #         return self.score
    #     else:
    #         raise ValueError('score invalid')

    # 在这里，老师一不小心多打了个9, 通常来说打分都是100分值，999是一个非法数据，不应该赋值成功。学生一多，老师打分出现手误的情况肯定会越来越多，
    # 所以我们必须想办法修改程序，限制score的值必须在0 - 100分。限制值我们定义一个方法，如果输入的不是0 - 100的整数，就让程序报错，数据合法，我们就把score属性修改成功。
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, new_score):
        if not isinstance(new_score, int):
            raise ValueError('score must be int')

        if 0 <= new_score <= 100:
            self._score = new_score
            return self._score
        else:
            raise ValueError('score invalid')


mike = Student('mike')

mike.score = 99

# mike.set_score(99)
print(mike.score)

# 设置属性
mike.score = 88
print(mike.score)

print(mike.birth, mike.age)
time.sleep(5)
print(datetime.now().second)

print(mike.birth, mike.age)
