""" Analyzes the word frequencies in a book downloaded from
Project Gutenberg """

import string
import os

def get_word_list(file_name):
    """ Reads the specified project Gutenberg book.  Header comments,
    punctuation, and whitespace are stripped away.  The function
    returns a list of the words used in the book as a list.
    All words are converted to lower case.
    """
    total_list = []
    filedir = os.path.abspath(file_name)
    content = open(filedir)

    for line in content:
        for punctuation in string.punctuation:
            line = line.replace(punctuation,' ')
        total_list.extend(line.split())

    return total_list

def get_top_n_words(word_list, n):
    """ Takes a list of words as input and returns a list of the n most frequently
    occurring words ordered from most to least frequently occurring.

    word_list: a list of words (assumed to all be in lower case with no
    punctuation
    n: the number of words to return
    returns: a list of n most frequently occurring words ordered from most
    frequently to least frequentlyoccurring
    """
    word_frequency = dict()
    for word in word_list:
        if word not in word_frequency:
            word_frequency[word] = 1
        else:
            word_frequency[word] += 1

    sorted_list = sorted(word_frequency, key=word_frequency.__getitem__, reverse=True)
    return sorted_list[0:n]

get_top_n_words(get_word_list('pg32325.txt'), 100)
