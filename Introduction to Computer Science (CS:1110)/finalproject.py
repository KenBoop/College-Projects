#part 1 cryptology
#problem 1
def caesar_encryption(string,enc_key):
  #temporary lowercase string to make checking faster
  tempString = string.lower()
  #for every character in inputted string
  for element in tempString:
    #check if the character is not within the alphabet
    if element not in "abcdefghijklmnopqrstuvwxyz":
      #result if the character is not within the alphabet
      return ('String must be alphabetic only.')
  #lowers enc_key if its its uppercase
  tempKey = enc_key.lower()
  #an ugly bunch of letters and numbers in a dictonary for picking the correct letter / correct letter shift
  letterDict = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,
'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26,1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'j',11:'k',12:'l',13:'m',14:'n',15:'o',16:'p',17:'q',18:'r',19:'s',20:'t',21:'u',22:'v',23:'w',24:'x',25:'y',
26:'z' }
  #compares the tempKey to a letter in the dictonary, then sets the corresponding defintiion as shiftNumber
  shiftNumber = letterDict[tempKey]
  #empty string for answer
  answer = ''
  #for every letter in lowercased string
  for element in tempString:
    #sets current new letter as hex number + number of shifts
    newLetter = letterDict[element] + shiftNumber
    #checks if newLetter exceeds Z 
    if newLetter > 26:
      #gets number of characters that exceed Z
      restartNumber = newLetter - 26
      #resets letter back to A (1) and adds extra shifts
      newLetter = 0 + restartNumber
    #adds newLetter to empty answer string
    answer = answer + letterDict[newLetter]
  return answer.upper()

#problem 2
def vegenere_encryption(string, string2):
  #temporary lowercase string to make checking faster
  tempString = string.lower()
  #for every character in inputted string
  for element in tempString:
    #check if the character is not within the alphabet
    if element not in "abcdefghijklmnopqrstuvwxyz":
      #result if the character is not within the alphabet
      return ('String must be alphabetic only.')
    #lowers second string if its its uppercase
    tempKey = string2.lower()
    #empty number list to put different shifts
    numberList = []
  #an ugly bunch of letters and numbers in a dictonary for picking the correct letter / correct letter shift
  letterDict = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,
'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26,1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'j',11:'k',12:'l',13:'m',14:'n',15:'o',16:'p',17:'q',18:'r',19:'s',20:'t',21:'u',22:'v',23:'w',24:'x',25:'y',
26:'z' }
  #for letter in string2 
  for element in tempKey:
    newNumber = letterDict[element]
    #appends the new shift distance
    numberList.append(newNumber)
  #empty string for answer
  answer = ''
  #counter for going through numberList
  counter = 0
  #for every letter in lowercased string      `q
  for element in tempString:
    #if the counter exceeds the length of the list - 1 (without - 1, it will cause a out of range error)
    if counter > len(numberList) - 1:
      #reset the counter back to 0
      counter = 0
    #sets the new letter to be the hex number of the current letter plus the shift the program is currently on
    newLetter = letterDict[element] + numberList[counter]
    #checks if newLetter exceeds Z 
    if newLetter > 26:
      #gets number of characters that exceed Z
      restartNumber = newLetter - 26
      #resets letter back to A (1) and adds extra shifts
      newLetter = 0 + restartNumber
    #adds 1 to counter to move onto the next shift
    counter = counter + 1
    #adds newLetter to empty answer string
    answer = answer + letterDict[newLetter]
  return answer.upper()


