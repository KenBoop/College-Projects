from tkinter import Tk,Label, Entry, Button, END
from tkinter.messagebox import showinfo

root = Tk()

def compute():
    #sets the inputs as global variables so the program can have the inputs in the function
    global heightEnt
    global weightEnt
    #obtains the inputs
    height = heightEnt.get()
    weight = weightEnt.get()

    #calculates bmi, assuming the inputs are imperial 
    bmi = (int(weight) * 703) / (int(height) ** 2)
    #rounds down bmi using the round function
    roundedBMI = round(bmi, 1)

    #creates a textbox 
    showinfo(message = 'Your BMI is {}'.format(roundedBMI))
    
    #deletes the inputs
    heightEnt.delete(0, END)
    weightEnt.delete(0, END)


#creates the text next to the entry object, asking for height
label = Label(root, text='Enter your height:')
label.grid(row=0, column=0)

#creates the text next to the entry object, asking for weight
label = Label(root, text='Enter your weight:')
label.grid(row=1, column=0)

#entry objects for height and weight
heightEnt = Entry(root)
heightEnt.grid(row=0, column=1)


weightEnt = Entry(root)
weightEnt.grid(row=1, column=1)

button = Button(root, text='Compute BMI', command=compute) 
button.grid(row=2, column=0, columnspan=2)

root.mainloop()

#Q2 Blackjack

import random
class Card:
    'class that represents a card'
    
    def __init__(self, rank, suit):
        'initilize card rank and suit'
        self.rank = rank
        self.suit = suit
        
    def setRank(self, rank):
        'set the rank of the card'
        self.rank = rank

    def setSuit(self, suit):
        'set the suit of the card'
        self.suit = suit

    def getRank(self):
        'returns the rank of the card'
        return self.rank
    
    def getSuit(self):
        'returns the suit of the card'
        return self.suit

#b) Implement class called Deck - Check Slides from Chapter 8

class Deck:
    'class that represents the deck'

    # ranks and suits are Deck class variables
    ranks = {'2','3','4','5','6','7','8','9','10','J','Q','K','A'}
    # suits is a set of 4 Unicode symbols representing the 4 suits 
    suits = {'\u2660', '\u2661', '\u2662', '\u2663'}

    def __init__(self):
        #list to store all the cards
        self.deck = []
        for suit in Deck.suits: 
                    for rank in Deck.ranks: 
                        # adds a card with a rank and suit to deck
                        self.deck.append(Card(rank,suit))

    def dealCard(self):
            'deal (pop and return) card from the top of the deck'
            return self.deck.pop()
        
    def shuffle(self):
        'shuffle the deck'
        random.shuffle(self.deck)

def blackjack(): #switch to blackjack later
  #stores the scores
  playerScore = 0 
  dealerScore = 0
  #counts number of ace cards
  playerAce = 0
  dealerAce = 0
  #initiates the deck
  deck = Deck()
  #shuffles deck multiple times to make sure its really random
  counter = 0
  while counter < 50:
    deck.shuffle()
    counter = counter + 1

  print("Your cards are:")
  #CARD 1
  card = deck.dealCard()
  print(card.getRank(), card.getSuit())
  #adds card to player's score
  #number cards
  if card.getRank() in ('2','3','4','5','6','7','8','9','10'):
    playerScore = playerScore + int(card.getRank())
  #JQK cards
  elif card.getRank() in ('J','Q','K'):
    playerScore = playerScore + 10
  #ace cards
  else:
    playerScore = playerScore + 11
    #adds 1 ace card to keep track of it before changing it to a 1
    playerAce = playerAce + 1

  #CARD 2
  card = deck.dealCard()
  print(card.getRank(), card.getSuit())
  #adds card to player's score
  if card.getRank() in ('2','3','4','5','6','7','8','9','10'):
    playerScore = playerScore + int(card.getRank())
  elif card.getRank() in ('J','Q','K'):
    playerScore = playerScore + 10
  else:
    playerScore = playerScore + 11
    playerAce = playerAce + 1

    #special code for rare case of 2 aces
    if playerAce == 2:
      playerAce = playerAce - 1
      playerScore = playerScore - 10 #subtract 10 to turn ace into 1
    
  while True:
    try:
      answer = eval(input("Would you like to hit or stand? "))
      #if player chooses hit, assign another card to them
      if answer.lower() == "hit":
        card = deck.dealCard()
        print(card.getRank(), card.getSuit())
        if card.getRank() in ('2','3','4','5','6','7','8','9','10'):
          playerScore = playerScore + int(card.getRank())
        elif card.getRank() in ('J','Q','K'):
          playerScore = playerScore + 10
        else:
          playerScore = playerScore + 11
          playerAce = playerAce + 1


      #checks if player went over 21, otherwise return to midgame 
        if playerScore > 21:
          #if player has ace, its not a game over
          if playerAce > 0:
            playerScore = playerScore - 10
            playerAce = playerAce - 1
          else:
            print("Dealer wins!")
            return -1
        #if it isnt over 21, let input loop continue
        else:
          continue

      elif answer.lower() == "stand":
        break
    #deals with exceptions and inputs that aren't 'hit' or 'stand'
      else:
        print("Invalid input")
        continue
    except:
      print("Must be a string")

  #once the input loop breaks, the dealer is given cards
  print("Dealer cards are:")
  #CARD 1
  card = deck.dealCard()
  print(card.getRank(), card.getSuit())
  #adds card to dealer's score
  if card.getRank() in ('2','3','4','5','6','7','8','9','10'):
    dealerScore = dealerScore + int(card.getRank())
  elif card.getRank() in ('J','Q','K'):
    dealerScore = dealerScore + 10
  else:
    dealerScore = dealerScore + 11
    dealerAce = dealerAce + 1

  #CARD 2
  card = deck.dealCard()
  print(card.getRank(), card.getSuit())
  #adds card to dealer's score
  if card.getRank() in ('2','3','4','5','6','7','8','9','10'):
    dealerScore = dealerScore + int(card.getRank())
  elif card.getRank() in ('J','Q','K'):
    dealerScore = dealerScore + 10
  else:
    dealerScore = dealerScore + 11
    dealerAce = dealerAce + 1
    #special code for rare case of 2 aces
    if dealerAce == 2:
      dealerAce = dealerAce - 1
      dealerAce = dealerAce - 10 #subtract 10 to turn ace into 1

  #while true keeps the dealer active if they get an ace, otherwise the program will hang after the last if check to see if the dealerscore is > 21 and an ace card gets rid of it
  while True: 
    if dealerScore < 17:
      while dealerScore < 17:
        card = deck.dealCard()
        print(card.getRank(), card.getSuit())
        #adds card to dealer's score
        if card.getRank() in ('2','3','4','5','6','7','8','9','10'):
            dealerScore = dealerScore + int(card.getRank())
        elif card.getRank() in ('J','Q','K'):
          dealerScore = dealerScore + 10
        else:
          dealerScore = dealerScore + 11
          dealerAce = dealerAce + 1
    
    if 17 <= dealerScore < 21:
      if dealerScore < playerScore:
        print("Player wins!")
        return 1
      elif dealerScore == playerScore:
        print("Tie!")
        return 0
      else:
        print("Dealer wins!")
        return -1 
    
    if dealerScore > 21:
      if dealerAce > 0:
          dealerScore = dealerScore - 10
          dealerAce = dealerAce - 1
          continue
      else:
        print("Player wins!")
        return 1
