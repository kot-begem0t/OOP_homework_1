class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and\
        (self.courses_in_progress or self.finished_courses):
            if grade <= 10:
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
            else:
                return 'Максимальная оценка не может быть больше 10'
        else:
            return 'Ошибка'

    # Average grade for all courses
    def aver_grade_homework(self, grades):
        count = 0
        for course in grades:
            for grade in grades[course]:
                count += grade
        if count > 0:
            return count / len(grades)
        else:
            return "Оценок нет"

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n'\
        f'Средняя оценка за домашние задания: {self.aver_grade_homework(self.grades)}\n'\
        f'Курсы в процессе изучения: {", ".join(self.courses_in_progress) if len(self.courses_in_progress) != 0 else "отсутствуют"}\n'\
        f'Завершенные курсы: {", ".join(self.finished_courses) if len(self.finished_courses) != 0 else "отсутствуют"}'

    # Operators
    def __gt__(self, other):
        # Terms. If object has class Student and it has type int or float and average is more 0
        if isinstance(other, Student) and\
        (type(other.aver_grade_homework(other.grades)) == int or float) and\
        other.aver_grade_homework(other.grades) > 0:
            return self.aver_grade_homework(self.grades) > other.aver_grade_homework(other.grades)
        else:
            return 'Ошибка'
    def __lt__(self, other):
        # Terms. If object has class Student and it has type int or float and average is more 0
        if isinstance(other, Student) and (type(other.aver_grade_homework(other.grades)) == int or float)\ 
        and other.aver_grade_homework(other.grades) > 0:
            return self.aver_grade_homework(self.grades) < other.aver_grade_homework(other.grades)
        else:
            return 'Ошибка'
    def __eq__(self, other):
        # Terms. If object has class Student and it has type int or float and average is more 0
        if isinstance(other, Student) and (type(other.aver_grade_homework(other.grades)) == int or float) and\ 
        other.aver_grade_homework(other.grades) > 0:
            return self.aver_grade_homework(self.grades) == other.aver_grade_homework(other.grades)
        else:
            return 'Ошибка'
    def __ne__(self, other):
        # Terms. If object has class Student and it has type int or float and average is more 0
        if isinstance(other, Student) and (type(other.aver_grade_homework(other.grades)) == int or float) and\ 
        other.aver_grade_homework(other.grades) > 0:
            return self.aver_grade_homework(self.grades) != other.aver_grade_homework(other.grades)
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    # I left this method if it needs future
    # def rate_hw(self, student, course, grade):
    #     if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
    #         if course in student.grades:
    #             student.grades[course] += [grade]
    #         else:
    #             student.grades[course] = [grade]
    #     else:
    #         return 'Ошибка'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    # Average grade for all courses
    def aver_grade_lect(self, grades):
        count = 0
        for course in grades:
            for grade in grades[course]:
                count += grade
        if count > 0:
            return count / len(grades)
        else:
            return "Оценок нет"

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.aver_grade_lect(self.grades)}'

    # Operators
    def __gt__(self, other):
        # Terms. If object has class Lecturer and it has type int or float and average is more 0
        if isinstance(other, Lecturer) and (type(other.aver_grade_lect(other.grades)) == int or float) and\
        other.aver_grade_lect(other.grades) > 0:
            return self.aver_grade_lect(self.grades) > other.aver_grade_lect(other.grades)
        else:
            return 'Ошибка'
    def __lt__(self, other):
        # Terms. If object has class Lecturer and it has type int or float and average is more 0
        if isinstance(other, Lecturer) and (type(other.aver_grade_lect(other.grades)) == int or float) and\
        other.aver_grade_lect(other.grades) > 0:
            return self.aver_grade_lect(self.grades) < other.aver_grade_lect(other.grades)
        else:
            return 'Ошибка'
    def __eq__(self, other):
        # Terms. If object has class Lecturer and it has type int or float and average is more 0
        if isinstance(other, Lecturer) and (type(other.aver_grade_lect(other.grades)) == int or float) and\
        other.aver_grade_lect(other.grades) > 0:
            return self.aver_grade_lect(self.grades) == other.aver_grade_lect(other.grades)
        else:
            return 'Ошибка'
    def __ne__(self, other):
        # Terms. If object has class Lecturer and it has type int or float and average is more 0
        if isinstance(other, Lecturer) and (type(other.aver_grade_lect(other.grades)) == int or float) and\
        other.aver_grade_lect(other.grades) > 0:
            return self.aver_grade_lect(self.grades) != other.aver_grade_lect(other.grades)
        else:
            return 'Ошибка'


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if grade <= 10:
                if course in student.grades:
                    student.grades[course] += [grade]
                else:
                    student.grades[course] = [grade]
            else:
                return 'Максимальная оценка не может быть больше 10'
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


