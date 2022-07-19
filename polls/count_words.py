from nltk.tokenize import RegexpTokenizer
import sys


def count_words(text):
    tokenizer = RegexpTokenizer(r'\w+')
    return len(tokenizer.tokenize(text))

