""" Analyzes the word frequencies in a book downloaded from
Project Gutenberg """

import string


def get_word_list(file_name):
    """ Reads the specified project Gutenberg book.  Header comments,
    punctuation, and whitespace are stripped away.  The function
    returns a list of the words used in the book as a list.
    All words are converted to lower case.
    """
    f = open(file_name, 'r')
    lines = f.readlines()
    curr_line = 0
    end_line =0
    while lines[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
      curr_line += 1
    while lines[end_line].find('End of the Project Gutenberg EBook') == -1:
      end_line += 1
    lines = lines[curr_line+1:end_line]
    text = ''
    for n in lines:
        text = text+n
    for n in string.punctuation:
        text = text.replace('--',' ')
        text = text.replace(n,'')
        text = text.lower()
    words = text.split()
    return words

get_word_list('heartofdarkness.txt')

def get_top_n_words(word_list, num):
    """ Takes a list of words as input and returns a list of the num most frequently
    occurring words ordered from most to least frequently occurring.

    word_list: a list of words (assumed to all be in lower case with no
    punctuation
    num: the number of words to return
    returns: a list of n most frequently occurring words ordered from most
    frequently to least frequentlyoccurring
    """
    freq = {}
    for n in word_list:
        if n in freq:
            freq[n] = freq[n]+1
        else : freq[n] = 1
    words = []
    for n in freq:
        words.append((freq[n],n))
    words.sort(reverse = True)
    res = []
    for i in range(0,num):
        res.append(words[i][1])
    print(res)

if __name__ == "__main__":
    print("Running WordFrequency Toolbox")
    word_list = get_word_list('heartofdarkness.txt')
    top_words = get_top_n_words(word_list,10)
    print(top_words)
