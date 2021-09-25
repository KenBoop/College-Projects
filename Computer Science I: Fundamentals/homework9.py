import tkinter
import random

window = tkinter.Tk()

#history keeper
problemListAny = []
problemListAdd = []
problemListSub = []
problemListMult = []
problemListDiv = []


# counters 
global incorrect
incorrect = 0

global correct
correct = 0

global attempts
attempts = 0

#single problem incorrect count
global singleProblemIC
singleProblemIC = 0

def quit():
  window.destroy()
  if correct + incorrect == 0:
    totalGuesses = 0
  else:
    totalGuesses = correct / (correct + incorrect)

  print("You have attempted {} problems. You got {} correct and have an average number of {} total guesses per problem.".format(attempts, correct, totalGuesses))

def checkGuess():
  global numToCheck
  guessAsString = guessEntry.get()
  guess = int(guessAsString)
  if(guess == numToCheck):
    label.configure(text = "That's correct!")
    guessEntry.delete(0, tkinter.END)
    button1.configure(text = "Choose a new problem", command = newProblem)
    global correct
    correct = correct + 1
  else:
    global incorrect
    incorrect = incorrect + 1

    global singleProblemIC
    singleProblemIC = singleProblemIC + 1

    label.configure(text = "Incorrect! Failed attempts: {}".format(singleProblemIC))
    guessEntry.delete(0, tkinter.END)


#checker 
numToCheck = None

#entry
guessEntry = tkinter.Entry(window)
guessEntry.pack(side=tkinter.BOTTOM)

selectedButtonText = "one"
choiceVar = tkinter.IntVar()
choiceVar.set(1)

def radioButtonChosen():
    if choiceVar.get() == 1:
      anything()

    elif(choiceVar.get() == 2):
      addition()

    elif(choiceVar.get() == 3):
      subtraction()

    elif(choiceVar.get() == 4):
      multiplication()

    else:
        division()

choice1 = tkinter.Radiobutton(window, text="Anything", variable=choiceVar, value=1,command=radioButtonChosen)
choice1.pack()

choice2 = tkinter.Radiobutton(window, text="+", variable=choiceVar, value=2,command=radioButtonChosen)
choice2.pack()

choice3 = tkinter.Radiobutton(window, text="-", variable=choiceVar, value=3,command=radioButtonChosen)
choice3.pack()

choice4 = tkinter.Radiobutton(window, text="*", variable=choiceVar, value=4,command=radioButtonChosen)
choice4.pack()

choice5 = tkinter.Radiobutton(window, text="/", variable=choiceVar, value=5,command=radioButtonChosen)
choice5.pack()


label = tkinter.Label(window, text = "radio button choice is: {}".format(selectedButtonText))
label.pack()

statusLabel = tkinter.Label(window, text="You haven't made any guesses yet")
statusLabel.pack(side=tkinter.RIGHT)

def addition():
  global numToCheck
  global attempts
  global singleProblemIC
  num1 = random.randint(1,999)
  num2 = random.randint(1,999)
  
  #history check
  historyCheck = num1,num2
  if historyCheck in problemListAdd:
    while num1 and num2 in problemListAdd:
      num1 = random.randint(1,999)
      num2 = random.randint(1,999)

  numToCheck = num1 + num2
  statusLabel.configure(text="What is {} + {}".format(num1, num2))
  label.configure(text="You haven't made any guesses yet.")
  button1.configure(text="Check It", command=checkGuess)

  problemListAdd.append(historyCheck)
  attempts = attempts + 1
  singleProblemIC = 0

def subtraction():
  global numToCheck
  global attempts
  global singleProblemIC
  num1 = random.randint(2,999)
  num2 = random.randint(1,999)
  while num2 > num1:
    num2 = random.randint(1, 999)

  #history check
  historyCheck = num1,num2
  if historyCheck in problemListSub:
    while num1 and num2 in problemListSub:
      num1 = random.randint(1,999)
      num2 = random.randint(1,999)
      while num2 > num1:
        num2 = random.randint(1, 999)

  numToCheck = num1 - num2
  statusLabel.configure(text="What is {} - {}".format(num1, num2))
  label.configure(text="You haven't made any guesses yet.")
  button1.configure(text="Check It", command=checkGuess)
  attempts = attempts + 1
  singleProblemIC = 0

def multiplication():
  global numToCheck
  global attempts
  global singleProblemIC
  num1 = random.randint(1,99)
  num2 = random.randint(1,99)

  #history check
  historyCheck = num1,num2
  if historyCheck in problemListMult:
    while num1 and num2 in problemListMult:
      num1 = random.randint(1,99)
      num2 = random.randint(1,99)

  numToCheck = num1 * num2
  statusLabel.configure(text="What is {} * {}".format(num1, num2))
  label.configure(text="You haven't made any guesses yet.")
  button1.configure(text="Check It", command=checkGuess)
  attempts = attempts + 1
  singleProblemIC = 0

def division():
  global numToCheck
  global attempts
  global singleProblemIC
  num1 = random.randint(1,999)
  num2 = random.randint(1,999)
  while num1 % num2 != 0:
    num2 = random.randint(1,999)

  #history check
  historyCheck = num1,num2
  if historyCheck in problemListDiv:
    while num1 and num2 in problemListDiv:
      num1 = random.randint(1,999)
      num2 = random.randint(1,999)
      while num1 % num2 !=0:
        num2 = random.randint(1, 999)

  numToCheck = num1 / num2
  statusLabel.configure(text="What is {} / {}".format(num1, num2))
  label.configure(text= "You haven't made any guesses yet.")
  button1.configure(text= "Check It", command=checkGuess)
  attempts = attempts + 1
  singleProblemIC = 0


def anything():
  symbol = random.randint(1, 4)
  if symbol == 1:
    addition()

  elif symbol == 2:
    subtraction()

  elif symbol == 3:
    multiplication()

  else:
    division()

#buttons
button1 = tkinter.Button(window, text="Check It!", command=checkGuess)
button1.pack() 

button2 = tkinter.Button(window, text="Quit", command=quit)
button2.pack()

def newProblem():
  startGUI()


def startGUI():
    global selectedButton
    window.mainloop()

anything()
