import unicodedata
import re
import json

import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords

import pandas as pd

def basic_clean(raw_text):
    '''
    Takes in a string of raw text,
    return text in lower case, normalized to ASCII characters and stripped of all characters that are not
    a white space, a single apostrophe, or alphanumeric.
    '''
    clean_text = raw_text.lower()
    clean_text = unicodedata.normalize('NFKD', clean_text)\
        .encode('ascii', 'ignore')\
            .decode('utf-8', 'ignore')
    clean_text = re.sub(r"[^a-z0-9'\s]", '', clean_text)
    return clean_text

def tokenize(raw_text):
    tokenizer = nltk.tokenize.ToktokTokenizer()
    tokenized_text = tokenizer.tokenize(raw_text, return_str=True)
    return tokenized_text

def stem(raw_text):
    '''
    Takes in a string of raw text,
    returns any existing stemmed version of the text
    '''
    ps = nltk.porter.PorterStemmer()
    stemmed_text = ps.stem(raw_text)
    return stemmed_text

def lemmatize(raw_text):
    wnl = nltk.stem.WordNetLemmatizer()
    lemmatized_text = wnl.lemmatize(raw_text)
    return lemmatized_text

def remove_stopwords(text_string, extra_words=[], exclude_words=[]):
    '''
    Takes in a list of strings,
    return list with stopwords removed.
    '''
    stopword_list = stopwords.words('english')
    stopword_list = set(stopword_list) - set(exclude_words)
    stopword_list = set(stopword_list).union(set(extra_words))
    
    filtered_text = [word for word in text_string.split() if word not in stopword_list]
    return ' '.join(filtered_text)