#part 2 boolean logic
'''
1.  a->b->c->d->e<->f v b ^ ~a ->a -> a ->b -> a 
=> a>b->c->d->e -> f -> f -> e v b ^ ~a -> a -> b -> a
#~
=> a>b->c->d->e -> f -> f -> e v b ^ (~a) -> a -> b -> a
#^
=> a>b->c->d->e -> f -> f -> e v (b ^ (~a)) -> a -> b -> a
#v
=> a>b->c->d->e -> f -> f -> (e v (b ^ (~a))) -> a -> b -> a
=> (a->(b->(c->(d->(e -> (f -> (f -> ((e v (b ^ (~a))) -> (a -> (b -> a))))))))))
=> (~a v (~b v (~c v (~d v (~e v (~f v (~f v ((~e v ~(b ^ (~a))) v (~a v (~b v a))))))))))

2. a v b ^ c v d ^ e <-> ~y -> t -> p ^ ~c -> b
=> a v b ^ c v d ^ e -> ~y ^ e -> ~y -> t -> p ^ ~c -> b
#~
=> a v b ^ c v d ^ e -> (~y) ^ e -> (~y) -> t -> p ^ (~c) -> b
#^
=> a v (b ^ c) v (d ^ e) -> ((~y) ^ e) -> (~y) -> t -> (p ^ (~c)) -> b
#v 
=> ((a v (b ^ c)) v (d ^ e)) -> ((~y) ^ e) -> (~y) -> t -> (p ^ (~c)) -> b
=> (((a v (b ^ c)) v ((d ^ e)) -> (((~y) ^ e) -> ((~y) -> (t -> (p ^ ((~c)) -> b))))))
=> ~(((a v (b ^ c)) v ((d ^ e)) -> ~(((~y) ^ e) -> (~(~y) -> (~t -> (p ^ (~(~c)) v b))))))

3. a ^ c -> b -> b -> a v b v ~c -> ~c -> ~d
#~
=> a ^ c -> b -> b -> a v b v (~c) -> (~c) -> (~d)
#^
=> (a ^ c) -> b -> b -> a v b v (~c) -> (~c) -> (~d)
#v
=> (a ^ c) -> b -> b -> ((a v b) v (~c)) -> (~c) -> (~d)
=> ((a ^ c) -> (b -> (b -> (((a v b) v (~c)) -> ((~c) -> (~d))))))
=> ~((a ^ c) v (~b v (~b v ~(((a v b) v (~c)) v (~(~c) v (~d))))))

'''
#part 3 artifical intelligence 
#problem 1
#having two variables set to None in defined function allows users to have the ability choose either 1 input or 2 inputs 
def move_range(a = None, b = None):
  #empty variable to put together the number and letter for tuple
  chessSpot = None
  #lowercases a for when its uppercased in input
  lowerCase = a.lower()
  #checks if the user did tuple, if it isn't, proceed with else statement
  if b != None:
    #creates the chessSpot
    chessSpot = lowerCase + str(b)
    #makes sure that the inputted letter and number are in chessboard range
    if lowerCase not in "abcdefgh" or b > 8:
      #if they aren't, give error
      return("Invalid input.")
  else:
    #gets rid of any spaces if the input is spaced out
    chessSpot = lowerCase.replace(" ","")
    #if the first character (letter) and second character (number) are in chessboard range. also checks if the number is beyond double digits, which returns an error too
    if lowerCase[0] not in "abcdefgh" or int(lowerCase[1:]) > 8:
      #if they aren't, give error
      return("Invalid input.")
  print('In spot' + ' ' + chessSpot)

  chessBoard = [
  ['a8','b8','c8','d8','e8','f8','g8','h8'],
  ['a7','b7','c7','d7','e7','f7','g7','h7'],
  ['a6','b6','c6','d6','e6','f6','g6','h6'],
  ['a5','b5','c5','d5','e5','f5','g5','h5'],
  ['a4','b4','c4','d4','e4','f4','g4','h4'],
  ['a3','b3','c3',"d3",'e3','f3','g3','h3'],
  ['a2','b2','c2','d2','e2','f2','g2','h2'],
  ['a1','b1','c1','d1','e1','f1','g1','h1']
  ]
  #counts each element in the list 
  counter = 0
  #when switch hits 1, end the for loop
  switch = 0
  #for each list in the matrix
  for element in chessBoard:
    #while the counter is less than 8 means while the loop hasn't reached [letter]8 on the chessboard
    while counter < 8:
      #if the loop found the matching chess input  
      if element[counter] == chessSpot:
        listSpot = element[counter]
        #activates the variable that ends the loop
        switch = 1
      #if the counter has reached the end of the list, break the while loop and move onto the next list
      if counter == 7:
        counter = 0
        break
      counter = counter + 1
    if switch == 1:
      break
  print(knight(listSpot))
  print(king(listSpot))
  print(bishop(listSpot))
  print(rook(listSpot))
  print(queen(listSpot))

def rook(listSpot):
  #recreate the chessboard matrix for finding the tiles on the board
  chessBoard = [
  ['a8','b8','c8','d8','e8','f8','g8','h8'],
  ['a7','b7','c7','d7','e7','f7','g7','h7'],
  ['a6','b6','c6','d6','e6','f6','g6','h6'],
  ['a5','b5','c5','d5','e5','f5','g5','h5'],
  ['a4','b4','c4','d4','e4','f4','g4','h4'],
  ['a3','b3','c3',"d3",'e3','f3','g3','h3'],
  ['a2','b2','c2','d2','e2','f2','g2','h2'],
  ['a1','b1','c1','d1','e1','f1','g1','h1']
  ]
  #list of tiles that the piece can go verically
  tileList = []
  #counts each element in the list 
  counter = 0
  #when switch hits 1, end the for loop
  switch = 0
  #for each list in the matrix
  for element in chessBoard:
    #while the counter is less than 8 means while the loop hasn't reached [letter]8 on the chessboard
    while counter < 8:
      #if the loop found a tile with a matching letter (horizontal)
      if element[counter][0] == listSpot[0]:
        #appends to the horzontal list
        tileList.append(element[counter])
        #adds one to variable, when it reaches 16 (accounting for the number of tiles horizontal and vertical will have combined), end the loop
        switch = switch + 1
      #if the loop found a tile with a matching number (vertical)
      if element[counter][1] == listSpot[1]:
        #append to vertical list
        tileList.append(element[counter])
        switch = switch + 1
      #if the counter has reached the end of the list, break the while loop and move onto the next list
      if counter == 7:
        counter = 0
        break
      counter = counter + 1
    if switch == 16:
      break
  #removes user input from list
  tileList.remove(listSpot)
  #removes user input from list
  tileList.remove(listSpot)
  #empty answer 
  answer = ''
  #counter of vertical tiles, for knowing when to add a comma or a period (vertical always comes last so it has to deal with this)
  vCounter = 0
  #for a horizontal tile, add it to empty answer string and add a comma after it
  tileList.sort()
  for item in tileList:
    answer = answer + item 
    #if vcounter matches length - 1, add period at end
    if vCounter == len(tileList) - 1:
      answer = answer + '.'
    else:
      #otherwise, add comma and increase counter by 1
      answer = answer + ', '
      vCounter = vCounter + 1
  return('Rook can move to spots ' + answer) 

