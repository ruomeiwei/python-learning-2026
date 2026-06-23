import re 
import pandas as pd

with open('BeginnerGuideToPython.txt', 'r', encoding='uft-8') as f:
    content = f.read()

words = re.split(r'[\s?!\.;,()/]+', content)

words_series = pd.Series(words)

top20_words = words_series.value_counts()[:20]