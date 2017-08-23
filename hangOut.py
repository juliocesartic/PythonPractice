# -*- coding: utf-8 -*-
import random


IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']

WORDS = ['lavadora', 'secadora', 'sofa', 'gobierno', 
'diputado', 'democracia', 'computadora', 'teclado']

def random_word():
    index = random.randint(0, len(WORDS) - 1)
    return WORDS[index]

def show_board(hidden_word, tries):
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print('----*----*----*----*----*')

def run():
    word = random_word()
    hidden_word = ['-'] * len(word)
    tries = 0
    while True:
        show_board(hidden_word, tries)
        current_letter = str(raw_input('Escoge una letra: '))

        letter_indexes = []
        for idx in range(len(word)):
            if word[idx] == current_letter:
                letter_indexes.append(idx)
        
        if len(letter_indexes) == 0:
            tries += 1
        else:
            for idx in letter_indexes:
                hidden_word[idx] = current_letter
            
            letter_indexes = []

if __name__ == '__main__':
    print(' BIENVENIDOS A EL JUEGO HANG OUT.')
    run()