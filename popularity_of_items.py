like_count = {}

with open('student_like.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        line = line[:-1]
        name, likes = line.split(' ')
        like_list = likes.split(',')
        for i in like_list:
            if i not in like_count:
                like_count[i] = 1 
            else:
                like_count[i] += 1

print(like_count)
