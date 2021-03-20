# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 12:14:38 2021

@author: Devesh Prasad
"""
##############################   SCOPE

from random import randint

easy_level_turns=5
hard_level_turns=10

turns=0
def check_answer(guess,answer, turns):
    if guess>answer:
        print("Too high !")
        return turns-1
    elif guess<answer:
        print("Too low !")
        return turns-1
    else:
        print(f"You got it Dammmmmn. The  answer is {answer} .")


def set_difficulty():
    level=input("Chooose a difficulty, Type 'easy' or 'hard' : ")
    if level=="easy":
        return easy_level_turns
    elif level=="hard":
        return hard_level_turns
    else:
        input("Please enter valid digits !")
        
def game():
    print("Welcome! The Game Begins")
    print("I'm thinking of a number between 1 - 100")
    answer=randint(1,100)
    turns=set_difficulty()
    print(f"The answer is {answer}")
    guess=0
    while guess!=answer:
        print(f"The no of guesses remaining is {turns}")
        guess=int(input("Make a guess :"))
        turns=check_answer(guess, answer,turns)   
        if turns==0:
            print("You Loser! Try some other easy games !hahahahah ")
            return
        elif guess!=answer:
            print("Guess again.")

game()