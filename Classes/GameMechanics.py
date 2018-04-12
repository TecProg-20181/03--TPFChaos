import string

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
                        |     /|/
                        |
                        |             """,

            1 : """
                        ________
                        |      |
                        |      0
                        |     /|/
                        |     /
                        |             """,

            0 : """
                        ________
                        |      |
                        |      0
                        |     /|/
                        |     / /
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

        self.guesses = 8
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
                print(self.hanging(self.guesses))
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
