class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.mid_grade = []

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer_name, course_name, grade):
        if isinstance(lecturer_name, Lecturer) and course_name in lecturer_name.courses_attached and course_name in self.courses_in_progress:
            if course_name in lecturer_name.grades:
                lecturer_name.grades[course_name] += [grade]
            else:
                lecturer_name.grades[course_name] = [grade]
        else:
            return 'Ошибка'

    def _middle_grade(self):
        self.mid_grade = sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), []))
        return self.mid_grade

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Невозможно сравнить!')
            return
        return self.mid_grade < other.mid_grade

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекцию: {self._middle_grade()}\n'
                f'Курсы в процессе изучения: {",".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {",".join(self.finished_courses)}\n')

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.mid_grade = []

    def _middle_grade(self):
        self.mid_grade = sum(sum(self.grades.values(),[]))/len(sum(self.grades.values(),[]))
        return self.mid_grade

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Невозможно сравнить!')
            return
        return self.mid_grade < other.mid_grade

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекцию: {self._middle_grade()}\n'
                )


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'Имя: {self.name}\n'
             f'Фамилия: {self.surname}\n')


first_lecturer = Lecturer('Some','Buddy')
first_lecturer.courses_attached += ['Python']

second_lecturer = Lecturer('Vasya','Buddy')
second_lecturer.courses_attached += ['Python']
'///////////////////////////////////////////'

first_student = Student('Dima', 'Gor', 'man')
first_student.courses_in_progress += ['Python']
first_student.finished_courses += ['Введение в программирование']
first_student.rate_lecturer(first_lecturer, 'Python', 9.9)
first_student.rate_lecturer(second_lecturer, 'Python', 7.9)

second_student = Student('Vadim', 'Gor', 'man')
second_student.courses_in_progress += ['Python']
second_student.finished_courses += ['Введение в программирование']
second_student.rate_lecturer(first_lecturer, 'Python', 7.9)
second_student.rate_lecturer(second_lecturer, 'Python', 4.9)


'///////////////////////////////////////////'

first_reviewer = Reviewer('Victor', 'Oladipo')
first_reviewer.courses_attached += ['Python']

first_reviewer.rate_hw(first_student, 'Python', 9)
first_reviewer.rate_hw(first_student, 'Python', 9)
first_reviewer.rate_hw(first_student, 'Python', 9)
first_reviewer.rate_hw(second_student, 'Python', 4)
first_reviewer.rate_hw(second_student, 'Python', 4)
first_reviewer.rate_hw(second_student, 'Python', 4)


def grade_av(students_list, course):
    sum_of_grades = 0
    counter = 0
    for student in students_list:
        for grade in student.grades[course]:
            sum_of_grades += grade
            counter += 1
    return sum_of_grades/counter

def grades_lect(lecturers_list, course):
    sum_of_grades = 0
    counter = 0
    for lector in lecturers_list:
        for grade_lector in lector.grades[course]:
            sum_of_grades += grade_lector
            counter += 1
    return sum_of_grades/counter

print(first_reviewer)

print(first_student)
print(second_student)


print(second_student < first_student)

print(first_lecturer)
print(second_lecturer)
print(second_lecturer < first_lecturer)

students_list = [first_student, second_student]
lecturers_list = [first_lecturer, second_lecturer]

print(f'Средняя оценка всех учащихся на курсе Python {grade_av(students_list,"Python")}')
print(f'Средняя оценка всех преподавателей на курсе Python {grades_lect(lecturers_list, "Python")}')