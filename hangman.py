# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 20:24:35 2021

@author: Devesh Prasad
"""
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lives=6
# from replit import clear
import random
from hangman_words import word_list
chosen_word=random.choice(word_list)
print(f"Choose word is {chosen_word}")
display=[]
for _ in range(len(chosen_word)):
    display+="_"
print(display)
end_of_game=False
while not end_of_game:
    guess=input("Guess a letter ? ").lower()
    #clear()
    if guess in display:
        print(f"You have already guessed the {guess} letter !")
    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        # print(f"Current position is {position} and letter is {guess} ")
        if letter==guess:
            display[position]=letter
    if guess not in chosen_word:
        print(f"Sorry you guessed this wrong letter {guess} ! Try Again")
        lives-=1
        if lives==0:
            end_of_game=True
            print("You Lose !")
            
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game=True
        print("You Win")
    print(stages[lives])