# #Задание № 2. Атрибуты и взаимодействие классов.
# #
# В квизе к предыдущей лекции мы реализовали возможность выставлять студентам оценки за домашние задания.
# Теперь это могут делать только Reviewer (реализуйте такой метод)!
# А что могут делать лекторы? Получать оценки за лекции от студентов
# Реализуйте метод выставления оценок лекторам у класса Student
# (оценки по 10-балльной шкале, хранятся в атрибуте-словаре у Lecturer,в котором ключи – названия курсов, а значения – списки оценок).
#  Лектор при этом должен быть закреплен за тем курсом, на который записан студент.

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lector,course, grade):
        if isinstance(lector,Lector) and course in self.courses_in_progress and course in lector.courses_attached and grade >=1 and grade<=10:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress and grade >=1 and grade<=10:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:return 'Ошибка'


class Lector(Mentor):
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}

    def rate_hw(self, student, course, grade):
        print('Лектор не может ставить оценки')


class Reviewer(Mentor):
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        grade = int() in range(1, 10)

best_student = Student('Ruoy', 'Eman', 'x')
best_student.courses_in_progress += ['Python','GIT','C++']
cool_lector = Lector('SomeL', 'BuddyL')
cool_lector.courses_attached += ['Python','GIT','css']
cool_reviewer = Reviewer('SomeR', 'BuddyR')
cool_reviewer.courses_attached += ['GIT']


best_student.rate_hw(cool_lector,'Python',1)
best_student.rate_hw(cool_lector,'Python',12)
best_student.rate_hw(cool_lector,'GIT',14)
best_student.rate_hw(cool_lector,'GIT',7)
best_student.rate_hw(cool_lector,'C++',7)
best_student.rate_hw(cool_lector,'css',7)
print('оценки лектора',cool_lector.grades)

cool_reviewer.rate_hw(best_student, 'GIT', 19)
cool_reviewer.rate_hw(best_student, 'GIT', 5)
print('оценки студента',best_student.grades)

cool_lector.rate_hw(best_student,'Python',10)


