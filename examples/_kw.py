class Person(object):
    def __init__(self, name, gender, birth, **kw):
        self.name = name
        self.gender = gender
        self.birth = birth
        self.job = ''
        for k, v in kw.items():
            setattr(self, k, v)


xiaoming = Person('Xiao Ming', 'Male', '1990-1-1', job='Student', job2='hhh')
print(xiaoming.name)
print(xiaoming.job)
print(xiaoming.job2)