def knight(listSpot):
  #recreate the chessboard matrix for finding the tiles on the board
  chessBoard = [
  ['a8','b8','c8','d8','e8','f8','g8','h8'],
  ['a7','b7','c7','d7','e7','f7','g7','h7'],
  ['a6','b6','c6','d6','e6','f6','g6','h6'],
  ['a5','b5','c5','d5','e5','f5','g5','h5'],
  ['a4','b4','c4','d4','e4','f4','g4','h4'],
  ['a3','b3','c3',"d3",'e3','f3','g3','h3'],
  ['a2','b2','c2','d2','e2','f2','g2','h2'],
  ['a1','b1','c1','d1','e1','f1','g1','h1']
  ]
  #counts each element in the list 
  counter = 0
  #list of tiles
  tileList = []
  #dictonary of letters, will use to determine letters of tiles which the piece can move to
  letterDict = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8, 
  1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h'}
  #left 1-2 and right 1-2 account for the 4 possible L shapes in both directions (8 possibilities)
  left1 = None
  left1E = 0
  left2 = None
  left2E = 0
  right1 = None
  right1E = 0
  right2 = None
  right2E = 0
  #E stands for enabled, if this variable turns into 1, then the loops later on will search for tiles with these letters in them
  #finds the dictionary number that corresponds to the inputted tile 
  knightNumber = letterDict[listSpot[0]]
  #if the selected tile is more than 1 tile away from the right edge
  if knightNumber > 1:
    #left1 is the chosen tile's letter but 2 back
    left1 = letterDict[knightNumber - 1]
    left1E = 1
  #if the tile is more than 2 tiles away from the right edge
  if knightNumber > 2:
    #left2 is the chosen tile's letter but 2 back
    left2 = letterDict[knightNumber - 2]
    left2E = 1
  #if the tile is more than one tile away from the left edge
  if knightNumber < 8:
    #right1 is the chosen tile's letter but 1 letter foward
    right1 = letterDict[knightNumber + 1]
    right1E = 1
  #if the tile is more than two tiles away from the left edge
  if knightNumber < 7:
    #right2 is the chosen tile's letter but 2 letters foward
    right2 = letterDict[knightNumber + 2]
    right2E = 1
  for element in chessBoard:
    #while the counter is less than 8 means while the loop hasn't reached [letter]8 on the chessboard
    while counter < 8:
      #checks if left1E was activated
      if left1E == 1:
        #checks if the current element's letter matches 
        if element[counter][0] == left1:
          #if the number of the current element matches the selected tile (look above to see what right1, right2, left1, and left 2 represent on the board)
          if int(element[counter][1]) == int(listSpot[1]) + 2:
            tileList.append(element[counter])
          elif int(element[counter][1]) == int(listSpot[1]) - 2:
            tileList.append(element[counter])
      if left2E == 1:
        if element[counter][0] == left2:
          #if the tile is 1 above the selected tile 
          if int(element[counter][1]) == (int(listSpot[1]) + 1):
            tileList.append(element[counter])
          #if the tile is 1 below the selected tile
          elif int(element[counter][1]) == int(listSpot[1]) - 1:
            tileList.append(element[counter])
      if right1E == 1:
        if element[counter][0] == right1:
          if int(element[counter][1]) == int(listSpot[1]) + 2:
            tileList.append(element[counter])
          elif int(element[counter][1]) == int(listSpot[1]) - 2:
            tileList.append(element[counter])
      if right2E == 1:
        if element[counter][0] == right2:
          if int(element[counter][1]) == int(listSpot[1]) + 1:
            tileList.append(element[counter])
          elif int(element[counter][1]) == int(listSpot[1]) - 1:
            tileList.append(element[counter])
      #if the counter has reached the end of the list, break the while loop and move onto the next list
      if counter == 7:
        counter = 0
        break
      counter = counter + 1
  answer = ''
  #counter of vertical tiles, for knowing when to add a comma or a period (vertical always comes last so it has to deal with this)
  vCounter = 0
  #for a horizontal tile, add it to empty answer string and add a comma after it
  tileList.sort() 
  for item in tileList:
    answer = answer + item 
    #if vcounter matches length - 1, add period at end
    if vCounter == len(tileList) - 1:
      answer = answer + '.'
    else:
      #otherwise, add comma and increase counter by 1
      answer = answer + ', '
      vCounter = vCounter + 1
  return('Knight can move to spots ' + answer) 

