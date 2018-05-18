
from Classes.word import Word
from Classes.GameMechanics import GameMechanics

word = Word()
mech = GameMechanics()

#secretWord = word.loadWords()
#length = word.diffCharacters()

while True:
    secretWord = word.loadWords()
    length = word.diffCharacters()
    if 8 > length:
        break

mech.hangman(secretWord,length)

###The code was adapted from python2 to python3
