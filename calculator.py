# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 12:18:13 2021

@author: Devesh Prasad
"""

############  Advanced leap Year

# def is_leap(year):
    
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True
#       else:
#         return False
#     else:
#       return True
#   else:
#     return False

# def days_in_month(year,month):
    # if month>12 or month<1:
    #     return "Invalid Input"
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
#   if is_leap(year) and month== 2:
#       return 29
#   return month_days[month-1]
  
  

# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)

############# Calculator

def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
operations={"+":add,"-":subtract,"*":multiply,"/":divide}
def calculator():
    num1=float(input("What is first No :  "))
    for symbol in operations:
        print(symbol)
    should_continue=True
    while should_continue:
        operation_symbol=input("Pick An Operation  :")
        
        num2=float(input("What is Next No :  "))
        
        calculation_function=operations[operation_symbol]
        answer=calculation_function(num1, num2)
        # print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        # operation_symbol=input("Pick another operations :")
        # num3= int(input("What is next number :"))
        # calculation_function=operations[operation_symbol]
        # second_answer=calculation_function(calculation_function(num1,num2), num3)
        
        print(f" {num1} {operation_symbol} {num2} = {answer}")
        if input(f"Type 'y'to continue calculating with {answer} or 'n' to exit :  ")=="y":
            num1=answer
        else:
            should_continue=False
            calculator()   
calculator()