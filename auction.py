# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 00:09:44 2021

@author: Devesh Prasad
"""

############## AUCTION
bids={}
bidding_finished=False
def find_highest_bidder(bidding_record):
    highest_bid=0
    winner=""
    for bidder in bidding_record:
        bid_amount=bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid=bid_amount
            winner=bidder
    print(f"The Winner is {winner} with a bid of ${highest_bid}")
while not bidding_finished:
    name=input("What is your name ? ")
    price=int(input("What is your bidding price ? $"))
    bids[name]=price
    should_continue=input("are there any new bidders yes or no ? ")
    if should_continue=="no":
        bidding_finished=True
        find_highest_bidder(bids)
   