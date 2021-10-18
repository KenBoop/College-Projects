#ken dompier

#problem 1

def prime(posInt):
    if posInt == 2:
        return True
    else:
        if posInt % 2 == 1:
            return True
        else:
            return False

#problem 2
    
def evenrow(l):
    for lists in l:
        numbers = 0
        counter = 0
        for item in lists:
            numbers = numbers + item
            counter = counter + 1
            if counter == len(lists):
                if numbers % 2 != 0:
                    return False
    return(True)

#problem 3
    
def lookup(fileName):
    dict = {}
    fileO = open(fileName, 'r')
    for line in fileO:
        counter = 0
        name = ''
        for word in line.split():
            counter = counter + 1
            if counter < 3:
                name = name + word + ' '
            if counter == 3:
                dict[name] = word
    while True:
        firstName = eval(input("Enter the first name: "))
        lastName = eval(input("Enter the last name: "))
        fullName = firstName + ' ' + lastName + ' '
        print(dict[fullName])
    
    

#problem 4
    
def crsp():
    import random
    rounds = random.choice(range(1,11))
    print('You will be playing ' + str(rounds) + ' rounds.')
    playerScore = 0
    computerScore = 0
    counter = 0
    while True:
        while True:
            player1Choice = eval(input("Player 1 choose R,P, or S: "))
            player1Choice = player1Choice.upper()
            if player1Choice not in "RPS":
                print('Invalid input')
                continue
            else:
                break
        computerChoice = random.choice(['R','S','P'])
        #negative 1 results
        if player1Choice == "S" and computerChoice == "P":
            playerScore = playerScore + 1
            print('Player 1 won!')
        elif player1Choice == "P" and computerChoice == "R":
            playerScore = playerScore + 1
            print('Player 1 won!')
        elif player1Choice == "R" and computerChoice == "S":
            playerScore = playerScore + 1
            print('Player 1 won!')

        #positive 1 results
        if player1Choice == "P" and computerChoice == "S":
            computerScore = computerScore + 1
            print('Computer won!')
        elif player1Choice == "R" and computerChoice == "P":
            computerScore = computerScore + 1
            print('Computer won!')
        elif player1Choice == "S" and computerChoice == "R":
            computerScore = computerScore + 1
            print('Computer won!')
            
        #tie results
        if player1Choice == computerChoice:
            print('Tie!')
        counter = counter + 1
        if counter == rounds:
            break
    if computerScore > playerScore:
        print('Computer is the winner!')
    elif computerScore < playerScore:
        print("You are the winner!")
    else:
        print("Nobody is a winner")


