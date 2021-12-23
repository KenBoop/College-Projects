from tkinter import *
from tkinter.messagebox import showinfo
import random

'''Card Class as seen in slides'''
class Card:
    'class that represents a card'
    def __init__(self, rank, suit):
        'initilize card rank and suit'
        self.rank = rank
        self.suit = suit
        
    def getCard(self):
        return self
        
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

    '''These are so that the card displays properly in the gui'''
    
    def __repr__(self):
        return '({},{})'.format(self.rank, self.suit)
    
    def __str__(self):
        return('{} {}').format(self.rank, self.suit)

'''Deck Class as seen in slides'''
class Deck:
    'class that represents the deck'
    ranks = {'2','3','4','5','6','7','8','9','10','J','Q','K','A'}
    suits = {'\u2660', '\u2661', '\u2662', '\u2663'}

    def __init__(self):
        self.deck = []
        for suit in Deck.suits: 
                    for rank in Deck.ranks: 
                        self.deck.append(Card(rank,suit))

    def dealCard(self):
            'deal (pop and return) card from the top of the deck'
            return self.deck.pop()
        
    def shuffle(self):
        'shuffle the deck'
        random.shuffle(self.deck)

'''The initialize  Tk object is the winow where the user enters the number of players andd rounds they have/wish to play'''

initialize = Tk()
initialize.geometry('400x170')
initialize['background'] = '#b5b5b5'



titleLabel = Label(initialize, text = 'Enter Initial Conditions', font = ('bold', 24), background = '#b5b5b5')
titleLabel.pack()

roundEntryLabel = Label(initialize, text = 'Number of Rounds:',  relief = 'flat', borderwidth = 4, background = '#b5b5b5')
roundEntryLabel.place(x = 30, y = 40)

roundEntry = Entry(initialize)
roundEntry.place(x = 180, y = 40)

playerNumberLabel = Label(initialize, text = 'Number of Players:', relief = 'flat', borderwidth = 4, background = '#b5b5b5')
playerNumberLabel.place(x = 30, y = 70)

playerEntry = Entry(initialize)
playerEntry.place(x = 180, y = 70)

'''This function submit gets values for the number of rounds and the number of players the game will have'''

#multiplayer counters
playersCount = 1
playerRound = 1 #keeps track of which player the round belongs to

#round counters
playRounds = 0
roundCounter = 0

scoreboard = {}

def submit():
    global playRounds
    global players
    rounds = roundEntry.get()
    playRounds = rounds
    players = playerEntry.get()
    playersCount = players

    #sets the amount of rounds by multiplying amount of other players
    if int(playersCount) > 1:
        playRounds = int(playRounds) * int(playersCount)
        roundStart = 1


    roundEntry.delete(0, 100)
    playerEntry.delete(0, 100)
    initialize.destroy()

submitButton = Button(initialize, text = 'Submit', command = submit, height = 1, width = 10)
submitButton.place(x = 150, y = 110)

initialize.mainloop()

playersCount = players #without this, the player turn messages don't work because playersCount becomes 0.