def average_grade_for_students(list, course):
    """Function count average grade for students one of course"""
    count_grade = 0
    count_student = 0
    for student in list:
        if course in student.grades:
            count_student = count_student + 1
            count = 0
            for i in student.grades[course]:
                count += i
            count_grade += count / len(student.grades[course])
    return f'Средння оценка студентов по курсу {course} - {count_grade / count_student}'


def aver_grade_lectrs(list, course):
    """Function count average grade for lecturers one of course"""
    count_grade = 0
    count_lecturers = 0
    for lecturer in list:
        if course in lecturer.grades:
            count_lecturers = count_lecturers + 1
            count = 0
            for i in lecturer.grades[course]:
                count += i
            count_grade += count / len(lecturer.grades[course])
    return f'Средння оценка лекторов по курсу {course} - {count_grade / count_lecturers}'


# Quiz
# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python']
#
# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
#
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
#
# print(best_student.grades)
#
#
# Exercise 1
# lecturer = Lecturer('Иван', 'Иванов')
# reviewer = Reviewer('Пётр', 'Петров')
# print(isinstance(lecturer, Mentor))
# print(isinstance(reviewer, Mentor))
# print(lecturer.courses_attached)
# print(reviewer.courses_attached)
#
#
# Exercise 2
# lecturer = Lecturer('Иван', 'Иванов')
# reviewer = Reviewer('Пётр', 'Петров')
# student = Student('Алёхина', 'Ольга', 'Ж')
#
# student.courses_in_progress += ['Python', 'Java']
# lecturer.courses_attached += ['Python', 'C++']
# reviewer.courses_attached += ['Python', 'C++']
#
# print(student.rate_lecture(lecturer, 'Python', 7))
# print(student.rate_lecture(lecturer, 'Java', 8))
# print(student.rate_lecture(lecturer, 'С++', 8))
# print(student.rate_lecture(reviewer, 'Python', 6))
#
# print(lecturer.grades)
#
#
# Exercise 3
# reviewer = Reviewer('Пётр', 'Петров')
# student = Student('Алёхина', 'Ольга', 'Ж')
# lecturer = Lecturer('Иван', 'Иванов')
#
# student.courses_in_progress += ['Python', 'Java', 'С++', 'C']
# lecturer.courses_attached += ['Python', 'Java', 'С++', 'C']
# reviewer.courses_attached += ['Python', 'Java', 'С++', 'C', 'Ruby']
#
# student.rate_lecture(lecturer, 'Python', 7)
# student.rate_lecture(lecturer, 'Python', 9)
# student.rate_lecture(lecturer, 'Java', 8)
# student.rate_lecture(lecturer, 'С++', 4)
# student.rate_lecture(lecturer, 'C', 6)
#
# reviewer.rate_hw(student, 'Python', 4)
# reviewer.rate_hw(student, 'Java', 9)
# reviewer.rate_hw(student, 'C++', 9)
# reviewer.rate_hw(student, 'C', 2)
# reviewer.rate_hw(student, 'Ruby', 3)
#
# print(reviewer)
# print()
# print(lecturer)
# print()
# print(student)
# print()
# print(student.aver_grade_homework(student.grades))
# print(lecturer.aver_grade_lect(lecturer.grades))
#
#
# Exercise 4
# Made objects of classes
lecturer_1 = Lecturer('Иван', 'Иванов')
lecturer_2 = Lecturer('Василий', 'Васильев')
reviewer_1 = Reviewer('Пётр', 'Петров')
reviewer_2 = Reviewer('Александр', 'Александров')
student_1 = Student('Алёхина', 'Ольга', 'Ж')
student_2 = Student('Ольгин', 'Алексей', 'М')

