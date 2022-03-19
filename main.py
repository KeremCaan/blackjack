from art import logo
import random
from replit import clear

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cardsinhand):

  if sum(cardsinhand) == 21 and len(cardsinhand) == 2:
    return 0
  if 11 in cardsinhand and sum(cardsinhand) > 21:
    cardsinhand.remove(11)
    cardsinhand.append(1)
  return sum(cardsinhand)

def compare(user_score, computer_score):
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose "
  if user_score == computer_score:
    return "Draw "
  elif computer_score == 0:
    return "Lose, opponent has Blackjack "
  elif user_score == 0:
    return "Blackjack !!! "
  elif user_score > 21:
    return "You went over. You lose "
  elif computer_score > 21:
    return "Opponent went over. You win "
  elif user_score > computer_score:
    return "You win "
  else:
    return "You lose "

def play_game():

  print(logo)

  user_cards = []
  computer_cards = []
  is_game_over = False

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())


  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"   Your cards: {user_cards}, current score: {user_score}")
    print(f"   Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      wants_to_continue = input("Type 'y' to get another card, type 'n' to pass: ")
      if wants_to_continue == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"   Your final hand: {user_cards}, final score: {user_score}")
  print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()
