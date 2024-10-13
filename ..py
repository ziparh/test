class Student:
    
    def __init__(self, skill = 'math', age = '15', work = 'study'):
        self.skill = skill
        self.age = age
        self.work = work

    def studing(self):
        print("Студент учится")
    def sleeping(self):
        print('Студент спит')
    def eating(self):
        print('Студент ест')

    def info(self):
        print(f"Студент хорошо умеет:, {self.skill}")
        print(f"Студену {self.age} лет")
        print(f"Студент сейчас: {self.work}")
student = Student()
student.info()