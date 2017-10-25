""" Analyzes the word frequencies in a book downloaded from
Project Gutenberg """

import string
from collections import Counter

def get_word_list(filename):
    """ Reads the specified project Gutenberg book.  Header comments,
    punctuation, and whitespace are stripped away.  The function
    returns a list of the words used in the book as a list.
    All words are converted to lower case.
    """
    f = open(filename, 'r')
    lines = f.readlines()
    curr_line = 0
    while lines[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
        curr_line += 1
    lines = lines[curr_line+1:]
    word_list = []
    for line in lines:
        for word in line.split():
            for character in string.punctuation:
                word = word.replace(character,'')
            word = word.lower()
            word_list.append(word)
    return word_list


def get_top_n_words(word_list,n):
    """ Takes a list of words as input and returns a list of the n most frequently
    occurring words ordered from most to least frequently occurring.

    word_list: a list of words (assumed to all be in lower case with no
    punctuation
    n: the number of words to return
    returns: a list of n most frequently occurring words ordered from most
    frequently to least frequentlyoccurring
    """
    words = Counter(word_list)
    top_n = words.most_common(n)
    return top_n


def main():
    word_list = get_word_list('pg1661.txt')
    print(get_top_n_words(word_list,10))


if __name__ == "__main__":
    main()
