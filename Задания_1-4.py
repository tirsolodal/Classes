class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def grade_lec(self, lecturer, course, grade):  
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"

    def aver_grad(self):  
        sum_ = 0
        len_ = 0
        for course in self.grades.values():   
            sum_ += sum(course)
            len_ += len(course)
        average = round(sum_ / len_, 2)
        return average   
 
    def __str__(self):
        res = f'Имя: {self.name}\n' f'Фамилия: {self.surname}\n' f'Средняя оценка за домашние задания: {self.aver_grad()}\n' f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' f'Завершенные курсы: {", ".join(self.finished_courses)}'
        return res
    
    def average_for_all(self, course):
        sum_ = 0
        len_ = 0
        for lesson in self.grades.keys():  
            if lesson == course:   
                sum_ += sum(self.grades[course])  
                len_ += len(self.grades[course])
        average = round(sum_ / len_, 2)
        return average 
    
    def __lt__(self, other):
             if not isinstance(other, Student):
                 print("Error")
                 return
             return self.average() < other.average()



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
   def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {} 


   def av_for_lect(self):
        sum_ = 0
        len_ = 0
        for course in self.grades.values():   
            sum_ += sum(course)
            len_ += len(course)
        average = round(sum_ / len_, 2)
        return average


   def average_for_all(self, course):
        sum_ = 0
        len_ = 0
        for lesson in self.grades.keys():
            if lesson == course:
                sum_ += sum(self.grades[course])
                len_ += len(self.grades[course])
        average = round(sum_ / len_, 2)
        return average   
   
   def __str__(self):
        res = f'Имя: {self.name}\n' f'Фамилия: {self.surname}\n' f'Средняя оценка за лекции: {self.av_for_lect()}\n' 
        return res

   def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Error")
            return
        return self.average() < other.average()

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress: 
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res



student_1 = Student('Nick', 'Mad')
student_1.courses_in_progress += ['C++']
student_1.finished_courses += ["Java"]

student_2 = Student('Sam', 'Nil')
student_2.courses_in_progress += ['Java']
student_2.finished_courses += ["C++"]

lecturer_1 = Lecturer('Stiv', 'Hocing')
lecturer_1.courses_attached += ['Java']
 
lecturer_2 = Lecturer('Stiv', 'Jobs')
lecturer_2.courses_attached += ['C++']

reviewer_1 = Reviewer('Jek', 'Nicolson')
reviewer_1.courses_attached += ['C++']
 
reviewer_2 = Reviewer('Alex', 'Red')
reviewer_2.courses_attached += ['Java']

# Наполняем словарь оценок у студентов
reviewer_1.rate_hw(student_1, 'C++', 4)
reviewer_2.rate_hw(student_2, 'Java', 6)
# Наполняем словарь оценок у лекторов
student_1.grade_lec(lecturer_1, 'Java', 5)
student_1. grade_lec(lecturer_1, 'Java', 1)


student_2.grade_lec(lecturer_2, 'C++', 8)
student_2.grade_lec(lecturer_2, 'C++', 2)

stud_list = [student_1, student_2]
lect_list = [lecturer_1, lecturer_2]

def average_for_all(course, stud_list):
    summ = 0
    step = 0
    for stud in stud_list:
        for course in stud.grades:
            course_sum = stud.average_for_all(course)
            summ += course_sum
            step += 1
    average = round(summ / step, 2)
    return average
  
    
print(average_for_all('Java', stud_list))
print(average_for_all('C++', lect_list))
 
print(student_1)
print(student_2)

print(lecturer_1)
print(lecturer_2)

print(reviewer_1)
print(reviewer_2)