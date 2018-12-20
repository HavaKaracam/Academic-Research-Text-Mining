import collections
import pandas as pd
from nltk import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import csv

from ReadDOCX import ReadDOCX
from ReadTXT import ReadTXT
from TfCloud import TfCloud
from TfList import TfList
from TfIdf import TfIdf
from ReadPDF import ReadPDF

ps = PorterStemmer()

#nltk.download('stopwords')
#nltk.download('punkt')

docName = "falkaya.docx"
doc1 = ReadDOCX()
doc1File = doc1.converToTxt(docName)
doc1Arr = []

txtName = "mcganiz.txt"
txt1 = ReadTXT()
txt1File = txt1.readTxt(txtName)

pdfName = "fcergin.pdf"
pdf1 = ReadPDF(pdfName)


tfList = TfList()
csvFile1 = tfList.createFile("tf_list.csv")
csvFile2 = tfList.createFile("tf-idf_list.csv")
csvWriter1 = csv.writer(csvFile1, delimiter=',', quotechar='|')
csvWriter2 = csv.writer(csvFile2, delimiter=',', quotechar='|')

tfCloud = TfCloud()

txtStr = txt1File.read()
txtStr = txtStr.lower()
docStr = doc1File.read()
docStr = docStr.lower()

pdfStr = pdf1.convert_pdf_to_txt()
pdfStr.lower()


tfidf = TfIdf()


# Stopwords
stopwords = set(stopwords.words('english'))
academicStopwords = set(line.strip() for line in open('acStopWords.txt'))
academicStopwords = academicStopwords.union(set(['mr','mrs','one','two','said']))
words1 = word_tokenize(txtStr)
words2 = word_tokenize(docStr)
words3 = word_tokenize(pdfStr)

files = [words1, words2, words3]
wordsFiltered = []
wordcount = {}

for file in files:
    filtered = []
    for word in file:

        if word not in stopwords and academicStopwords:
            if word.isdigit():
                continue
            if '-' not in word:
                word = ps.stem(word)
            filtered.append(word)

    wordsFiltered.append(filtered)

print(wordsFiltered)

files = []

for listt in wordsFiltered:
    for word in listt:
        if word not in (stopwords and academicStopwords):

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

    files.append(listt)


# Print most common word
print("\nOK. The 50 most common words are as follows\n")
word_counter = collections.Counter(wordcount)

first50Words = []
for word, count in word_counter.most_common(50):
    csvWriter1.writerow([word, count])
    first50Words.append(word)
    print(word, ": ", count)

idfs = []
for word in first50Words:
    idf = tfidf.computeIdf(word, files)
    idfs.append(idf)
    csvWriter2.writerow([word, idf])

csvFile1.close()
csvFile2.close()
tfCloud.createWordCloud("tf_list.csv")
tfCloud.createWordCloud("tf-idf_list.csv")
csvFile1.close()
csvFile2.close()
