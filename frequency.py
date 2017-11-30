""" Analyzes the word frequencies in a book downloaded from
Project Gutenberg """

import string
import pickle
from collections import defaultdict #frequwords
import operator
"""
This program takes two Mark Twain novels and finds the 100 most common words.
It then finds all of the common words that both novels have in common and 
Removes them from the list.
It then prints a list of the most common unique words in both novels. 
"""


def get_word_list(file_name):
    """ Reads the specified project Gutenberg book.  Header comments,
    punctuation, and whitespace are stripped away.  The function
    returns a list of the words used in the book as a list.
    All words are converted to lower case.
    """
    nopunk = ''
    input_file = open(file_name, 'r')
   # opened_text = pickle.load(input_file)
    book = (input_file.read())
    start_pos = book.find("eBook or online at www.gutenberg.net")+100
    justbook = (book[start_pos:])

    
    for f in string.punctuation:
        justbook = justbook.replace(f, ' ')
        

    justbook = justbook.lower()
    return(justbook.split())
  #  return opened_text


def get_top_n_words(text, n):
    """ Takes a list of words as input and returns a list of the n most frequently
    occurring words ordered from most to least frequently occurring.

    word_list: a list of words (assumed to all be in lower case with no
    punctuation
    n: the number of words to return
    returns: a list of n most frequently occurring words ordered from most
    frequently to least frequentlyoccurring
    """

    top_words = []
    freqwords = defaultdict(int) #initializes a dictionary
    
    for words in text: #goes through a list of all the words in the string text
        freqwords[words] += 1  #if a word is found add 1 to the counter
    sortedwords = sorted(freqwords.items(), key=operator.itemgetter(1), reverse = True) #sorts dictionary of words based on how many times the word was found in reverse order. 
    for i in range(n):
        top_words.append(sortedwords[i][0]) #store the 25 most common words
    return (top_words) 

def commonOverAll(list1,list2):
        """ 
        returns a list of words that are most common in both stories.

        """
    
        return( (list(set(list1).intersection(list2))))
    
def removewords(words,wordstoremove): 
        """
        Removes words from the list that are found in both lists
        """
        
        return ([x for x in words if x not in wordstoremove]) #return elements in words that are not in wordstoremove 
        pass

if __name__ == "__main__":
    print("Running WordFrequency Toolbox")
    print(string.punctuation.split())
    get_word_list('pg32325.txt')
    list1 = (get_top_n_words(get_word_list('pg32325.txt'),100))
    list2 = (get_top_n_words(get_word_list('Inocentabraud.txt'),100))

    comonWords = commonOverAll(list1,list2)
    

    print(removewords(list1,comonWords))
    print(removewords(list2,comonWords))

    