from loadBooks import *
import string
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import nltk
from collections import defaultdict #frequwords
import random
import operator


def removegutnburg(text):
	"""
	Removes the Gutenberg license information for so that the text can 
	be analyzed.

	"""
	
	licence = "ject Gutenberg Association / Carnegie Mellon University" #last line in license
	bookstart = "by William Shakespeare" # set to Act V to
	bookend = "THE END"
	start_pos = text.find(licence) + 60 				#finds the end of the licensing agreement	
	start_reading = text.find(bookstart,start_pos) + 22 #all of the books start with "title" by William Shakespeare
	end_reading = text.find(bookend,start_reading ) 	#finds THE END at the end of the book
	return (text[start_reading:end_reading])			#returns text of the play


def loadjustbooks(playfiles):
	"""
	Takes a list of play names and a list of text files of those plays.
	Removes Gutenberg license, newlines and punctuation from the play text.

	Ex. Makes a list of all of the text of the comedic plays

	"""

	plays = []

	
	for i in playfiles:
		play = opensavedbook(i)		#opens play text file
		just_play = removegutnburg(play) #removes gutenberge license
		just_play = RemoveAllButLettersAndSpaces(just_play) #removes newlines and punctuation
		plays.append(just_play)		#adds current play to the play list

	return plays #returns list of plays

def RemoveAllButLettersAndSpaces(mystring):
	"""
	removes special characters and punctuation from play texts.
	>>>  RemoveAllButLettersAndSpaces("\r\nqwetr.,")
	'qwe2tr'
	"""
	toremove = ['\r', '\n','\'','[', ']','.','?', ';',':','-', '\"',',']
	for c in toremove:
		mystring = mystring.replace(c, ' ')

	
	return mystring.lower() #makes everything lower case words like "The" and "the" are the same

def RunSentAnalysis(mylist):
	"""
	runs sentimient analysis and returns positive and negitive sentiments 
	"""
	res = []
	analyzer = SentimentIntensityAnalyzer()
	answer = analyzer.polarity_scores(mylist)
	res.append(answer["pos"])
	res.append(answer["neg"])
	return res
	

def Most_Common(text):
	"""
	takes a string and returns the 25 most common words in the string
	"""
	top_words = []
	freqwords = defaultdict(int) #initializes a dictionary
	
	for words in text.split(): #goes through a list of all the words in the string text
		freqwords[words] += 1  #if a word is found add 1 to the counter
	sortedwords = sorted(freqwords.items(), key=operator.itemgetter(1), reverse = True) #sorts dictionary of words based on how many times the word was found in reverse order. 
	for i in range(25):
		top_words.append(sortedwords[i][0])	#store the 25 most common words
	return (top_words)						#Rreturns a list of the 24 most common words

def commonOverAll(list1,list2,list3):
	""" 
	returns a list of all the most universally common words of all three story types

	"""
	
	return( list(set(list(set(list1).intersection(list2))).intersection(list3)))

def removewords(words,wordstoremove): 
	"""
	Removes words from the plays that are univeraly common amonge all types
	"""
	words = words.split()
	return ([x for x in words if x not in wordstoremove]) #return elements in words that are not in wordstoremove

def listtostring(mylist):
	"""
	convers a list of words to string of words
	"""
	return ' '.join(mylist)

def linklists(mylist):
	"""
	Add several list together into one large list
	"""
	res = []
	for i in range(len(mylist)):
		res += [mylist[i]]
	return listtostring(res)

def sampling(mylist, trials):
	pos = 0
	neg = 0
	for i in range(trials):
		sample = listtostring(random.sample(mylist,10))
		sentiment = RunSentAnalysis(sample)
		pos += sentiment[0]
		neg += sentiment[1]

	return[pos/trials, neg/trials]


def textmining(): # Main function that runs the textmining code.
	"""
	13 of Shakespeare’s plays were saved from gutenberg.org.
	I sorted the file names of all of the plays into tree lists
	comedies, tragedies, and histories.

	"""
	
	comedies = ['A_Midsummer_Nights_Dream.pickle', 'Alls_Well_That_Ends_Well.pickle']
	tragedies = ['Antony_and_Cleopatra.pickle','Coriolanus.pickle','Cymbeline.pickle']
	histories = ['King_Henry_IV.pickle','King_John.pickle','King_Richard_II.pickle']


	colletion = []								#list to store all three types of books
	colletion.append(loadjustbooks(comedies))	#loads text from the comedies into the first element
	colletion.append(loadjustbooks(tragedies))	#loads text from the trageties into the second element
	colletion.append(loadjustbooks(histories))	#loads text from the histories into the second element
														#collection was broken up into comedies, tragedies and
														#histories to increase code readability
	all_comedies = (linklists(colletion[0]))			#combines all of the saved comedies into one list
	all_trageties = (linklists(colletion[1]))			#combines all of the saved trageties into one list
	all_histories = (linklists(colletion[2]))			#combines all of the saved histories into one list

	common_comedies = (Most_Common(all_comedies))		#finds the most common words in Shakespeare’s comedies
	common_trageties = (Most_Common(all_trageties))		#finds the most common words in Shakespeare’s trageties
	common_histories = (Most_Common(all_histories))		#finds the most common words in Shakespeare’s histories

	common_words = (commonOverAll(common_comedies,common_trageties, common_histories)) #make a list of words common along all three play types

	comedy_uncommon = removewords(all_comedies,common_words)		#removes the univeraly common words from the comedic plays
	tragety_uncommon = removewords(all_trageties,common_words)	#removes the universally common words from the tragic plays
	history_uncommon = removewords(all_histories,common_words)	#removes the universally common words from the historic plays

	



	print("\n")
	print("Sentiment Analysis Average of Comedic Plays")
	average = sampling(comedy_uncommon,500)		#preform Sentiment Analyses on all three play types
	print (average)
	print("Sentiment Analysis of Tragic Plays")
	average = sampling(tragety_uncommon,500)		#preform Sentiment Analyses on all three play types
	print (average)
	print("Sentiment Analysis of Historic Plays")
	average = sampling(tragety_uncommon,500)		#preform Sentiment Analyses on all three play types
	print (average)
	#RunSentAnalysis(tragic_string)
	#print("\n")
	#print("Sentiment Analysis of Historic Plays")
	#RunSentAnalysis(historic_string)




textmining()
#if __name__ == "__main__":
#    import doctest
#doctest.testmod()

