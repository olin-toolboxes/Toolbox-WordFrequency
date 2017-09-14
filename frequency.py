""" Analyzes the word frequencies in a book downloaded from
Project Gutenberg """

import string
from pickle import dump, load


def get_word_list(file_name):
    """ Reads the specified project Gutenberg book.  Header comments,
    punctuation, and whitespace are stripped away.  The function
    returns a list of the words used in the book as a list.
    All words are converted to lower case.
    """
    file_ = open(file_name, 'r')
    lines = file_.readlines()

    start_line = 0
    while lines[start_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
        start_line += 1

    lines = lines[start_line+1:]

    end_line = 0
    while lines[end_line].find('END OF THIS PROJECT GUTENBERG EBOOK') == -1:
        end_line += 1

    lines = lines[:end_line-3]

    list_ = ' '.join(lines)
    list_ = str.lower(list_)
    list_ = list_.translate(None, string.punctuation)
    list_ = list_.split()

    return list_


def get_top_n_words(word_list, n):
    """ Takes a list of words as input and returns a list of the n most frequently
    occurring words ordered from most to least frequently occurring.

    word_list: a list of words (assumed to all be in lower case with no
    punctuation
    n: the number of words to return
    returns: a list of n most frequently occurring words ordered from most
    frequently to least frequently occurring
    """
    word_counts = dict()

    for word in word_list:
        freq = word_counts.get(word, 1)
        word_counts[word] = freq + 1

    ordered_by_frequency = sorted(word_counts, key=word_counts.get, reverse=True)

    return ordered_by_frequency[0:n]


if __name__ == "__main__":
    print("Running WordFrequency Toolbox")
    word_list = get_word_list('Frankenstein.txt')
    print(get_top_n_words(word_list, 100))