# Added courses for objects
student_1.courses_in_progress += ['Python', 'Java']
student_2.courses_in_progress += ['С++', 'C']
student_1.finished_courses += ['C++']
student_2.finished_courses += ['Python']
lecturer_1.courses_attached += ['Python', 'С++']
lecturer_2.courses_attached += ['Java', 'C']
reviewer_1.courses_attached += ['Python', 'C', 'Ruby']
reviewer_2.courses_attached += ['Java', 'С++']

# Added grades for students and lecturers and check rate
student_1.rate_lecture(lecturer_1, 'Python', 7)
student_1.rate_lecture(lecturer_1, 'Java', 8)
student_1.rate_lecture(lecturer_1, 'С++', 4)
student_1.rate_lecture(lecturer_1, 'C', 6)
student_1.rate_lecture(lecturer_2, 'Python', 9)
student_1.rate_lecture(lecturer_2, 'Java', 8)
student_1.rate_lecture(lecturer_2, 'С++', 4)
student_1.rate_lecture(lecturer_2, 'C', 6)
student_2.rate_lecture(lecturer_1, 'Python', 4)
student_2.rate_lecture(lecturer_1, 'Java', 3)
student_2.rate_lecture(lecturer_1, 'С++', 1)
student_2.rate_lecture(lecturer_1, 'C', 8)
student_2.rate_lecture(lecturer_2, 'Python', 3)
student_2.rate_lecture(lecturer_2, 'Java', 2)
student_2.rate_lecture(lecturer_2, 'С++', 9)
student_2.rate_lecture(lecturer_2, 'C', 9)

reviewer_1.rate_hw(student_1, 'Python', 4)
reviewer_1.rate_hw(student_1, 'Java', 9)
reviewer_1.rate_hw(student_1, 'C++', 9)
reviewer_1.rate_hw(student_1, 'C', 2)
reviewer_1.rate_hw(student_1, 'Ruby', 3)
reviewer_1.rate_hw(student_2, 'Python', 4)
reviewer_1.rate_hw(student_2, 'Java', 9)
reviewer_1.rate_hw(student_2, 'C++', 9)
reviewer_1.rate_hw(student_2, 'C', 2)
reviewer_1.rate_hw(student_2, 'Ruby', 3)
reviewer_2.rate_hw(student_1, 'Python', 8)
reviewer_2.rate_hw(student_1, 'Java', 4)
reviewer_2.rate_hw(student_1, 'C++', 9)
reviewer_2.rate_hw(student_1, 'C', 3)
reviewer_2.rate_hw(student_1, 'Ruby', 5)
reviewer_2.rate_hw(student_2, 'Python', 5)
reviewer_2.rate_hw(student_2, 'Java', 5)
reviewer_2.rate_hw(student_2, 'C++', 6)
reviewer_2.rate_hw(student_2, 'C', 7)
reviewer_2.rate_hw(student_2, 'Ruby', 8)

# Check method __str__
print(reviewer_1)
print(reviewer_2)
print()
print(lecturer_1)
print(lecturer_2)
print()
print(student_1)
print(student_2)
print()

# check ==,>,<
print(student_1 > student_2)
print(student_1 < student_2)
print(student_1 == student_2)
print()
print(lecturer_1 < lecturer_2)
print(lecturer_1 > lecturer_2)
print(lecturer_1 == lecturer_2)

# check function count average grade for students one of course
student_2.grades['Python'] = [10, 10, 10]
list_stud = [student_1, student_2]
print()
print(student_1.grades)
print(student_2.grades)
print(average_grade_for_students(list_stud, 'Python'))

# check function count average grade for lecturers one of course
lecturer_2.grades['Python'] = [10, 10, 10]
list_lect = [lecturer_1, lecturer_2]
print()
print(lecturer_1.grades)
print(lecturer_2.grades)
print(aver_grade_lectrs(list_lect, 'Python'))