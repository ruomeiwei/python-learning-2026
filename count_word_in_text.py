word_count = {}

with open('BeginnerGuideToPython.txt', 'r', encoding='utf-8') as f:
    words = []
    for line in f.readlines():
        line = line[:-1]
        words.append(line.split())
        if words:
            for word in words: 
                if word not in word_count:
                    word_count[word] = 1
                else:
                    word_count[word] += 1
print(sorted(word_count.items(), key = lambda x: x[1], reverse=True)[:10])
