
from Classes.word import Word
from Classes.GameMechanics import GameMechanics

word = Word()
mech = GameMechanics()

secretWord = word.loadWords()
length = word.diffCharacters()

while True:
    if length > 8:
        secretWord = word.loadWords()
        length = word.diffCharacters()
    elif 8 > length:
        break

mech.hangman(secretWord,length)

###The code was adapted from python2 to python3
