""" Analyzes the word frequencies in a book downloaded from
Project Gutenberg """

import string

def get_word_list(file_name):
    """ Reads the specified project Gutenberg book.  Header comments,
    punctuation, and whitespace are stripped away.  The function
    returns a list of the words used in the book as a list.
    All words are converted to lower case.
    """
    book = requests.get(file_name).text
    split_text = book.split()
    #F ind index of second '***'
    asterisk = split_text.index('***')
    split_text = split_text[asterisk+1:]
    asterisk2 = split_text.index('***')
    split_text = split_text[asterisk2+1:]
    # Make words lowercase
    split_text = [x.lower() for x in split_text]
    return split_text

def get_top_n_words(word_list, n):
    """ Takes a list of words as input and returns a list of the n most frequently
    occurring words ordered from most to least frequently occurring.

    word_list: a list of words (assumed to all be in lower case with no
    punctuation
    n: the number of words to return
    returns: a list of n most frequently occurring words ordered from most
    frequently to least frequentlyoccurring
    """
    frequency = {}
    for word in word_list:
        frequency[word] = 0
    for word in word_list:
        frequency[word] += 1
    sort_top_words = sorted(frequency.items(), key=lambda x:x[1])
    sort_top_words.reverse()
    return sort_top_words[:n]

if __name__ == "__main__":
    print("Running WordFrequency Toolbox")
    print(string.punctuation)
