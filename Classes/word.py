import random
import string
import os
import sys

WORDLIST_FILENAME = "palavras.txt"

class Word():

    def __init__(self):
        self.secretWord = ''
        self.inFile = ''
        self.line = ''
        self.wordlist = ''
        self.length = 9
        self.nowords = False

    def loadWords(self):
        print ("Loading word list from file...")
        try:
            self.inFile = open(WORDLIST_FILENAME, 'r')
            if os.stat(WORDLIST_FILENAME).st_size > 0:
               print ("All good")
            else:
               print ("The file is Empty! The game will be ended due to no words being available")
               sys.exit()                       
        except OSError:
            print ("No file found")
            sys.exit()        
        self.line = self.inFile.readline()
        self.wordlist = self.line.split(' ')
        print ("  ", len(self.wordlist), "words loaded.")                       
        word = random.choice(self.wordlist)
        for letter in word:
            if letter.isalpha() == False and letter.isspace() == False:
                print('The word contains letters, please choose an archive with nothing but letters and spaces')
                sys.exit()
        return word

    def diffCharacters(self):
        while self.length > 8:
            diff = ''.join(set(self.secretWord))
            self.length = len(diff)
        return self.length
