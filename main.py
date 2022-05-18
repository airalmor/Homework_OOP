#исходный код
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


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


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

print(best_student.grades)



# class Student:
#     def __init__(self, name, surname, gender):
#         self.name = name
#         self.surname = surname
#         self.gender = gender
#         self.finished_courses = []
#         self.courses_in_progress = []
#         self.grades = {}
#
#     def rate_hw(self, lecturer, course, grade):
#         if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
#             if course in lecturer.grades:
#                 lecturer.grades[course] += [grade]
#             else:
#                 lecturer.grades[course] = [grade]
#         else:
#             print('ошибка')
#             return
#
#     def __str__(self):
#         res = f'Имя: {self.name}\n' \
#               f'Фамилия: {self.surname}\n' \
#               f'Курсы в процессе изучения: {self.courses_in_progress}\n' \
#               f'Средняя оценка '
#         return res
#
#
# class Mentor:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#         self.courses_attached = []
#
#     def rate_hw(self, student, course, grade):
#         if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
#             if course in student.grades:
#                 student.grades[course] += [grade]
#             else:
#                 student.grades[course] = [grade]
#         else:
#             return 'Ошибка'
#
#         def __str__(self):
#             res = f'Имя: {self.name}\nФамилия: {self.surname}\nКурсы в базе: {self.courses_attached}'
#             return res
#
# class Lecturer(Mentor):
#     def __init__(self, name, surname):
#         super().__init__(name,surname)
#         self.grades = {}
#     def __str__(self):
#         res = f'Имя: {self.name}\nФамилия: {self.surname}\nПреподает курсы : {self.courses_attached}'
#         return res
#
#
#
# class Reviewer(Mentor):
#     def __init__(self, name, surname):
#         super().__init__(name, surname)
#         self.courses_attached=[]
#
#     def __str__(self):
#         res = f'Имя: {self.name}\nФамилия: {self.surname}\nПроверяет курсы: {self.courses_attached}'
#         return res
#
#
#     def rate_hw(self, student, course, grade):
#         if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
#             if course in student.grades:
#                 student.grades[course] += [grade]
#             else:
#                 student.grades[course] = [grade]
#         else:
#             return 'Ошибка'
# mentor_1 = Mentor('name','surname')
# student_1 = Student('Alex', 'Morozov', 'm')
# student_2 = Student('Tatiana','Manko','f')
# student_1.courses_in_progress = ['python']
# student_2.courses_in_progress = ['git']
#
# lecturer_1 = Lecturer('Oleg', 'Ivanov')
# lecturer_2 = Lecturer('Ivan','Olegov')
# lecturer_1.courses_attached += ['python','postgres']
# lecturer_2.courses_attached += ['git','sql']
# reviewer_1 = Reviewer('Alena','Fetisova')
# reviewer_2 = Reviewer('Petr','Kazantsev')
# reviewer_1.courses_attached=['python','git']
# reviewer_2.courses_attached=['git','python']
#
#
# student_1.rate_hw(lecturer_1, 'python', 8)
# student_1.rate_hw(lecturer_1, 'postgres', 8)
# student_1.rate_hw(lecturer_1, 'python', 6)
# student_1.rate_hw(lecturer_2, 'git', 10)
# student_1.rate_hw(lecturer_2, 'sql', 9)
# student_2.rate_hw(lecturer_1, 'python', 7)
# student_2.rate_hw(lecturer_1, 'postgres', 7)
# student_2.rate_hw(lecturer_2, 'sql', 7)
# student_2.rate_hw(lecturer_2, 'git', 2)
#
#
# reviewer_1.rate_hw(student_1, 'python', 7)
# reviewer_1.rate_hw(student_1, 'python', 5)
# reviewer_1.rate_hw(student_1, 'git', 6)
# reviewer_1.rate_hw(student_1, 'git', 8)
# reviewer_2.rate_hw(student_2, 'git', 6)
# reviewer_2.rate_hw(student_2, 'git', 3)
# reviewer_2.rate_hw(student_2, 'python', 3)
# reviewer_2.rate_hw(student_2, 'python', 5)
# reviewer_2.rate_hw(student_2, 'python', 9)
#
# print(student_1.grades.values())
#
#
#
#
# print('-----Студенты------')
# print(student_1)
# print(student_2)
# print('-------Лекторы------')
# print(lecturer_1)
# print(lecturer_2)
# print()
# print('------Проверяющие------')
# print(reviewer_1)
# print(reviewer_2)
# print()
# print('------Mentor------')
# print(mentor_1)

