Part 1: Word Embeddings (50 points)
For this first part, we're going to implement a word embedding approach that is a bit simpler than word2vec. The key idea is to look at co-occurrences between center words and context words (somewhat like in word2vec) but without any pesky learning of model parameters.

If you're interested in a deeper treatment of comparing count vs. learned embeddings, take a look at: Don’t count, predict! A systematic comparison of context-counting vs. context-predicting semantic vectors

Load the Brown Corpus
The dataset for this part is the (in)famous Brown corpus that is a collection of text samples from a wide range of sources, with over one million unique words. Good for us, you can find the Brown corpus in nltk. Make sure you have already installed nltk with something like: conda install nltk


import nltk
nltk.download('brown')
​
[nltk_data] Downloading package brown to /Users/hari/nltk_data...
[nltk_data]   Package brown is already up-to-date!
True
Once you have it locally, you can load the dataset into your notebook. You can access the words using brown.words():


from nltk.corpus import brown
brown.words()
[u'The', u'Fulton', u'County', u'Grand', u'Jury', ...]
1.1 Dataset Pre-processing
OK, now we need to do some basic pre-processing. For this part you should:

Remove stopwords and punctuation.
Make everything lowercase.
Then, count how often each word occurs. We will define the 5,000 most frequent words as your vocabulary (V). We will define the 1,000 most frequent words as our context (C). Include a print statement below to show the top-20 words after pre-processing.


  #removing digits
# Your Code Here...
'''
Removing the stopwords using the stopwords from 3 libraries -- 
1. nltk
2. sklearn
3. spacy
​
- Removing blank spaces, numbers and '$'
'''
​
from nltk import word_tokenize
from nltk.corpus import stopwords
import string
from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS
from spacy.lang.en import STOP_WORDS as STOPWORDS
import re
import operator
​
stop = set(stopwords.words('english') + list(string.punctuation) + ['the'] + ["''"] + ["``"] + list('1234567890'))
stop.add(ENGLISH_STOP_WORDS)
stop.union(STOPWORDS)
​
data = []
​
#[i for i in word_tokenize(sent.lower()) if i not in stop]
dict_word = {}
digits = ['1','2','3','4','5','6','7','8','9','0', '$', '-', '/', '.']
digits_set = set(digits)
data = []
for word in brown.words():
    data.append(word)
    if word.lower() not in stop:
        if word[0] not in digits_set:  #removing digits
            if word in dict_word:
                dict_word[word] += 1
            else:
                dict_word[word] = 1
            
i = 0
dict_word = sorted(dict_word.items(), key = lambda x:x[1], reverse=True)
print(dict_word[:20])
​
​
​
[(u'one', 2873), (u'would', 2677), (u'said', 1943), (u'could', 1580), (u'time', 1556), (u'two', 1311), (u'may', 1292), (u'first', 1242), (u'like', 1237), (u'man', 1151), (u'made', 1122), (u'new', 1060), (u'must', 1003), (u'also', 999), (u'Af', 995), (u'even', 985), (u'back', 950), (u'years', 943), (u'many', 925), (u'much', 900)]

import unicodedata
​
context = set()
vocab = set()
context_dict = {}
vocab_dict = {}
i = 0
for w in dict_word[:1000]:
        first =  w[0]
        second = unicodedata.normalize('NFKD', first).encode('ascii','ignore')
        context_dict[str(second)] = i
        i += 1
        context.add(w[0])
​
i = 0
for w in dict_word[:5000]:
    first = w[0]
    second = unicodedata.normalize('NFKD', first).encode('ascii','ignore')
    vocab_dict[str(second)] = i
    i += 1
    vocab.add(w[0])
​
1.2 Making the co-occurance matrix!
Making the co-occurance matrix here, with the vocabulary as rows and context as columns, the dicitonaries made int he previous cell come to the rescue to link the specific column or row number with the exact word.


# Your Code Here...
cooc_matrix = []
​
for word in vocab:
    temp = []
    for cont in context:
        temp.append(0)
    cooc_matrix.append(temp)
# print(len(cooc_matrix))
​
#initializes a 5000x1000 matrix
​
# need to map each vocab word with a number and each context word with a number
# given in the above cell
​
​
i = 0
# data = data[:500]
total2 = 0
​
for word in data:
    ind = i
    if word.lower() in vocab:
        matrix_v_ind = vocab_dict[word.lower()]
        window = data[ind-2:ind+3]
#         print(window)
        for j in window:
            if j.lower() in context:
                #print("yo!")
                total2 += 1
                matrix_c_ind = context_dict[j]
                cooc_matrix[matrix_v_ind][matrix_c_ind] += 1
    i += 1
    
print("Number of times the co-occurance matrix has non-zero values is:")
print(total2)
print("")
print("This clearly shows how sparse the co-occurance matrix really is!")
Number of times the co-occurance matrix has non-zero values is:
176

This clearly shows how sparse the co-occurance matrix really is!