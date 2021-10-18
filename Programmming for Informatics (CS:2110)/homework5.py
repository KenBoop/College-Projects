# Q1 
def fcopy(file1, file2):
    characterCount = 0
    f1 = open(file1,'r')
    f2 = open(file2, 'w')
    for line in f1:
        f2.write(line)
        characterCount = characterCount + len(line)       
    f1.close()
    f2.close()
    return(characterCount)
        

#characterCount = fcopy("example.txt", "output.txt")
#print(characterCount)
# Q2 
def distribution(file1):
    aPlus = 0
    aCount = 0
    aMinus = 0

    bPlus = 0
    bCount = 0
    bMinus = 0

    cPlus = 0
    cCount = 0
    cMinus = 0

    dPlus = 0
    dCount = 0
    dMinus = 0

    fCount = 0
    
    f1 = open(file1, 'r')
    for line in f1:
        for word in line.split():
            if 'A' in word:
                if '+' in word:
                    aPlus = aPlus + 1
                elif '-' in word:
                    aMinus = aMinus + 1
                else:
                    aCount = aCount + 1
            elif 'B' in word:
                if '+' in word:
                    bPlus = bPlus + 1
                elif '-' in word:
                    bMinus = bMinus + 1
                else:
                    bCount = bCount + 1
            elif 'C' in word:
                if '+' in word:
                    cPlus = cPlus + 1
                elif '-' in word:
                    cMinus = cMinus + 1
                else:
                    cCount = cCount + 1
            elif 'D' in word:
                if '+' in word:
                    dPlus = aPlus + 1
                elif '-' in word:
                    dMinus = aMinus + 1
                else:
                    dCount = dCount + 1
            else:
                fCount += 1
        if aPlus == 1:
             print('1 student got A+')
        elif aPlus > 1:
            print(str(aPlus) + ' students got A+')
#a         
        if aCount == 1:
             print('1 student got A')
        elif aCount > 1:
            print(str(aCount) + ' students got A')
            
        if aMinus == 1:
             print('1 student got A-')
        elif aMinus > 1:
            print(str(aMinus) + ' students got A-')
            
        if bPlus == 1:
             print('1 student got B+')
        elif bPlus > 1:
            print(str(bPlus) + ' students got B+')
#b           
        if bCount == 1:
             print('1 student got B')
        elif bCount > 1:
            print(str(bCount) + ' students got B')
            
        if bMinus == 1:
             print('1 student got B-')
        elif bMinus > 1:
            print(str(bMinus) + ' students got B-')
#c
        if cPlus == 1:
             print('1 student got C+')
        elif cPlus > 1:
            print(str(CPlus) + ' students got C+')
            
        if cCount == 1:
             print('1 student got C')
        elif cCount > 1:
            print(str(cCount) + ' students got C')
            
        if cMinus == 1:
             print('1 student got C-')
        elif cMinus > 1:
            print(str(cMinus) + ' students got C-')
#d
        if dPlus == 1:
             print('1 student got D+')
        elif dPlus > 1:
            print(str(dPlus) + ' students got D+')
            
        if dCount == 1:
             print('1 student got D')
        elif dCount > 1:
            print(str(DCount) + ' students got D')
            
        if dMinus == 1:
             print('1 student got D-')
        elif dMinus > 1:
            print(str(dMinus) + ' students got D-')

#f
        if fCount == 1:
            print('1 student got F')
        elif fCount > 1:
            print(str(fCount) + ' students got F')
            

# Q3    
def censor(file1):
    f1 = open(file1, 'r')
    emptyString = ''
    for line in f1:
        for word in line.split():
            if len(word) == 4:
                emptyString = emptyString +  'xxxx '
            else:
                emptyString = emptyString + word + ' '
    f2 = open( 'censored.txt','a')
    for word in emptyString:
        f2.write(word)

# Q4
def intersect(list1,list2):
    comboList = []
    if list1 == list2:
        return("Can't be duplicate values.")
    for item in list1:
        if item in list2:
            comboList.append(item)
    return(comboList)
            
# Q5    
def rsp():
    while True:
        player1Choice = eval(input("Player 1 choose R,P, or S:  "))
        player1Choice = player1Choice.upper()
        if player1Choice not in "RPS":
            print('Invalid input')
            continue
        else:
            break
    
    spaceCounter = 0
    while spaceCounter < 100: #added this to hide the first player's choice from the second player
        print('''                        ''')
        spaceCounter = spaceCounter + 1
        
    while True:  
        player2Choice = eval(input("Player 2 choose R, P, or S: "))
        player2Choice = player2Choice.upper()
        if player2Choice not in "RPS":
            print('Invalid input')
            continue
        else:
            break
        
    #negative 1 results
    if player1Choice == "S" and player2Choice == "P":
        return(-1)
    elif player1Choice == "P" and player2Choice == "R":
        return(-1)
    elif player1Choice == "R" and player2Choice == "S":
        return(-1)

    #positive 1 results
    if player1Choice == "P" and player2Choice == "S":
        return(1)
    elif player1Choice == "R" and player2Choice == "P":
        return(1)
    elif player1Choice == "S" and player2Choice == "R":
        return(1)

    #0 results
    if player1Choice == player2Choice:
        return(0)


