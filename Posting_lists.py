import pandas as pd
import json
import porter
import spell
from itertools import chain

def flatten_list(matrix):
    return list(chain.from_iterable(matrix))

def remove_punctuation(text):
    for c in text:  
        if not c.isalnum():
            text = text.replace(c, " ")
    return text

def stem_document(words):
    stemmed_document = []
    for word in words:
        stemmed_word = porter.stem(word)
        stemmed_document.append(stemmed_word)
    return stemmed_document

def create_dictionary(docs_words):
    unique = list(set(docs_words)) 
    unique.sort()         #All unique words in the documents
    return unique 

def create_p_c(docs_words):
    dictionary = flatten_list(docs_words)
    p_c = spell.readwords(dictionary)
    return p_c

def create_posting_lists(dictionary, stemmed_docs):
    posting_lists = dict()
    j=0
    for word in dictionary:
        j+=1
        print(j)
        list = []
        for i in range(len(stemmed_docs)):
            doc = stemmed_docs[i]
            if word in doc:
                list.append(i)
        posting_lists[word] = list
    return posting_lists


dataset = pd.read_csv('D:\Materiale uni magistrale\Digital content retrieval mod. B\Reviews.csv', usecols=['Text'])
docs_words = [] #List of list of words
stemmed_docs = []  #List of list of words
for i in range(len(dataset)):
    doc = remove_punctuation(dataset.iloc[i,0]).lower().split()
    docs_words.append(doc)
    stemmed_doc = stem_document(doc)
    stemmed_docs.append(stemmed_doc) 

dictionary = create_dictionary(flatten_list(stemmed_docs))
posting_lists = create_posting_lists(dictionary=dictionary, stemmed_docs=stemmed_docs)


with open('posting_lists_1.json', 'w') as convert_file:
    convert_file.write(json.dumps(posting_lists))
print('Done')

p_c = create_p_c(docs_words)
print('Done')

with open('p_c.json_1', 'w') as convert_file:
    convert_file.write(json.dumps(p_c))



