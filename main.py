from src.Classes import Student
from src.Classes import Mentor
from src.Classes import Lecturer
from src.Classes import Reviewer



student_1 = Student('Masha', 'Begovaya', 'Woman')
student_2 = Student('Vasya', 'Ostrov', 'Man')
student_3 = Student('Vlad', 'Chesnov', 'Man')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Git']
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Git']
student_3.courses_in_progress += ['Python']

student_1.finished_courses += ['SQL']

mentor_1 = Lecturer('Ivan', 'Zaharov')
mentor_2 = Reviewer('Petya', 'Popov')
mentor_3 = Reviewer('Anton', 'Kozlov')

# mentor_1.courses_attached += ['Python']
# mentor_1.courses_attached += ['Git']
# mentor_2.courses_attached += ['Python']
# mentor_2.courses_attached += ['Git']
# mentor_3.courses_attached += ['Python']
# mentor_3.courses_attached += ['Git']

# mentor_2.rate_hw(student_1, 'Python', 10)
# mentor_2.rate_hw(student_2, 'Python', 9)
# mentor_2.rate_hw(student_3, 'Python', 5)
# mentor_2.rate_hw(student_1, 'Git', 10)
# mentor_2.rate_hw(student_2, 'Git', 7)

# mentor_3.rate_hw(student_1, 'Python', 7)
# mentor_3.rate_hw(student_2, 'Python', 10)
# mentor_3.rate_hw(student_3, 'Python', 8)
# mentor_3.rate_hw(student_1, 'Git', 6)
# mentor_3.rate_hw(student_2, 'Git', 9)


student_1.rate_lecturer(mentor_1, 'Python', 10)
student_1.rate_lecturer(mentor_1, 'Git', 9)

student_2.rate_lecturer(mentor_1, 'Python', 10)
student_2.rate_lecturer(mentor_1, 'Git', 9)

student_3.rate_lecturer(mentor_1, 'Python', 10)

# print(student_1.grades)
# print(student_2.grades)
# print(student_3.grades)



print(mentor_1.grades)