def king(listSpot):
  #recreate the chessboard matrix for finding the tiles on the board
  chessBoard = [
  ['a8','b8','c8','d8','e8','f8','g8','h8'],
  ['a7','b7','c7','d7','e7','f7','g7','h7'],
  ['a6','b6','c6','d6','e6','f6','g6','h6'],
  ['a5','b5','c5','d5','e5','f5','g5','h5'],
  ['a4','b4','c4','d4','e4','f4','g4','h4'],
  ['a3','b3','c3',"d3",'e3','f3','g3','h3'],
  ['a2','b2','c2','d2','e2','f2','g2','h2'],
  ['a1','b1','c1','d1','e1','f1','g1','h1']
  ]
  #counts each element in the list 
  counter = 0
  #list of tiles
  tileList = []
  #dictonary of letters, will use to determine letters of tiles which the piece can move to
  letterDict = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8, 
  1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h'}
  #left means the letter to the left of the selected tile
  left = None
  left1E = 0
  #right means the letter to the right of the selected tile
  right = None
  right1E = 0
  #E stands for enabled, if this variable turns into 1, then the loops later on will search for tiles with these letters in them
  #finds the dictionary number that corresponds to the inputted tile 
  kingNumber = letterDict[listSpot[0]]
  #if the selected tile is more than 1 tile away from the right edge
  if kingNumber > 1:
    left = letterDict[kingNumber - 1]
    left1E = 1
  #if the tile is more than one tile away from the left edge
  if kingNumber < 8:
    right = letterDict[kingNumber + 1]
    right1E = 1
  for element in chessBoard:
    #while the counter is less than 8 means while the loop hasn't reached [letter]8 on the chessboard
    while counter < 8:
      #checks if left1E was activated
      if left1E == 1:
        #checks if the current element's letter matches 
        if element[counter][0] == left:
          #if the number of the current element matches the selected tile (look above to see what right and left)
          #if the tile is 1 above the selected tile 
          if int(element[counter][1]) == int(listSpot[1]) + 1:
            tileList.append(element[counter])
          #if the tile is right next to the selected tile
          elif int(element[counter][1]) == int(listSpot[1]):
            tileList.append(element[counter])
          #if the tile is 1 below the selected tile
          elif int(element[counter][1]) == int(listSpot[1]) - 1:
            tileList.append(element[counter])
      if right1E == 1:
        if element[counter][0] == right:
          if int(element[counter][1]) == int(listSpot[1]) + 1:
            tileList.append(element[counter])
          elif int(element[counter][1]) == int(listSpot[1]):
            tileList.append(element[counter])
          elif int(element[counter][1]) == int(listSpot[1]) - 1:
            tileList.append(element[counter])
      #if the tile is directly next to the selected tile
      if element[counter][0] == listSpot[0]:
        if int(element[counter][1]) == int(listSpot[1]) + 1:
          tileList.append(element[counter])
        elif int(element[counter][1]) == int(listSpot[1]) - 1:
          tileList.append(element[counter])
      #if the counter has reached the end of the list, break the while loop and move onto the next list
      if counter == 7:
        counter = 0
        break
      counter = counter + 1
  answer = ''
  #counter of vertical tiles, for knowing when to add a comma or a period (vertical always comes last so it has to deal with this)
  vCounter = 0
  #for a horizontal tile, add it to empty answer string and add a comma after it
  tileList.sort()
  for item in tileList:
    answer = answer + item 
    #if vcounter matches length - 1, add period at end
    if vCounter == len(tileList) - 1:
      answer = answer + '.'
    else:
      #otherwise, add comma and increase counter by 1
      answer = answer + ', '
      vCounter = vCounter + 1
  return('King can move to spots ' + answer) 

