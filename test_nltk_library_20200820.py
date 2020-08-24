#
# import nltk
# nltk.download()
from nltk.book import *
import nltk

len(text3)
sorted(set(text3))
len(set(text3))
len(set(text3)) / len(text3)
text3.count("smote")
100 * text4.count('a') / len(text4)


fdist1 = FreqDist(text1)
print(fdist1)
fdist1.most_common(50)

V = set(text1)
long_words = [w for w in V if len(w) > 15]
sorted(long_words)

fdist5 = FreqDist(text5)
sorted(w for w in set(text5) if len(w) > 7 and fdist5[w] > 7)


list(bigrams(['more', 'is', 'said', 'than', 'done']))
text4.collocations()
fdist = FreqDist(len(w) for w in text1)

text_vocab = set(w.lower() for w in text1 if w.isalpha())



