import os
import io
import numpy
import scipy
from pandas import DataFrame
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

def readFiles(path):
    for root, dirnames, filenames in os.walk(path):
        for filename in filenames:
            path = os.path.join(root, filename)

            inBody = False
            lines = []
            f = io.open(path, 'r', encoding='latin1')
            for line in f:
                if inBody:
                    lines.append(line)
                elif line == '\n':
                    inBody = True
            f.close()
            message = '\n'.join(lines)
            yield path, message


def dataFrameFromDirectory(path, classification):
    rows = []
    index = []
    for filename, message in readFiles(path):
        rows.append({'message': message, 'class': classification})
        index.append(filename)

    return DataFrame(rows, index=index)

f = open("datacleanfile.txt", "w+")

data = DataFrame({'message': [], 'class': []})
#We want a dataframe with 2 columns - message --> actual text and class --> spam/ham

data = data.append(dataFrameFromDirectory('spam', 'spam'))
data = data.append(dataFrameFromDirectory('ham', 'ham'))

#putting only the top 5 entries of the emails from spam in the file
# so as to showcase the result of the data cleaning
f.write(str(data.head()))

#COuntVectorize() - segregates the words in emails and classifies them
vectorizer = CountVectorizer()
counts = vectorizer.fit_transform(data['message'].values)
#counts give the number of times each word occurs in each individual message

classifier = MultinomialNB()
targets = data['class'].values
classifier.fit(counts, targets)

#testing the classifier on two input statements --> to predict if the emails are spam or ham

examples = ['Free Viagra now!!!', "Hi Gary, how about a game tomorrow?", 'Free Free Free!!']
example_counts = vectorizer.transform(examples)
predictions = classifier.predict(example_counts)
print(predictions)
k = open("results.txt", "w+")
k.write(str(predictions))