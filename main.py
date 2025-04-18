############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
   # https://appbrewery.github.io/python-day11-demo/

#Hint 2: Read this breakdown of program requirements: 
     # http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
   # https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.


import random
from replit import clear
from art import logo
from builtins import sum

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal():
   """Returns random card from the deck of cards"""
   ran = random.choice(cards)
   return ran


def total(he):
   tot = sum(he)
   if tot == 21 and len(he) == 2:
      return 0
   if 11 in he and tot>21:
      he.remove(11)
      he.append(1)
   return tot
   
def play_game():
   print(logo)
 
   user_cards = []
   computer_cards = []
   
   for _ in range(2):
      user_cards.append(deal())
      computer_cards.append(deal())

   
   def compare(val1,val2):
      if val1>21 or val2>21:
         return "The score is exceeded"
   
      if val1 == val2:
         return "Draw!"
      elif val1 == 0:
         return "You have wom the game!"
      elif val2 == 0:
         return "You have lost the game!"
      elif val1 > 21:
         return "You went over. You lose"
      elif val2 > 21:
         return "Opponent went over. You win"
      elif val1 > val2:
         return "Congrats! You have won!"
      else:
         return "You lose"

   
   true = True   
   while true:
      
      print(f"Your cards: {user_cards}, current score: {total(user_cards)}")
      print(f"Computer's first card: {computer_cards[0]}")
      
      val1 = total(user_cards)
      val2 = total(computer_cards)
      if val1 == 0 or val2 == 0 or val1>21:
         print("Game over!")
         true = False
      else:
         continue1 = input("Do you want to continue. Type 'y' to continue or 'n' to stop: ")
         if continue1 == 'y':
            # he3 = random.choice(cards)
            # print(he3)
            user_cards.append(deal())
            print(user_cards)
            val1 = total(user_cards)
            print(val1)
            he5 = compare(val1,val2)
            # print(he5)
         else:
            # computer_cards.append(deal())
            print(computer_cards)
            he5 = compare(val1,val2)
            print(he5)
            true = False

      while val2 != 0 and val2 < 17:
         computer_cards.append(deal())
         val2 = total(computer_cards)
         print(val2)

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
   clear()
   play_game()


# def deal():
#    user = []
#    for _ in range(2):
#       user1 = random.choice(cards)

#    user.append(user1)
#       # user2 = random.choice(cards)
#    return user#,user2

# ran = deal()
# print(ran)
   # total = sum(user_card)
   # print(total)
   # total1 = sum(computer_card)
   # print(total1)
   # for j in user_card:
   #    i+=j
   # print(i)

# for i in range(len(cards)):
#   li = random.choice(cards)
# print(f'{[li]}')