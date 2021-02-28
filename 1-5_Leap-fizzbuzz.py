# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 16:03:47 2021

@author: Devesh Prasad
"""
################################     LEAP YEAR
year=int(input("Which year do you want to check ?"))
if year % 4==0:
    if year % 100==0:
       if year % 400==0:
           print("Leap Year")
       else:
           print("Not Leap Year")
    else:
        print("Leap Year")
else:
    print("Not a Leap Year")
    
#############################  ROCK PAPER SCISSORS
import random
Rock="rock"
Paper="paper"
Scissors="scissors"
game=[Rock,Paper,Scissors]
user_choice=int(input("Type 0 for Rock, 1 for Paper, 2 for scissors ?\n"))

print(f"User choice is {user_choice} "+game[user_choice])
comp_choice=random.randint(0,2)

print(f"Computer choice is {comp_choice} "+game[comp_choice])
if user_choice>=3 or user_choice<0:
    print("You type something invalid")
elif user_choice==0 and comp_choice==2:
    print("You Win !")
elif comp_choice==0 and user_choice==2:
    print("You Lose !")
elif comp_choice>user_choice:
    print("You Lose")
elif user_choice>comp_choice:
    print("You Win")
elif user_choice==comp_choice:
    print("It's a Draw !")

#############################   fizzbuzzz
for number in range(1,101):
    if number % 3==0 & number % 5==0:
        print("FizzBuzz")
    elif number%3==0:
        print("Fizz")
    elif number%5==0:
        print("Buzz")
    else:
        print(number)