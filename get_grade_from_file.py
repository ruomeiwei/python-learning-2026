def compute_score():
    grade = []
    with open('student_grade.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            line = line[:-1]
            line = line.split(',')
            grade.append(float(line[2]))
    max_grade = max(grade)
    min_grade = min(grade)
    avg_grade = round(sum(grade) / len(grade),2)

    return max_grade, min_grade, avg_grade