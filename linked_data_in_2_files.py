
course_teacher = {}


with open('course_teacher.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        line = line[:-1]
        course, teacher = line.split(',')
        course_teacher[course] = teacher

with open('course_student_grade.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        line = line[:-1]
        course, sid, name, grade = line.split(',')
        teacher = course_teacher.get(course)
        print(course, teacher, sid, name, grade)