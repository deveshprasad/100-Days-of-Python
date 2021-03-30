# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 16:15:19 2021

@author: Devesh Prasad
"""

################################# Coffee Maker
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


profit=0
def is_resource_sufficient(order_ingredients):
    """Returns if the ingredients are sufficicent or not"""
    is_enough=True
    for item in order_ingredients:
        if order_ingredients[item]>=resources[item]:
            print("Sorry ! No resources {item} to fullfil your demands !")
            return False
    return True


def process_coins():
    """Returns Total calculated from coins inserted"""
    print("Please insert coins")
    total=int(input("How many quarters ? : "))*0.25
    total+=int(input("How many dimes ? : "))*0.1
    total+=int(input("How many nickles ? : "))*0.05
    total+=int(input("How many pennies ? : "))*0.01
    return total
    

def is_transaction_succesful(money_recieved,drink_cost):
    """ Returns true if payment accepted otherwise refund is generated"""
    if money_recieved>=drink_cost:
        change=round(money_recieved-drink_cost,2)
        print(f"Here is ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry Thats's not enough money !")
        return False
    


def make_coffee(drink_name,order_ingredients):
    """Deduct the ingredients from the resource"""
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"Here is your {drink_name}")



is_on=True
while is_on:
    choice=input("What would you like to have espresso,latte,cappuccino ? ")
    if choice=="off":
        is_on=False
    elif choice=="report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee:{resources['coffee']}gm")
        print(f"Money: ${profit}")
    else:
        drink=MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment=process_coins()
            if is_transaction_succesful(payment, drink['cost']):
                make_coffee(choice,drink["ingredients"])
            