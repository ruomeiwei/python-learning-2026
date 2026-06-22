course_grade = {}

with open('course_student_grade.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        line = line[:-1]
        course, sid, name, grade = line.split(',')
        if course not in course_grade:
            course_grade[course] = []
        course_grade[course].append(float(grade)) 


for course, grade in course_grade.items():
    print(f"For {course}, max grade is {max(grade):.2f}, min grade is {min(grade):.2f}, avg grade is {sum(grade)/len(grade):.2f}")