def bishop(listSpot):
  #recreate the chessboard matrix for finding the tiles on the board
  chessBoard = [
  ['a8','b8','c8','d8','e8','f8','g8','h8'],
  ['a7','b7','c7','d7','e7','f7','g7','h7'],
  ['a6','b6','c6','d6','e6','f6','g6','h6'],
  ['a5','b5','c5','d5','e5','f5','g5','h5'],
  ['a4','b4','c4','d4','e4','f4','g4','h4'],
  ['a3','b3','c3',"d3",'e3','f3','g3','h3'],
  ['a2','b2','c2','d2','e2','f2','g2','h2'],
  ['a1','b1','c1','d1','e1','f1','g1','h1']
  ]
  #counts each element in the list 
  counter = 0
  #list of tiles
  tileList = []
  #dictonary of letters, will use to determine letters of tiles which the piece can move to
  letterDict = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8, 
  1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h'}
  #left means the letter to the left of the selected tile, each number is according to distance from input. ex. right1 when the input is "e4" would be f
  #right means the letter to the right of the selected tile
  right1 = None
  right1E = 0
  right2 = None
  right2E = 0
  right3 = None
  right3E = 0
  right4 = None
  right4E = 0
  right5 = None
  right5E = 0
  right6 = None
  right6E = 0
  right7 = None
  right7E = 0
  right8 = None
  right8E = 0
  left1 = None
  left1E = 0
  left2 = None
  left2E = 0
  left3 = None
  left3E = 0
  left4 = None
  left4E = 0
  left5 = None
  left5E = 0
  left6 = None
  left6E = 0
  left7 = None
  left7E = 0
  left8 = None
  left8E = 0
  #E stands for enabled, if this variable turns into 1, then the loops later on will search for tiles with these letters in them
  #finds the dictionary number that corresponds to the inputted tile 
  bishopNumber = letterDict[listSpot[0]]
  #if the selected tile is more than 1 tile away from the right edge. 1 increases to 2 and so fourth
  if bishopNumber > 1:
    left1 = letterDict[bishopNumber - 1]
    left1E = 1
  if bishopNumber > 2:
    left2 = letterDict[bishopNumber -2]
    left2E = 1
  if bishopNumber > 3:
    left3 = letterDict[bishopNumber - 3]
    left3E = 1
  if bishopNumber > 4:
    left4 = letterDict[bishopNumber -4]
    left4E = 1
  if bishopNumber > 5:
    right5 = letterDict[bishopNumber -5]
    right5E = 1
  if bishopNumber > 6:
    right6 = letterDict[bishopNumber -6]
    right6E = 1
  if bishopNumber > 7:
    right7 = letterDict[bishopNumber -7]
    right7E = 1
  if bishopNumber > 8:
    right8 = letterDict[bishopNumber -8]
    right8E = 1
  #if the tile is more than one tile away from the left edge. 1 increases to 2 and so fourth
  if bishopNumber < 8:
    right1 = letterDict[bishopNumber + 1]
    right1E = 1
  if bishopNumber < 7:
    right2 = letterDict[bishopNumber + 2]
    right2E = 1
  if bishopNumber < 6:
    right3 = letterDict[bishopNumber + 3]
    right3E = 1
  if bishopNumber < 5:
    right4 = letterDict[bishopNumber + 4]
    right4E = 1
  if bishopNumber < 4:
    right5 = letterDict[bishopNumber + 5]
    right5E = 1
  if bishopNumber < 3:
    right6 = letterDict[bishopNumber + 6]
    right6E = 1
  if bishopNumber < 2:
    right7 = letterDict[bishopNumber + 7]
    right7E = 1
  if bishopNumber < 1:
    right8 = letterDict[bishopNumber + 8]
    right8E = 1
  for element in chessBoard:
      #while the counter is less than 8 means while the loop hasn't reached [letter]8 on the chessboard
      while counter < 8:
        #checks if right1E was activated
        if right1E == 1:
          #checks if the current element's letter matches 
          if element[counter][0] == right1:
            #if the number of the current element matches the selected tile (look above to see what right1, right2, left1, and left 2 represent on the board). in the case for bishop, the number of int(listSpot[1]) is adding with increases with each right/left. so right1 is + 1 and right4 is +4. this is to account for the increase in height for the bishop's diagnol moveset. 
            if int(element[counter][1]) == int(listSpot[1]) + 1:
              tileList.append(element[counter])
            elif int(element[counter][1]) == int(listSpot[1]) - 1:
              tileList.append(element[counter])
        if right2E == 1:
          #checks if the current element's letter matches 
          if element[counter][0] == right2:
            #if the number of the current element matches the selected tile (look above to see what right1, right2, left1, and left 2 represent on the board)
            if int(element[counter][1]) == int(listSpot[1]) + 2:
              tileList.append(element[counter])
            elif int(element[counter][1]) == int(listSpot[1]) - 2:
              tileList.append(element[counter])
        if right3E == 1:
          #checks if the current element's letter matches 
          if element[counter][0] == right3:
            if int(element[counter][1]) == int(listSpot[1]) + 3:
              tileList.append(element[counter])
            elif int(element[counter][1]) == int(listSpot[1]) - 3:
              tileList.append(element[counter])
        if right4E == 1:
          #checks if the current element's letter matches 
          if element[counter][0] == right4:
            if int(element[counter][1]) == int(listSpot[1]) + 4:
              tileList.append(element[counter])
            elif int(element[counter][1]) == int(listSpot[1]) - 4:
              tileList.append(element[counter])
        if right5E == 1:
          #checks if the current element's letter matches 
          if element[counter][0] == right5:
            if int(element[counter][1]) == int(listSpot[1]) + 5:
              tileList.append(element[counter])
            elif int(element[counter][1]) == int(listSpot[1]) - 5:
              tileList.append(element[counter])
        if right6E == 1:
          #checks if the current element's letter matches 
          if element[counter][0] == right6:
            if int(element[counter][1]) == int(listSpot[1]) + 6:
              tileList.append(element[counter])
            elif int(element[counter][1]) == int(listSpot[1]) - 6:
              tileList.append(element[counter])
        if right7E == 1:
          #checks if the current element's letter matches 
          if element[counter][0] == right7:
            if int(element[counter][1]) == int(listSpot[1]) + 7:
              tileList.append(element[counter])
            elif int(element[counter][1]) == int(listSpot[1]) - 7:
              tileList.append(element[counter])
        if right8E == 1:
          #checks if the current element's letter matches 
          if element[counter][0] == right8:
            if int(element[counter][1]) == int(listSpot[1]) + 8:
              tileList.append(element[counter])
            elif int(element[counter][1]) == int(listSpot[1]) - 8:
              tileList.append(element[counter])
        if left1E == 1:
          #checks if the current element's letter matches 
          if element[counter][0] == left1:
            if int(element[counter][1]) == int(listSpot[1]) + 1:
              tileList.append(element[counter])
            elif int(element[counter][1]) == int(listSpot[1]) - 1:
              tileList.append(element[counter])
        if left2E == 1:
          #checks if the current element's letter matches 
          if element[counter][0] == left2:
            if int(element[counter][1]) == int(listSpot[1]) + 2:
              tileList.append(element[counter])
            elif int(element[counter][1]) == int(listSpot[1]) - 2:
              tileList.append(element[counter])
        if left3E == 1:
          #checks if the current element's letter matches 
          if element[counter][0] == left3:
            if int(element[counter][1]) == int(listSpot[1]) + 3:
              tileList.append(element[counter])
            elif int(element[counter][1]) == int(listSpot[1]) - 3:
              tileList.append(element[counter])
        if left4E == 1:
          #checks if the current element's letter matches 
          if element[counter][0] == left4:
            if int(element[counter][1]) == int(listSpot[1]) + 4:
              tileList.append(element[counter])
            elif int(element[counter][1]) == int(listSpot[1]) - 4:
              tileList.append(element[counter])
        if left5E == 1:
          #checks if the current element's letter matches 
          if element[counter][0] == left5:
            if int(element[counter][1]) == int(listSpot[1]) + 5:
              tileList.append(element[counter])
            elif int(element[counter][1]) == int(listSpot[1]) - 5:
              tileList.append(element[counter])
        if left6E == 1:
          #checks if the current element's letter matches 
          if element[counter][0] == left6:
            if int(element[counter][1]) == int(listSpot[1]) + 6:
              tileList.append(element[counter])
            elif int(element[counter][1]) == int(listSpot[1]) - 6:
              tileList.append(element[counter])
        if left7E == 1:
          #checks if the current element's letter matches 
          if element[counter][0] == left7:
            if int(element[counter][1]) == int(listSpot[1]) + 7:
              tileList.append(element[counter])
            elif int(element[counter][1]) == int(listSpot[1]) - 7:
              tileList.append(element[counter])   
        if left8E == 1:
          #checks if the current element's letter matches 
          if element[counter][0] == left8:
            if int(element[counter][1]) == int(listSpot[1]) + 8:
              tileList.append(element[counter])
            elif int(element[counter][1]) == int(listSpot[1]) - 8:
              tileList.append(element[counter])
        #if the counter has reached the end of the list, break the while loop and move onto the next list
        if counter == 7:
          counter = 0
          break
        counter = counter + 1
  answer = ''
  #counter of vertical tiles, for knowing when to add a comma or a period (vertical always comes last so it has to deal with this)
  vCounter = 0
  #for a horizontal tile, add it to empty answer string and add a comma after it
  tileList.sort()
  for item in tileList:
    answer = answer + item 
    #if vcounter matches length - 1, add period at end
    if vCounter == len(tileList) - 1:
      answer = answer + '.'
    else:
      #otherwise, add comma and increase counter by 1
      answer = answer + ', '
      vCounter = vCounter + 1
  return('Bishop can move to spots ' + answer)  

