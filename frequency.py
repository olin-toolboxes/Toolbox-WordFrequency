# -*- coding:utf-8 -*-
""" Analyzes the word frequencies in a book downloaded from
Project Gutenberg """

import string
import re
from collections import Counter


def get_word_list(file_name):
    """ Reads the specified project Gutenberg book.  Header comments,
    punctuation, and whitespace are stripped away.  The function
    returns a list of the words used in the book as a list.
    All words are converted to lower case.
    """
    f = open(file_name, 'r', encoding = 'utf-8')
    lines = f.readlines()
    curr_line = 0
    while lines[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
      curr_line += 1
    lines =  lines[curr_line+1:]
    lines = [''.join(ch for ch in line if ch not in set(string.punctuation)) for line in lines]
    word_list = []
    for line in lines:
        word_list.extend(line.lower().split())
    print('done')
    return word_list


def get_top_n_words(word_list, n):
    """ Takes a list of words as input and returns a list of the n most frequently
    occurring words ordered from most to least frequently occurring.

    word_list: a list of words (assumed to all be in lower case with no
    punctuation
    n: the number of words to return
    returns: a list of n most frequently occurring words ordered from most
    frequently to least frequentlyoccurring
    """
    counts = Counter(word_list)
    ordered = sorted(word_list, key=lambda x: -counts[x])
    seen = {}
    freq_words = [seen.setdefault(x, x) for x in ordered if x not in seen]
    return freq_words[:n]

if __name__ == "__main__":
    print("Running WordFrequency Toolbox")
    list = get_word_list('pg32325.txt')
    print(get_top_n_words(list,100))
