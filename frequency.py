""" Analyzes the word frequencies in a book downloaded from
Project Gutenberg

John Wen
 """

import string


def remove_punct(textlist):
    """ A helper function to remove all punctuations from a string while
    converting the list into a string
    """
    cleanedlist = []
    textlist = textlist.lower().split()
    for word in textlist:
        symbols = string.punctuation
        for i in range (0,len(symbols)):
            word = word.replace(symbols[i], '')
        if len(word) > 0:
            cleanedlist.append(word)
    return cleanedlist

# print(remove_punct('so people said. They judged it was him, anyway; said this drownded man'))


def get_word_list(file_name):
    """ Reads the specified project Gutenberg book.  Header comments,
    punctuation, and whitespace are stripped away.  The function
    returns a list of the words used in the book as a list.
    All words are converted to lower case.
    """
    f = open(file_name, 'r')
    lines = f.readlines()
    curr_line = 0
    while lines[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
      curr_line += 1
      lines = lines[curr_line+1:]
    """ first part of code removes the headers while the second part cleans the white space
    and then cleans the string of punctuations using the helper function above
    """
    cleanedwhitespace = []
    cleanedlist = []
    for words in lines:
        cleanedwhitespace.append(words.rstrip())
    for eachstring in cleanedwhitespace:
        cleanedlist.extend(remove_punct(eachstring))
    return cleanedlist



def highestfreqword(d):
    """ returns the highest value in the dictionary as a tuple pair

    >>> highestfreqword({'the': 5, 'apple': 2, 'is' : 3, 'large' : 15})
    ('large', 15)
    >>> highestfreqword({'the': 5, 'apple': 8, 'is' : 3, 'large' : 2})
    ('apple', 8)

    Functionality: Breaks down the dictionary down into lists of keys and values and
    picks the highest value and maps that index back to the key.
    """
    v=list(d.values())
    k=list(d.keys())
    return k[v.index(max(v))], d[k[v.index(max(v))]]


def get_top_n_words(word_list, n):
    """ Takes a list of words as input and returns a list of the n most frequently
    occurring words ordered from most to least frequently occurring.

    word_list: a list of words (assumed to all be in lower case with no
    punctuation
    n: the number of words to return
    returns: a list of n most frequently occurring words ordered from most
    frequently to least frequently occuring.

    """
    d = dict()
    for words in word_list:
        d[words] = d.get(words,0) + 1
    newdictionary = d
    listoftups = []
    while n > 0:
        listoftups.append(highestfreqword(newdictionary))
        newdictionary.pop(highestfreqword(newdictionary)[0])
        n = n - 1
    return listoftups

if __name__ == "__main__":
    print(get_top_n_words(get_word_list('pg32325.txt') ,100))
    import doctest
    doctest.testmod(verbose=False)