def queen(listSpot):
 #recreate the chessboard matrix for finding the tiles on the board
  chessBoard = [
  ['a8','b8','c8','d8','e8','f8','g8','h8'],
  ['a7','b7','c7','d7','e7','f7','g7','h7'],
  ['a6','b6','c6','d6','e6','f6','g6','h6'],
  ['a5','b5','c5','d5','e5','f5','g5','h5'],
  ['a4','b4','c4','d4','e4','f4','g4','h4'],
  ['a3','b3','c3',"d3",'e3','f3','g3','h3'],
  ['a2','b2','c2','d2','e2','f2','g2','h2'],
  ['a1','b1','c1','d1','e1','f1','g1','h1']
  ]
  #ugly code begins with finding rook moves
  #list for queen moves (combining all the answers from bishop, rook, and king)
  queenList = []
  #counts each element in the list 
  counter = 0
  #when switch hits 1, end the for loop
  switch = 0
  #for each list in the matrix
  for element in chessBoard:
    #while the counter is less than 8 means while the loop hasn't reached [letter]8 on the chessboard
    while counter < 8:
      #if the loop found a tile with a matching letter (horizontal)
      if element[counter][0] == listSpot[0]:
        #appends to the horzontal list
        queenList.append(element[counter])
        #adds one to variable, when it reaches 16 (accounting for the number of tiles horizontal and vertical will have combined), end the loop
        switch = switch + 1
      #if the loop found a tile with a matching number (vertical)
      if element[counter][1] == listSpot[1]:
        #append to vertical list
        queenList.append(element[counter])
        switch = switch + 1
      #if the counter has reached the end of the list, break the while loop and move onto the next list
      if counter == 7:
        counter = 0
        break
      counter = counter + 1
    if switch == 16:
      break
  #removes user input from list
  queenList.remove(listSpot)
  #removes user input from list
  queenList.remove(listSpot)

  #next is king paste
  #counts each element in the list 
  counter = 0
  #dictonary of letters, will use to determine letters of tiles which the piece can move to
  letterDict = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8, 
  1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h'}
  #left means the letter to the left of the selected tile, K = King
  left = None
  left1K = 0
  #right means the letter to the right of the selected tile, K = king
  right = None
  right1K = 0
  #E stands for enabled, if this variable turns into 1, then the loops later on will search for tiles with these letters in them
  #finds the dictionary number that corresponds to the inputted tile 
  kingNumber = letterDict[listSpot[0]]
  #if the selected tile is more than 1 tile away from the right edge
  if kingNumber > 1:
    left = letterDict[kingNumber - 1]
    left1K = 1
  #if the tile is more than one tile away from the left edge
  if kingNumber < 8:
    right = letterDict[kingNumber + 1]
    right1K = 1
  for element in chessBoard:
    #while the counter is less than 8 means while the loop hasn't reached [letter]8 on the chessboard
    while counter < 8:
      #checks if left1E was activated
      if left1K == 1:
        #checks if the current element's letter matches 
        if element[counter][0] == left:
          #if the number of the current element matches the selected tile (look above to see what right and left)
          #if the tile is 1 above the selected tile 
          if int(element[counter][1]) == int(listSpot[1]) + 1:
            queenList.append(element[counter])
          #if the tile is right next to the selected tile
          elif int(element[counter][1]) == int(listSpot[1]):
            queenList.append(element[counter])
          #if the tile is 1 below the selected tile
          elif int(element[counter][1]) == int(listSpot[1]) - 1:
            queenList.append(element[counter])
      if right1K == 1:
        if element[counter][0] == right:
          if int(element[counter][1]) == int(listSpot[1]) + 1:
            queenList.append(element[counter])
          elif int(element[counter][1]) == int(listSpot[1]):
            queenList.append(element[counter])
          elif int(element[counter][1]) == int(listSpot[1]) - 1:
            queenList.append(element[counter])
      #if the tile is directly next to the selected tile
      if element[counter][0] == listSpot[0]:
        if int(element[counter][1]) == int(listSpot[1]) + 1:
          queenList.append(element[counter])
        elif int(element[counter][1]) == int(listSpot[1]) - 1:
          queenList.append(element[counter])
      #if the counter has reached the end of the list, break the while loop and move onto the next list
      if counter == 7:
        counter = 0
        break
      counter = counter + 1
  
  #and finally, bishop paste
  #counts each element in the list 
  counter = 0
  #list of tiles
  tileList = []
  #dictonary of letters, will use to determine letters of tiles which the piece can move to
  letterDict = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8, 
  1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h'}
  #left means the letter to the left of the selected tile, each number is according to distance from input. ex. right1 when the input is "e4" would be f
  #right means the letter to the right of the selected tile
  right1 = None
  right1E = 0
  right2 = None
  right2E = 0
  right3 = None
  right3E = 0
  right4 = None
  right4E = 0
  right5 = None
  right5E = 0
  right6 = None
  right6E = 0
  right7 = None
  right7E = 0
  right8 = None
  right8E = 0
  left1 = None
  left1E = 0
  left2 = None
  left2E = 0
  left3 = None
  left3E = 0
  left4 = None
  left4E = 0
  left5 = None
  left5E = 0
  left6 = None
  left6E = 0
  left7 = None
  left7E = 0
  left8 = None
  left8E = 0
  #E stands for enabled, if this variable turns into 1, then the loops later on will search for tiles with these letters in them
  #finds the dictionary number that corresponds to the inputted tile 
  bishopNumber = letterDict[listSpot[0]]
  #if the selected tile is more than 1 tile away from the right edge. 1 increases to 2 and so fourth
  if bishopNumber > 1:
    left1 = letterDict[bishopNumber - 1]
    left1E = 1
  if bishopNumber > 2:
    left2 = letterDict[bishopNumber -2]
    left2E = 1
  if bishopNumber > 3:
    left3 = letterDict[bishopNumber - 3]
    left3E = 1
  if bishopNumber > 4:
    left4 = letterDict[bishopNumber -4]
    left4E = 1
  if bishopNumber > 5:
    right5 = letterDict[bishopNumber -5]
    right5E = 1
  if bishopNumber > 6:
    right6 = letterDict[bishopNumber -6]
    right6E = 1
  if bishopNumber > 7:
    right7 = letterDict[bishopNumber -7]
    right7E = 1
  if bishopNumber > 8:
    right8 = letterDict[bishopNumber -8]
    right8E = 1
  #if the tile is more than one tile away from the left edge. 1 increases to 2 and so fourth
  if bishopNumber < 8:
    right1 = letterDict[bishopNumber + 1]
    right1E = 1
  if bishopNumber < 7:
    right2 = letterDict[bishopNumber + 2]
    right2E = 1
  if bishopNumber < 6:
    right3 = letterDict[bishopNumber + 3]
    right3E = 1
  if bishopNumber < 5:
    right4 = letterDict[bishopNumber + 4]
    right4E = 1
  if bishopNumber < 4:
    right5 = letterDict[bishopNumber + 5]
    right5E = 1
  if bishopNumber < 3:
    right6 = letterDict[bishopNumber + 6]
    right6E = 1
  if bishopNumber < 2:
    right7 = letterDict[bishopNumber + 7]
    right7E = 1
  if bishopNumber < 1:
    right8 = letterDict[bishopNumber + 8]
    right8E = 1
  for element in chessBoard:
      #while the counter is less than 8 means while the loop hasn't reached [letter]8 on the chessboard
      while counter < 8:
        #checks if right1E was activated
        if right1E == 1:
          #checks if the current element's letter matches 
          if element[counter][0] == right1:
            #if the number of the current element matches the selected tile (look above to see what right1, right2, left1, and left 2 represent on the board). in the case for bishop, the number of int(listSpot[1]) is adding with increases with each right/left. so right1 is + 1 and right4 is +4. this is to account for the increase in height for the bishop's diagnol moveset. 
            if int(element[counter][1]) == int(listSpot[1]) + 1:
              queenList.append(element[counter])
            elif int(element[counter][1]) == int(listSpot[1]) - 1:
              queenList.append(element[counter])
        if right2E == 1:
          #checks if the current element's letter matches 
          if element[counter][0] == right2:
            #if the number of the current element matches the selected tile (look above to see what right1, right2, left1, and left 2 represent on the board)
            if int(element[counter][1]) == int(listSpot[1]) + 2:
              queenList.append(element[counter])
            elif int(element[counter][1]) == int(listSpot[1]) - 2:
              queenList.append(element[counter])
        if right3E == 1:
          #checks if the current element's letter matches 
          if element[counter][0] == right3:
            if int(element[counter][1]) == int(listSpot[1]) + 3:
              queenList.append(element[counter])
            elif int(element[counter][1]) == int(listSpot[1]) - 3:
              queenList.append(element[counter])
        if right4E == 1:
          #checks if the current element's letter matches 
          if element[counter][0] == right4:
            if int(element[counter][1]) == int(listSpot[1]) + 4:
              queenList.append(element[counter])
            elif int(element[counter][1]) == int(listSpot[1]) - 4:
              queenList.append(element[counter])
        if right5E == 1:
          #checks if the current element's letter matches 
          if element[counter][0] == right5:
            if int(element[counter][1]) == int(listSpot[1]) + 5:
              queenList.append(element[counter])
            elif int(element[counter][1]) == int(listSpot[1]) - 5:
              queenList.append(element[counter])
        if right6E == 1:
          #checks if the current element's letter matches 
          if element[counter][0] == right6:
            if int(element[counter][1]) == int(listSpot[1]) + 6:
              queenList.append(element[counter])
            elif int(element[counter][1]) == int(listSpot[1]) - 6:
              queenList.append(element[counter])
        if right7E == 1:
          #checks if the current element's letter matches 
          if element[counter][0] == right7:
            if int(element[counter][1]) == int(listSpot[1]) + 7:
              queenList.append(element[counter])
            elif int(element[counter][1]) == int(listSpot[1]) - 7:
              queenList.append(element[counter])
        if right8E == 1:
          #checks if the current element's letter matches 
          if element[counter][0] == right8:
            if int(element[counter][1]) == int(listSpot[1]) + 8:
              queenList.append(element[counter])
            elif int(element[counter][1]) == int(listSpot[1]) - 8:
              queenList.append(element[counter])
        if left1E == 1:
          #checks if the current element's letter matches 
          if element[counter][0] == left1:
            if int(element[counter][1]) == int(listSpot[1]) + 1:
              queenList.append(element[counter])
            elif int(element[counter][1]) == int(listSpot[1]) - 1:
              queenList.append(element[counter])
        if left2E == 1:
          #checks if the current element's letter matches 
          if element[counter][0] == left2:
            if int(element[counter][1]) == int(listSpot[1]) + 2:
              queenList.append(element[counter])
            elif int(element[counter][1]) == int(listSpot[1]) - 2:
              queenList.append(element[counter])
        if left3E == 1:
          #checks if the current element's letter matches 
          if element[counter][0] == left3:
            if int(element[counter][1]) == int(listSpot[1]) + 3:
              queenList.append(element[counter])
            elif int(element[counter][1]) == int(listSpot[1]) - 3:
              queenList.append(element[counter])
        if left4E == 1:
          #checks if the current element's letter matches 
          if element[counter][0] == left4:
            if int(element[counter][1]) == int(listSpot[1]) + 4:
              queenList.append(element[counter])
            elif int(element[counter][1]) == int(listSpot[1]) - 4:
              queenList.append(element[counter])
        if left5E == 1:
          #checks if the current element's letter matches 
          if element[counter][0] == left5:
            if int(element[counter][1]) == int(listSpot[1]) + 5:
              queenList.append(element[counter])
            elif int(element[counter][1]) == int(listSpot[1]) - 5:
              queenList.append(element[counter])
        if left6E == 1:
          #checks if the current element's letter matches 
          if element[counter][0] == left6:
            if int(element[counter][1]) == int(listSpot[1]) + 6:
              queenList.append(element[counter])
            elif int(element[counter][1]) == int(listSpot[1]) - 6:
              queenList.append(element[counter])
        if left7E == 1:
          #checks if the current element's letter matches 
          if element[counter][0] == left7:
            if int(element[counter][1]) == int(listSpot[1]) + 7:
              queenList.append(element[counter])
            elif int(element[counter][1]) == int(listSpot[1]) - 7:
              queenList.append(element[counter])   
        if left8E == 1:
          #checks if the current element's letter matches 
          if element[counter][0] == left8:
            if int(element[counter][1]) == int(listSpot[1]) + 8:
              queenList.append(element[counter])
            elif int(element[counter][1]) == int(listSpot[1]) - 8:
              queenList.append(element[counter])
        #if the counter has reached the end of the list, break the while loop and move onto the next list
        if counter == 7:
          counter = 0
          break
        counter = counter + 1
  queenList.sort()
  answer = ''
  #counter of vertical tiles, for knowing when to add a comma or a period (vertical always comes last so it has to deal with this)
  vCounter = 0
  #for a horizontal tile, add it to empty answer string and add a comma after it
  for item in queenList:
    #to deal with duplicates, checks to see if current item is not already in the answer string
    if item not in answer:
      answer = answer + item 
      #if vcounter matches length - 1, add period at end
      if vCounter == len(queenList) - 1:
        answer = answer + '.'
      else:
        #otherwise, add comma and increase counter by 1
        answer = answer + ', '
    vCounter = vCounter + 1
  return('Queen can move to spots ' + answer) 