while True:   
    if roundCounter == int(playRounds): #checks after reopening window to see if the program has played enough rounds
        scoreMessage = ''
        for element in scoreboard: #for each key in dictionary, create a line for the scoreboard
            scoreMessage = scoreMessage + 'Player {} scored: {} \n'.format(element, scoreboard[element])
        break
    else:
        roundCounter = roundCounter + 1

    '''Sets up the deck internally before displaying the UI'''
    playerAmount = 0
    dealerAmount = 0

    playerAce = 0
    dealerAce = 0

    #deck shuffler
    deck = Deck()
    shuffleCounter = 0
    while shuffleCounter < 50:
        deck.shuffle()
        shuffleCounter = shuffleCounter + 1

    #CARD 1
    card = deck.dealCard()
    a = card #adds card to visual deck
    
    #numbered cards
    if card.getRank() in ('2','3','4','5','6','7','8','9','10'):
        playerAmount = playerAmount + int(card.getRank())
    #JQK cards
    elif card.getRank() in ('J','Q','K'):
        playerAmount = playerAmount + 10
    #ace cards
    else:
        playerAmount = playerAmount + 11
        #adds 1 ace card to keep track of it before changing it to a 1
        playerAce = playerAce + 1

    #CARD 2
    card = deck.dealCard()
    b = card #adds card to visual deck

    if card.getRank() in ('2','3','4','5','6','7','8','9','10'):
        playerAmount = playerAmount + int(card.getRank())
        
    elif card.getRank() in ('J','Q','K'):
        playerAmount = playerAmount + 10
        
    else:
        playerAmount = playerAmount + 11
        playerAce = playerAce + 1

        #in case the player gets 2 aces
        if playerAce == 2:
          playerAce = playerAce - 1
          playerAmount = playerAmount - 10 #subtract 10 to turn ace into 1
          
        
    '''UI'''
    
    root = Tk()


    root.geometry('400x600')
    root['background'] = '#b5b5b5'
    cardBack = PhotoImage(file = 'cardBack (1).gif')

    '''This section contains all labels that represent the name of the game, the image for the dealer cards and the deck, the image for the table, all visual stuff that does not  impact the code'''

    nameLabel = Label(root, text = 'Blackjack', font = ('bold', 24), background = '#b5b5b5')
    nameLabel.pack()

    dealerCard1 = Label(root, image = cardBack, width = 52, height = 91, borderwidth = 0)
    dealerCard1.place(x = 142, y = 54)

    dealerCard2 = Label(root, image = cardBack, width = 52, height = 91, borderwidth = 0)
    dealerCard2.place(x = 206, y = 54)

    Image = PhotoImage(file = 'newTable.gif')

    tableImage = Label(root, image = Image, width = 250, height = 125, borderwidth = 0)
    tableImage.place(x = 70, y = 155)

    deckPic = Label(root, image = cardBack, width = 52, height = 91, borderwidth = 0)
    deckPic.place(x = 330, y = 170)

    '''This section includes the player's card frame, the buttons for viewing next and previous cards, and functions assosciated for hit, stand, next and previous cards. The hit and stand functions will replace the input sections from the blackjack version we made in class. Note, these are placeholder functions at the moment, just so that I could get the widgets working before we stitch it all together'''


    '''visual playerHand for UI'''

    playerHand = [a,b]

    '''this counter keeps track of which card in the list of player cards is being displaced'''

    handCounter = 0

    '''Stringvar is for kinter so that the card can be updated as the buttons are placed'''

    currentCard = StringVar()

    currentCard.set(playerHand[handCounter].getCard())

    playerCard = Label(root, width = 10, height = 10, relief = 'ridge', borderwidth = 3)
    playerCard.place(x = 95 , y = 290)

    scorePlayer = playerRound #saves the playerRound before it changes for next player message. this allows the scoreboard system to function. 

    #checks whether to display player round messages or not
    if int(playersCount) > 1:
        if int(playerRound) == int(playersCount): #if the round number is equal to playercount, reset it so its player 1 again
            showinfo(message = "Player {}'s turn!".format(playerRound))
            playerRound = 1
        else:
            showinfo(message = "Player {}'s turn!".format(playerRound))
            playerRound = int(playerRound) + 1

    def nextCard():
        global handCounter
        if handCounter == (len(playerHand)-1):
            handCounter += 0
            currentCard.set(playerHand[handCounter].getCard())        
        else:
            handCounter += 1
            currentCard.set(playerHand[handCounter].getCard())

        if "10" in currentCard.get():
            cardLabelBR.place(x = 150, y = 430)
        else:
            cardLabelBR.place(x = 158, y = 430)

    playerNext = Button(root,  text = 'Next Card', command = nextCard, height = 2, width = 10)
    playerNext.place(x = 210, y = 290)

    def previousCard():
        global handCounter
        if handCounter == 0:
            handCounter += 0
            currentCard.set(playerHand[handCounter].getCard())
        else:
            handCounter -= 1
            currentCard.set(playerHand[handCounter].getCard())

        if "10" in currentCard.get():
            cardLabelBR.place(x = 150, y = 430)
        else:
            cardLabelBR.place(x = 158, y = 430)
        
    playerPrevious = Button(root, text = 'Previous Card', command = previousCard, height = 2, width = 10)
    playerPrevious.place(x = 210, y = 355)

    placeHolderTotal = playerAmount

    totalValue = Label(root, text = 'Total: ' +  str(placeHolderTotal), height = 2, width = 10, borderwidth = 1, relief = 'solid')
    totalValue.place(x = 210, y = 420)

    def updateTotal():
        totalValue.configure(text='Total: ' + str(playerAmount))

    '''These two labels are for the card display in the top left and bottom right of the card'''

    cardLabelTL = Label(root, textvariable = currentCard, font = ('bold', 12))
    cardLabelTL.place(x = 100, y = 295)

    cardLabelBR = Label( root, textvariable = currentCard, font = ('bold', 12))
    if "10" in currentCard.get(): #fixes visual glitches for specific cards
        cardLabelBR.place(x = 150, y = 430)
    else:
        cardLabelBR.place(x = 158, y = 430)
        
    def hit():
      global playerAmount
      global playerAce
      card = deck.dealCard()
      playerHand.append(card)
      if card.getRank() in ('2','3','4','5','6','7','8','9','10'):
        playerAmount = playerAmount + int(card.getRank())
      elif card.getRank() in ('J','Q','K'):
        playerAmount = playerAmount + 10
      else:
        playerAmount = playerAmount + 11
        playerAce = playerAce + 1
      updateTotal()
      
      #checks if player went over 21 
      if playerAmount > 21:
        #if player has ace, remove 10 before checking to see if the dealer wins
        if playerAce > 0:
          playerAmount = playerAmount - 10
          if playerAmount > 21: #added this if player has 21 and gets an ace card with a hit, which breaks the game by saying you have a total of 22
            showinfo(message = "Dealer wins!")
            if int(scorePlayer) not in scoreboard: #adds 0 to scoreboard if player isn't on the scoreboard yet
                scoreboard[int(scorePlayer)] = 0
            root.destroy()
          playerAce = playerAce - 1
          updateTotal()
        else:
            showinfo(message = "Dealer wins!")
            if int(scorePlayer) not in scoreboard:
                scoreboard[int(scorePlayer)] = 0
            root.destroy()
      else:
        updateTotal()
          
        
    hitButton = Button(root, text = 'Hit', command = hit, height = 2, width = 10, borderwidth = 1)
    hitButton.place(x = 95, y = 470)


    def stand():
        global playerAmount
        global dealerAmount
        global dealerAce
        
        print("Dealer's cards are: ")
        while True: 
          if dealerAmount < 17:
            while dealerAmount < 17:
              card = deck.dealCard()
              print(card.getRank(), card.getSuit()) 
              #adds card to dealer's amount
              if card.getRank() in ('2','3','4','5','6','7','8','9','10'):
                dealerAmount = dealerAmount + int(card.getRank())
              elif card.getRank() in ('J','Q','K'):
                  dealerAmount = dealerAmount + 10
              else:
                dealerAmount = dealerAmount + 11
                dealerAce = dealerAce + 1
          if 17 <= dealerAmount <= 21:
            if dealerAmount < playerAmount:
              showinfo(message = "Player wins!")
              #playerRound dictionary
              if int(scorePlayer) not in scoreboard:
                    scoreboard[int(scorePlayer)] = 1
              else:
                  tempScore = scoreboard[int(scorePlayer)]
                  tempScore = tempScore + 1
                  scoreboard[int(scorePlayer)] = tempScore
              root.destroy()
              break
              
              root.destroy()
              break
            elif dealerAmount == playerAmount:
              showinfo(message = "Tie!")
              if int(scorePlayer) not in scoreboard:
                    scoreboard[int(scorePlayer)] = 0 
              root.destroy()
              break
            else:
              showinfo(message = "Dealer wins!")
              if int(scorePlayer) not in scoreboard:
                    scoreboard[int(scorePlayer)] = 0
              root.destroy()
              break

            
          if dealerAmount > 21:
            if dealerAce > 0:
              dealerAmount = dealerAmount - 10
              dealerAce = dealerAce - 1
              continue
            else:
              showinfo(message = "Player wins!")
              #scoreboard dictionary 
              if int(scorePlayer) not in scoreboard:
                    scoreboard[int(scorePlayer)] = 1
              else:
                  tempScore = scoreboard[int(scorePlayer)]
                  tempScore = tempScore + 1
                  scoreboard[int(scorePlayer)] = tempScore
              root.destroy()
              break
            

    standButton = Button(root, text = 'Stand', command = stand, height = 2, width = 10, borderwidth = 1)
    standButton.place(x = 210, y = 470)
    
    
    root.mainloop()

#scoreboard
    
initialize = Tk()
initialize.geometry('400x170')
initialize['background'] = '#b5b5b5'

scoreLabel = Label(initialize, text = 'Scoreboard', font = ('bold', 24), background = '#b5b5b5')

roundEntryLabel = Label(initialize, text = scoreMessage, font = (10), relief = 'flat', borderwidth = 4, background = '#b5b5b5', justify = "center")
roundEntryLabel.place(x = 135, y = 40)

scoreLabel.pack()
initialize.mainloop()
