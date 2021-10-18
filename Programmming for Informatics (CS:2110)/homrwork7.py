# Lab 7
import random
# Q1
def sublist(l1,l2):
    newList = []
    newList2 = []
    #puts items in l1 into new list
    for item in l1:
        if item in l2:
            newList.append(item)
    #puts same items that are in l2 into new list in l2 order
    for item in l2:
        if item in newList:
            newList2.append(item)
    #compares order
    counter = 0
    while counter < len(newList):
        if newList[counter] != newList2[counter]:
            return False
        counter = counter + 1
    return True
        
# Q2
def names():
    namesList = []
    numbersDict = {}
    while True:
        name = eval(input('Enter next name: '))
        if len(name) == 0:
            break
        else:
            if name not in namesList:
                namesList.append(name)
            if name not in numbersDict:
                numbersDict[name] = 1
            else:
                oldNumber = numbersDict[name]
                numbersDict[name] = oldNumber + 1
            continue

    isare = ''
    student = ''
    for name in namesList:
        if numbersDict[name] < 2:
            isare = 'is'
            student = 'student'
        else:
            isare = 'are'
            student = 'students'
        print('There {} {} {} named {}'.format(isare,numbersDict[name],student, name))
              


# Q3
def craps():
    while True:
        dice1 = random.randrange(1,7)
        dice2 = random.randrange(1,7)
        #win
        if dice1 + dice2 == 7:
            return 1
        elif dice1 + dice2 == 11:
            return 1
        #lose
        if dice1 + dice2 == 2:
            return 0
        elif dice1 + dice2 == 3:
            return 0
        elif dice1 + dice2 == 12:
            return 0


def testCraps(n):
    counter = 0
    win = 0
    lose = 0
    while counter < n:
        dice1 = random.randrange(1,7)
        dice2 = random.randrange(1,7)
        #win
        if dice1 + dice2 == 7:
            win = win + 1
            counter = counter + 1
        elif dice1 + dice2 == 11:
            win = win + 1
            counter = counter + 1
        #lose
        if dice1 + dice2 == 2:
            lose = lose + 1
            counter = counter + 1
        elif dice1 + dice2 == 3:
            lose = lose + 1
            counter = counter + 1
        elif dice1 + dice2 == 12:
            lose = lose + 1
            counter = counter + 1
    return(win/counter)

