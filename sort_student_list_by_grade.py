students = [
    {'sno': 101, 'sname': 'Alice', 'grade': 85},
    {'sno': 102, 'sname': 'Bob', 'grade': 92},
    {'sno': 103, 'sname': 'Charlie', 'grade': 78},
    {'sno': 104, 'sname': 'David', 'grade': 90},
]

sorted_students = sorted(students, key=lambda x: x['grade'], reverse=True)

print(sorted_students)