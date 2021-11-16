from class_text_20211115 import text
from class_vocabulary_item_20211115 import vocabulary_item
import os

d0 = r'.\data'
file_name = 'pride_and_prejudice.txt'
file_path = os.path.join(d0, file_name)

t = text()
t.getTextFromFile(file_path)
print(t.sentenses_all)
vocabulary_list = {}
for s in t.sentenses_all:
    print(s)
    punctuation_list = " ,.!?:; \"“”-_\'(){}[]\n#1234567890$+-*/—%’‘"
    for p in punctuation_list:
        s = s.replace(p, ",")
    word_list = s.split(",")
    for word in word_list:
        if word == '':
            continue
        if word not in vocabulary_list:
            vocabulary_list[word] = vocabulary_item(word)
        vocabulary_list[word].add_one_count(s)


import spacy
nlp = spacy.load("en_core_web_sm")
doc = nlp("Apple is looking at buying U.K. startup for")
for token in doc:
    print(token.text, token.pos_, token.dep_)