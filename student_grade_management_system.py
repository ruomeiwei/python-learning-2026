class Student:
    def __init__(self, name):
        self.name = name 
        self.grades = []
    
    def add_grade(self, grade):
        self.grades.append(grade)
    
    def avg_grade(self):
        if not self.grades:
            return 0 
        return sum(self.grades) / len(self.grades)


class StudentGradeManager:
    def __init__(self):
        self.students = {}
        self

    def add_student(self, name):
        if name not in self.students:
            self.students[name] = Student(name)
        else:
            print(f'{name} is already in the system.')
    
    def get_student(self,name):
        return self.students.get(name)
    
    def add_grade(self, name, grade):
        student = self.get_student(name)
        if student:
            student.add_grade(grade) 
        else: 
            return "Student doesn't exist" 
    def show_avg_grade(self):
        for name, student in self.students.items():
            print(name, student.avg_grade())

manager = StudentGradeManager() 
manager.add_student('bingbing')
manager.add_student('susu')
manager.add_student('ziyi')

manager.add_grade('bingbing', 90)
manager.add_grade('susu', 80)

manager.show_avg_grade()