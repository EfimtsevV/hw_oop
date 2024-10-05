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
student_2.finished_courses += ['C++']
student_3.finished_courses += ['JS']

mentor_1 = Lecturer('Ivan', 'Zaharov')
mentor_2 = Reviewer('Petya', 'Popov')
mentor_3 = Reviewer('Anton', 'Kozlov')
mentor_4 = Lecturer('Petya', 'Pavlov')

mentor_1.courses_attached += ['Python']
mentor_1.courses_attached += ['Git']
mentor_2.courses_attached += ['Python']
mentor_2.courses_attached += ['Git']
mentor_3.courses_attached += ['Python']
mentor_3.courses_attached += ['Git']
mentor_4.courses_attached += ['Python']

mentor_2.rate_hw(student_1, 'Python', 10)
mentor_2.rate_hw(student_2, 'Python', 9)
mentor_2.rate_hw(student_3, 'Python', 5)
mentor_2.rate_hw(student_1, 'Git', 10)
mentor_2.rate_hw(student_2, 'Git', 7)

mentor_3.rate_hw(student_1, 'Python', 7)
mentor_3.rate_hw(student_2, 'Python', 10)
mentor_3.rate_hw(student_3, 'Python', 8)
mentor_3.rate_hw(student_1, 'Git', 6)
mentor_3.rate_hw(student_2, 'Git', 9)


student_1.rate_lecturer(mentor_1, 'Python', 10)
student_1.rate_lecturer(mentor_1, 'Git', 9)
student_1.rate_lecturer(mentor_4, 'Python', 10)

student_2.rate_lecturer(mentor_1, 'Python', 10)
student_2.rate_lecturer(mentor_1, 'Git', 9)
student_2.rate_lecturer(mentor_4, 'Python', 4)

student_3.rate_lecturer(mentor_1, 'Python', 10)
student_3.rate_lecturer(mentor_4, 'Python', 8)



# Задание 1-2 

#Оценки студентов
print(student_1.grades)
print(student_2.grades)
print(student_3.grades)

#Оценки лекторов
print(mentor_1.grades)
print(mentor_4.grades)

#Задание 3(1 пункт) - добавление __str__
print(mentor_1)
print(mentor_2)
print(mentor_3)
print(mentor_4)

print(student_1)
print(student_2)
print(student_3)

#Задание 3(2 пункт) - сравнение ср оценки

print(Lecturer.comparison_avg(mentor_1, mentor_4))

print(Student.comparison_avg(student_1, student_2))
print(Student.comparison_avg(student_1, student_3))
print(Student.comparison_avg(student_2, student_3))
 
 #4 задание 
 
avg_grade_student_py = Student.average_grade_for_course(Student.collect_all_students(student_1, student_2, student_3), 'Python')
avg_grade_student_git = Student.average_grade_for_course(Student.collect_all_students(student_1, student_2, student_3), 'Git')

print(f'Средняя оценка студентов за дз на курсе Python: {avg_grade_student_py} \n')
print(f'Cредняя оценка студентов за дз на курсе Git: {avg_grade_student_git}\n')

avg_grade_lecturer_py = Lecturer.average_grade_for_course(Lecturer.collect_all_lecturers(mentor_1, mentor_4), 'Python')
avg_grade_student_git = Lecturer.average_grade_for_course(Lecturer.collect_all_lecturers(mentor_1, mentor_4), 'Git')

print(f'Средняя оценка лекторов за лекции на курсе Python: {avg_grade_lecturer_py} \n')
print(f'Срнедняя оценка лекторов за лекции на курсе Git: {avg_grade_student_git} \n')

