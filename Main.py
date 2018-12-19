import collections
import pandas as pd
from nltk import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

import nltk

from ReadDOCX import ReadDOCX
from ReadTXT import ReadTXT

ps = PorterStemmer()

#nltk.download('stopwords')
#nltk.download('punkt')

docName = "falkaya.docx"
doc1 = ReadDOCX()
doc1File = doc1.converToTxt(docName)

txtName = "mcganiz.txt"
txt1 = ReadTXT()
txt1File = txt1.readTxt(txtName)


file = open('asd.txt')
txtStr = txt1File.read()
txtStr = txtStr.lower()
docStr = doc1File.read()
docStr = docStr.lower()

# Stopwords
stopwords = set(stopwords.words('english'))
academicStopwords = set(line.strip() for line in open('acStopWords.txt'))
academicStopwords = academicStopwords.union(set(['mr','mrs','one','two','said']))
words = word_tokenize(txtStr) + word_tokenize(docStr)

wordsFiltered = []

for w in words:
    if w not in stopwords and academicStopwords:

        if w.isdigit():
            words.remove(w)

        if '-' not in w:
            w = ps.stem(w)

        wordsFiltered.append(w)

print(wordsFiltered)
wordcount = {}

for word in wordsFiltered:
    if word not in (stopwords and academicStopwords):

        ps.stem(word)
        word = word.replace(".", "")
        word = word.replace(",", "")
        word = word.replace(":", "")
        word = word.replace("\"", "")
        word = word.replace("!", "")
        word = word.replace("â€œ", "")
        word = word.replace("â€˜", "")
        word = word.replace("*", "")

        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1

# Print most common word
n_print = int(input("How many most common words to print: "))
print("\nOK. The {} most common words are as follows\n".format(n_print))
word_counter = collections.Counter(wordcount)
for word, count in word_counter.most_common(n_print):
    print(word, ": ", count)

file.close()
