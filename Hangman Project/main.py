# Importação das bibliotecas necessárias.

import random

import os

from hangman_ascii import logo
from hangman_ascii import stages

from hangman_data import word_list

# Início do jogo. 

print(logo)

print("Olá! Deseja iniciar o jogo? ")

os.system('pause')
os.system('cls')

# Variáveis Principais.

random_word = random.choice(word_list)
size_of_word = len(random_word)

# Determinando a quantidade de espaços impressas.

i = 0
blank = ""

while i < size_of_word:
    blank += "- "
    i += 1

blank_list = blank.split(" ")
blank_list.remove("")

# Determinando a palavra nos espaços.

chosen_word = list(random_word)

# Determinando a quantidade de letras repetidas na palavra aleatória.

different_letters = set()

for letter in random_word:
    if letter.isalpha():
        different_letters.add(letter.lower())

# Estrutura principal do jogo.

number_of_letters = len(different_letters)
life = 6
character = 1
correct_guess = 0
letters_guessed = []

while True:
    if ((correct_guess == number_of_letters) or not(life > 0)):
        break
    else:
        n = 0
        hit = False
        fail = 0

        separator = " "
        blanks = separator.join(blank_list)

        print(stages[-character])
        print(blanks)
        print(f"Sua vida restante é {life}")
        user_choice = input("Digite uma letra: ")

        os.system('cls')

        for letter in different_letters:
            if user_choice == letter:
                hit = True  
            else:
                fail += 1
        
        if fail == number_of_letters:
            life -= 1
            character += 1

        if hit == True:
            for letter in chosen_word:
                if user_choice == letter:
                        blank_list[n] = user_choice
                        n += 1
                else:
                        n += 1
            if correct_guess == number_of_letters - 1:
                print(stages[-character])
                separator = " "
                blanks = separator.join(blank_list)
                print(blanks)
            correct_guess += 1

        # Determinando se o input está repetido.

        for char in letters_guessed:
            if user_choice == char:
                correct_guess -= 1
                life -= 1
                character += 1

        letters_guessed = set()

        for char in user_choice:
            if char.isalpha():
                letters_guessed.add(char.lower())

# Determinando se é vencedor ou perdedor.
if correct_guess == number_of_letters:
    print("Vitoria.")
if life == 0:
    print(stages[-character])
    print(f"Derrota. A palavra era {random_word}.")
