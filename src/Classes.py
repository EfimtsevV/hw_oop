class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
                
    def average_grade(self):
        total_grades = 0
        total_courses = 0
        for course, grades in self.grades.items():
            total_grades += sum(grades)
            total_courses += len(grades)
        return total_grades / total_courses if total_courses > 0 else 0
    
    def __str__(self) -> str:
        return f"Студент: \nИмя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.average_grade()} \nКурсы в процессе изучения: {', '.join(self.courses_in_progress)} \nЗавершенные курсы: {', '.join(self.finished_courses)}"
    
    def comparison_avg(self, other):
        if isinstance(other, Student):
            if  self.average_grade() > other.average_grade():
                return f"Средняя оценка за дз {self.name} {self.surname} лучше, чем {other.name} {other.surname}"
            elif self.average_grade() < other.average_grade():
                return f"Средняя оценка за дз {self.name} {self.surname} хуже, чем {other.name} {other.surname}"
            else:
                return f"Средняя оценка за дз {self.name} {self.surname} такая же как средняя оценка за дз {other.name} {other.surname}"
    def __lt__(self, other):
        return self.average_grade() < other.average_grade()
    def __eq__(self, other):
        return self.average_grade() == other.average_grade()
    def __gt__(self, other):
        return self.average_grade() > other.average_grade()
           
       
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.all_lecturers = {}
        

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    
        
    def average_grade(self):
        total_grades = 0
        total_courses = 0
        for course, grades in self.grades.items():
            total_grades += sum(grades)
            total_courses += len(grades)
        return total_grades / total_courses if total_courses > 0 else 0
    
    def __str__(self) -> str:
        return f"Лектор: \nИмя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.average_grade()}"
    
    def comparison_avg(self, other):
        if isinstance(other, Lecturer):
            if  self.average_grade() > other.average_grade():
                return f"Средняя оценка за лекции {self.name} {self.surname} лучше, чем {other.name} {other.surname}"
            elif self.average_grade() < other.average_grade():
                return f"Средняя оценка за лекции{self.name} {self.surname} хуже, чем {other.name} {other.surname}"
            else:
                return f"Средняя оценка за лекции {self.name} {self.surname} такая же как средняя оценка за лекции {other.name} {other.surname}"
    def __lt__(self, other):
        return self.average_grade() < other.average_grade()
    def __eq__(self, other):
        return self.average_grade() == other.average_grade()
    def __gt__(self, other):
        return self.average_grade() > other.average_grade()
           
        
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
    def __str__(self) -> str:
        return f"Эксперт, проверяющий домашние задания: \nИмя: {self.name} \nФамилия: {self.surname}"