import random

def deal_card():
  cards = [11, 2, 3 ,4 ,5 ,6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculation_start(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0

  if 11 in cards and sum(cards) == 21:
    cards.remove(11)
    cards.append(1)

  return sum(cards)

def compare(u_score, c_score):
  if u_score == c_score:
    return "Draw"
  elif c_score == 0:
    return "You lose, computer has a blackjack!"
  elif u_score == 0:
    return "You win with a blackjack!"
  elif u_score > 21:
    return "You went over. You lose!"
  elif c_score > 21:
    return "Computer went over. You win!"
  elif u_score > c_score:
    return "You win!"
  else:
    return "You lose!"

user_cards = []
computer_cards = []
computer_score = -1
user_score = -1
game_over = False

for _ in range(2):
  user_cards.append(deal_card())
  computer_cards.append(deal_card())

while not game_over: 
  user_score = calculation_start(user_cards)
  computer_score = calculation_start(computer_cards)
  
  print(f"Your cards are: {user_cards}. Current score is: {user_score}")
  print(f"Computer's first card is: {computer_cards[0]}")
  
  if user_score == 0 or computer_score == 0 or user_score > 21:
    game_over = True
  else:
    user_should_deal = input("Type 'y' to deal another card. Otherwise type 'n': ").lower()
    if user_should_deal == 'y':
      user_cards.append(deal_card())
    else:
      game_over = True

while computer_score != 0 and computer_score < 17:
  computer_cards.append(deal_card())
  computer_score = calculation_start(computer_cards)

print(f"\nYour final hand is: {user_cards}. Final score is: {user_score}")
print(f"Computer's final hand is: {computer_score}. Final score is: {computer_score}")
print(compare(user_score, computer_score))
  