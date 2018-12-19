import collections
import pandas as pd
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

import nltk
nltk.download('stopwords')
nltk.download('punkt')

# Read input file, note the encoding is specified here
# It may be different in your text file
file = open('asd.txt')
a = file.read()
a = a.lower()
# Stopwords
stopwords = set(stopwords.words('english'))
academicStopwords = set(line.strip() for line in open('acStopWords.txt'))
academicStopwords = academicStopwords.union(set(['mr','mrs','one','two','said']))
words = word_tokenize(a)

wordsFiltered = []

for w in words:
    if w not in stopwords and academicStopwords:
        wordsFiltered.append(w)

print(wordsFiltered)
# Instantiate a dictionary, and for every word in the file,
# Add to the dictionary if it doesn't exist. If it does, increase the count.
wordcount = {}

# To eliminate duplicates, remember to split by punctuation, and use case demiliters.
for word in wordsFiltered:
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
# Print most common word
n_print = int(input("How many most common words to print: "))
print("\nOK. The {} most common words are as follows\n".format(n_print))
word_counter = collections.Counter(wordcount)
for word, count in word_counter.most_common(n_print):
    print(word, ": ", count)
# Close the file
file.close()
# Create a data frame of the most common words
# Draw a bar chart
