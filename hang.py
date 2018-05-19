
from Classes.word import Word
from Classes.GameMechanics import GameMechanics

word = Word()
mech = GameMechanics()

while True:
    secretWord = word.loadWords()
    length = word.diffCharacters()
    if 8 > length:
        break

mech.hangman(secretWord,length)

