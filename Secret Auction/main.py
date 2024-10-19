from turtle import clear
from art import logo

print(logo)

bids = {}
bidding_finished = False

def find_highest_bid(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bidding_amount = bidding_record[bidder]
    if bidding_amount > highest_bid:
      highest_bid = bidding_amount
      winner = bidder
  print(f"The winner is {winner}. With a highest bid of ${highest_bid}.")

while not bidding_finished:
  name = input("What is your name? ")
  bid = int(input("What is your bid? $"))
  bids[name] = bid
  
  should_continue = input("Are there any bids? Type 'yes' or 'no': ").lower()
  if should_continue == "no":
    find_highest_bid(bids)
    bidding_finished = True
  elif should_continue == "yes":
    clear()
  