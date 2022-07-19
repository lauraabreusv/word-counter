from nltk.tokenize import RegexpTokenizer
import sys


def count_words(text):
    tokenizer = RegexpTokenizer(r'\w+')
    try:
        c = len(tokenizer.tokenize(text))
    except:
        c = 0
    return c

