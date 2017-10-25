""" Analyzes the word frequencies in a book downloaded from
Project Gutenberg """

import re, string


def get_word_list(file_name):
    """ Reads the specified project Gutenberg book.  Header comments,
    punctuation, and whitespace are stripped away.  The function
    returns a list of the words used in the book as a list.
    All words are converted to lower case.
    """

    file = open(file_name, 'r')
    text = file.read() # read
    file.close()

    cut_text = re.search('START OF THIS PROJECT GUTENBERG EBOOK THE ADVENTURES OF HUCKLEBERRY FINN(.+?)END OF THIS PROJECT GUTENBERG EBOOK THE ADVENTURES OF HUCKLEBERRY FINN', text).group(1)
    word = re.compile(r'\w+')
    text = cut_text.lower()
    words = word.findall(text)

    return words





def get_top_n_words(word_list, n):
    """ Takes a list of words as input and returns a list of the n most frequently
    occurring words ordered from most to least frequently occurring.

    word_list: a list of words (assumed to all be in lower case with no
    punctuation
    n: the number of words to return
    returns: a list of n most frequently occurring words ordered from most
    frequently to least frequentlyoccurring
    """
    return Counter(word_list).most_common(n)


get_top_n_words(get_word_list('pg32325.txt'), 100)

# if __name__ == "__main__":
#     print("Running WordFrequency Toolbox")
#     print(string.punctuation)
