# Задание № 1. Наследование
#
# Исходя из квиза к предыдущему занятию, у нас уже есть класс преподавателей и класс студентов
# Студентов пока оставим без изменения, а вот преподаватели бывают разные,
#  поэтому теперь класс Mentor должен стать родительским классом,
# а от него нужно реализовать наследование классов Lecturer (лекторы) и Reviewer
# Очевидно, имя, фамилия и список закрепленных курсов логично реализовать на уровне родительского класса.
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

#метод есть у ментора
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
#создаем класс лектора
class Lector(Mentor):
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
#создаем класс проверяющего
class Reviewer(Mentor):
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

print(Reviewer.mro())
print(Lector.mro())

