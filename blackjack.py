# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 21:06:41 2021

@author: Devesh Prasad
"""
import random
# import clear
import os
clear = lambda: os.system('cls')

def deal_card():
    # to create random card generation
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card
def calculate_score(cards):
    # to calculate score of user and computer
    # user or computer got 21
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare(user_score, computer_score):
    if user_score==computer_score:
        return "Draw"
    elif computer_score==0:
        return "Lose , opponent has Blackjack"
    elif user_score==0:
        return "Win with a Blackjack"
    elif user_score>21:
        return "You went over. You Lose"
    elif computer_score>21:
        return "Opponent went over . You Win "
    elif user_score>computer_score:
        return "You Win"
    else:
        return "You Lose"
def play_game():
    
    user_cards=[]
    computer_cards=[]
    is_game_over=False
    
    for _ in range(2):
        # to get random card and add it to the computer and user list
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
        
    while not is_game_over:
           
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)    
        print(f" Your cards are {user_cards} , current score : {user_score} ")
        print(f"Computer first card is : {computer_cards[0] }")
        
        if user_score==0 or computer_score==0 or user_score>21:
            is_game_over=True
        else:
            user_should_deal=input("Type 'y' to get another card or 'n' to deal :")
            if user_should_deal=="y":
                user_cards.append(deal_card())
            else:
                is_game_over=True
    while computer_score !=0 and computer_score<17:
          computer_cards.append(deal_card())
          computer_score=calculate_score(computer_cards)
    print(f"Your final hand : {user_cards} , final score : {user_score}")
    print(f"Computer final are : {computer_cards} , final score:{computer_score}")
    print(compare(user_score, computer_score))
while input("Wanna Play Blackjack  'y' for YES or 'n' for NO :")=="y":
    clear()
    play_game()