#!/usr/bin/env python
# coding: utf-8

# # CORPUS/DATA SET

# In[66]:


import nltk
nltk.downloader.download("book","nltl_data")


# 
# # TEXT NORMALIZATION

# In[69]:


from nltk.corpus import stopwords
import string
import re
from nltk.book import*


# In[78]:


stopwords_list=stopwords.words('english')
ftext=" ".join(text6)
#print(ftext)
sp=ftext.split()
#print(sp)
pun=list(string.punctuation)
list_of_words=[]
for i in sp:
    if i not in pun:
        list_of_words.append(i)
print(list_of_words)


# # TRIGRAM ALGORITHM

# In[87]:


def Tri_Grams(text6):
    text6=" ".join(text6)
    trigram=nltk.collocations.BigramCollocationFinder.from_words(text6.split())
    for trig,freq in trigram.ngram_fd.items():
        print(trig,freq)
Tri_Grams(text6)

