class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Нельзя сравнить')
        return self.get_average() < other.get_average()

    def get_average(self):
        average_grade_list = []
        for key, value in self.grades.items():
            average_grade_list.extend(value)
        result = round(sum(average_grade_list) / len(average_grade_list), 1)
        return result

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Завершенные курсы: {self.finished_courses}\n' \
              f'Курсы в процессе изучения: {self.courses_in_progress}\n' \
              f'Средняя оценка за домашние задания:{self.get_average()} \n'
        return res

    def rate_hw(self, lector, course, grade):
        if isinstance(lector,
                      Lector) and course in self.courses_in_progress and course in lector.courses_attached and 1 <= grade <= 10:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student,
                      Student) and course in self.courses_attached and course in student.courses_in_progress and 1 <= grade <= 10:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lector(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}
        self.average_grade = [5]

    def __lt__(self, other):
        if not isinstance(other, Lector):
            print('Нельзя сравнить')
        return Student.get_average(self) < Student.get_average(other)

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Ведет курсы: {self.courses_attached}\n' \
              f'Средняя оценка за лекции: {Student.get_average(self)} '
        return res

    def rate_hw(self, student, course, grade):
        print('Лектор не может ставить оценки')


class Reviewer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        grade = int() in range(1, 10)

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}'
        return res


# Создаем 2 студента
best_student = Student('Ruoy', 'Eman', 'x')
best_student.courses_in_progress += ['Python', 'GIT', 'C++']
best_student.finished_courses += ['Brainfuck']

not_best_student = Student('Egor', 'Letov', 'm')
not_best_student.courses_in_progress += ['Python', 'GIT', 'C++']
not_best_student.finished_courses += ['Brainfuck']

# Создаем 2 лектора
cool_lector = Lector('SomeL', 'BuddyL')
cool_lector.courses_attached += ['Python', 'GIT', 'css']

not_cool_lector = Lector('Svidetel', 'Is_Fryazino')
not_cool_lector.courses_attached += ['Python', 'GIT']

# Создаем 2 ревьюера
cool_reviewer = Reviewer('SomeR', 'BuddyR')
cool_reviewer.courses_attached += ['GIT', 'Python']
not_cool_reviewer = Reviewer('Mikle', 'Moor')
not_cool_reviewer.courses_attached += ['GIT', 'Python']

# Выставляем оценки студентами , правильные и не правильные(не в рамках 1-10, по курсу который не проходился)
best_student.rate_hw(cool_lector, 'Python', 1)
best_student.rate_hw(cool_lector, 'Python', 12)
best_student.rate_hw(cool_lector, 'GIT', 14)
best_student.rate_hw(cool_lector, 'GIT', 7)
best_student.rate_hw(cool_lector, 'C++', 7)
best_student.rate_hw(cool_lector, 'css', 7)
best_student.rate_hw(cool_lector, 'Python', 1)
best_student.rate_hw(cool_lector, 'Python', 9)
best_student.rate_hw(cool_lector, 'GIT', 8)
best_student.rate_hw(cool_lector, 'GIT', 6)
not_best_student.rate_hw(not_cool_lector, 'Python', 1)
not_best_student.rate_hw(not_cool_lector, 'Python', 3)
best_student.rate_hw(not_cool_lector, 'Python', 5)
best_student.rate_hw(not_cool_lector, 'GIT', 3)
best_student.rate_hw(not_cool_lector, 'GIT', 1)
# Выставляем оценки Ревьюерами
cool_reviewer.rate_hw(best_student, 'GIT', 1)
cool_reviewer.rate_hw(best_student, 'GIT', 15)
cool_reviewer.rate_hw(best_student, 'GIT', 9)
cool_reviewer.rate_hw(not_best_student, 'GIT', 5)
cool_reviewer.rate_hw(not_best_student, 'GIT', 2)
cool_reviewer.rate_hw(not_best_student, 'Python', 1)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 18)
cool_reviewer.rate_hw(not_best_student, 'Python', 2)
# Попытка лектором поставить оценку
cool_lector.rate_hw(best_student, 'Python', 10)

# Dsdjl информации о студенте по образцу
print(best_student)
print((not_best_student))
# Вывод информации о Лекторах по образцу
print(cool_lector)
print(not_cool_lector)
# Вывод сравнения лекторов кто лучше и студентов кто лучше
print(best_student > not_best_student)
print(cool_lector > not_cool_lector)

# Создали две функции , одна по лекторам, вторая по студентам, выводящие информацию о сраедней по всем, по курсу
incom_students_list = [best_student, not_best_student]
incom_lectors_list = [cool_lector, not_cool_lector]
incom_course = 'Python'


def get_average_grade_course_lectors(income_list, income_course):
    common_grades = []
    for lectors in incom_lectors_list:
        for value in lectors.grades.values():
            common_grades.extend(lectors.grades[incom_course])
    print(f'По курсу {incom_course} средняя оценка лекторов: {round(sum(common_grades) / len(common_grades),1)} ')
    return


def get_average_grade_course_students(income_students_list, income_course):
    common_grades = []
    for students in incom_students_list:
        for value in students.grades.values():
            common_grades.extend(students.grades[incom_course])
    print(f'По курсу {incom_course} средняя оценка студентов: {sum(common_grades) / len(common_grades)} ')
    return

#Вызываем эти функции
get_average_grade_course_lectors(incom_lectors_list, incom_course)
get_average_grade_course_students(incom_students_list, incom_course)
