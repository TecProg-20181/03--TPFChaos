import random
import string

WORDLIST_FILENAME = "palavras.txt"

class Word():

    def __init__(self):
        self.secretWord = self.loadWords().lower()
        self.inFile = ''
        self.line = ''
        self.wordlist = ''
        self.length = 9

    def loadWords(self):
        print ("Loading word list from file...")
        self.inFile = open(WORDLIST_FILENAME, 'r')
        self.line = self.inFile.readline()
        self.wordlist = self.line.split(' ')
        print ("  ", len(self.wordlist), "words loaded.")
        return random.choice(self.wordlist)

    def diffCharacters(self):
        while self.length > 8:
            diff = ''.join(set(self.secretWord))
            self.length = len(diff)
        return self.length

class GameMechanics():
    def __init__(self):
        self.guesses = 8
        self.secretWord = ''

    def isWordGuessed(self):

        for letter in self.secretWord:
            if letter in self.lettersGuessed:
                pass
            else:
                return False

        return True


    def hanging(self,guesses):
        return {
            7: """
                        |
                        |
                        |
                        |
                        |             """,

            6 :"""
                        ________
                        |      |
                        |
                        |
                        |
                        |             """,

            5 : """
                        ________
                        |      |
                        |      0
                        |
                        |
                        |             """,

            4 : """
                        ________
                        |      |
                        |      0
                        |     /
                        |
                        |             """,

            3 : """
                        ________
                        |      |
                        |      0
                        |     /|
                        |
                        |             """,

            2: """
                        ________
                        |      |
                        |      0
                        |     /|\
                        |
                        |             """,

            1 : """
                        ________
                        |      |
                        |      0
                        |     /|\
                        |     /
                        |             """,

            0 : """
                        ________
                        |      |
                        |      0
                        |     /|\
                        |     / \
                        |
                            GAME OVER!"""

        }[self.guesses]

    def letterGuessing(self):
        self.guessed = ''
        for letter in self.secretWord:
            if letter in self.lettersGuessed:
                self.guessed += letter
            else:
                self.guessed += '_ '
            return self.guessed

    def hangman(self,secretWord,length):

        self.guesses = 1
        self.secretWord = secretWord
        self.lettersGuessed = []
        print ('Welcome to the game, Hangam!')
        print ('I am thinking of a word that is', len(self.secretWord), ' letters long.')
        print ('This word has',length,'different characters.' )
        print ('-------------')

        while  self.isWordGuessed() == False and self.guesses >0:
            print ('You have ', self.guesses, 'guesses left.')
            self.available = string.ascii_lowercase
            for letter in self.available:
                if letter in self.lettersGuessed:
                    self.available = self.available.replace(letter, '')

            print ('Available letters:', self.available)
            letter = input('Please guess a letter: ')
            if letter in self.lettersGuessed:

                self.guessed = ''
                for letter in self.secretWord:
                    if letter in self.lettersGuessed:
                        self.guessed += letter
                    else:
                        self.guessed += '_'

                print ('Oops! You have already guessed that letter: ', self.guessed)
            elif letter in self.secretWord:
                self.lettersGuessed.append(letter)
                self.guessed = ''
                for letter in self.secretWord:
                    if letter in self.lettersGuessed:
                        self.guessed += letter
                    else:
                        self.guessed += '_'

                print ('Good Guess: ', self.guessed)
            else:

                self.guesses -= 1
                #self.length = Word.diffCharacters(self.secretWord)
                #print(self.hanging(self.guesses))
                self.lettersGuessed.append(letter)

                self.guessed = self.letterGuessing()
                print(self.guesses)

                print ('Ops! That letter is not in my word: ',  self.guessed)
            print ('------------')

        else:
            if self.isWordGuessed() == True:
                print ('Congratulations, you won!')
            else:
                print ('Sorry, you ran out of guesses. The word was ', self.secretWord, '.')

word = Word()
mech = GameMechanics()

secretWord = word.loadWords()
length = word.diffCharacters()

mech.hangman(secretWord,length)

###The code was adapted from python2 to python3
