#problem 1
#function to do matrix stuff when the integer is a prime
def primeTrue(insertMatrix):
  #counts up number of items within matrix, useful for indexing
  matrixLength = len(insertMatrix)
  #for getting and modifying the last item in matrix (counting index starts at 0)
  index = matrixLength - 1
  #reverses the last item in matrix, idea to reverse with [::-1] found on stackoverflow
  newLast = ((insertMatrix[index][::-1]))
  #new list to insert the newLast item
  #deletes the old last item in the list, found out the dictionary del function works for lists too
  del insertMatrix[index]
  #adds / appends the reversed last item in matrix
  insertMatrix.append(newLast)
  return insertMatrix

#function to do matrix stuff when the integer isn't a prime
def primeFalse(insertMatrix2):
  #counts up number of items within matrix, useful for indexing
  matrixLength = len(insertMatrix2)
  #for getting and modifying the last item in matrix (counting index starts at 0)
  index = matrixLength - 1 
  #counts the amount of items in first list in matrix
  firstLength = len(insertMatrix2[0]) - 1
  #counts the amount of items in last list in matrix
  lastLength = len(insertMatrix2[index]) - 1
  #last number in firstItem
  firstItem = insertMatrix2[0][firstLength]
  #last number in last item
  lastItem = insertMatrix2[index][lastLength]
  #deletes the original last number of first list
  del insertMatrix2[0][firstLength]
  #replaces last number of first list with last number of last list
  insertMatrix2[0].append(lastItem)
   #deletes the original last number of last list
  del insertMatrix2[index][lastLength]
  #replaces last number of last list with last number of first list
  insertMatrix2[index].append(firstItem)
  return(insertMatrix2)


def isPrime(pos_integer, matrix):
  #makes sure the input is positive
  if pos_integer < 0:
    return primeFalse(matrix)
  #accounts for if anything that isn't an integer is put in
  elif type(pos_integer) != int:
    return primeFalse(matrix)
  #if positive integer, continue as normal
  else:
    #checks if input is 0 or 1, which does the false function
    if pos_integer == 0 or pos_integer == 1:
      return primeFalse(matrix)
    #checks if input is 2, which does the true funciton since its the smallest possible prime 
    elif pos_integer == 2:
      return primeTrue(matrix)
    else:
      #if count goes beyond 1, number is not prime
      count = 0
    #checks if the positive integer is prime, range of numbers between 2 and input, checks every number between to see if input is a prime
      for i in range(2, pos_integer): 
    #if the input has no remainder, its not a prime
        if (pos_integer % i) == 0:
          count = count + 1
        #after dividing with every number in range between 2 and input, checks count to see if any numbers had no remainders
        if count > 0:
          return primeFalse(matrix)
        else:
          return primeTrue(matrix)

#problem 2
def location_matrix(number,matrix):
  #aList stores sums of all items in matrix
  aList = []
  #checks if number is divisble by both 5 and 9
  if number % 5 == 0 and number % 9 == 0:
    #for item in matrix, add sums to list
    for i in range(len(matrix)):
      sums = sum(matrix[i])
      aList.append(sums)  
    #sumsList contains the sum
    sumsList = sum(aList)
    #contains the number of items in the first item im matrix
    itemLength = len(matrix[0])
    #multiplies itemLength by the number of items in the matrix
    itemLengthAll = itemLength * len(matrix)
    return(sumsList/itemLengthAll) #length of the first item should represent the lengths of the other items

  #checks if number is divisble by 5 and not 9
  elif number % 5 == 0 and number % 9 != 0:
    #sets list number
    row = 0
    #sets number of item within each list
    column = 0

    #sets first integer in matrix as smallest
    smallest_integer = matrix[0][0]
    #sets the default smallest row and columns for answer as 0
    small_row = 0
    #sets real_column as small_column when smallest integer is found
    small_column = 0
    
    #gets amount of numbers in matrix total
    numberColumns = len(matrix[0])  * len(matrix)
    #for index purposes, wont go out of bounds
    numberColumns_index = numberColumns - 1

    #while the column is smaller than the number of columns in list
    while column < numberColumns_index:
      #checks if column is past first number in list
      if column != 0:
        #if column has reached length of numbers in row
        if column == len(matrix[0]):
          #changes the row to analyze the next list in matrix if column
          row = row + 1
          column = 0
      #if formula is on last number and column is zero, stop or else you will get an index out of range error
      if row == len(matrix) and column == 0:
        break
      #if current number is smaller than smallest integer, change smallest integer to be that number. also record the row and column the number was on
      if matrix[row][column] < smallest_integer:
        smallest_integer = matrix[row][column]
        small_row = row
        small_column  = column
      #then update columns to reflect changing number in list
      column = column + 1

    #turns 0 into 1 in answer to follow the example on the PA3 page
    return(small_row,small_column)

  #checks if number is divisble by 9 and not 5
  elif number % 5 != 0 and number % 9 == 0:
    #sets list number
    row = 0
    #sets number of item within each list
    column = 0

    #sets first integer in matrix as smallest
    biggest_integer = matrix[0][0]
    #sets the default smallest row and columns for answer as 0
    big_row = 0
    #sets real_column as big_column when biggest integer is found
    big_column = 0
    
    #gets amount of numbers in matrix total
    numberColumns = len(matrix[0])  * len(matrix)
    #for index purposes, wont go out of bounds
    numberColumns_index = numberColumns - 1

    #while the column is smaller than the number of columns in list
    while column < numberColumns_index:
      #checks if column is past first number in list
      if column != 0:
        #if column has reached length of numbers in row
        if column == len(matrix[0]):
          #changes the row to analyze the next list in matrix if column
          row = row + 1
          column = 0
      #if formula is on last row and column is zero, stop or else you will get an index out of range error
      if row == len(matrix) and column == 0:
        break
      #if current number is bigger than biggest integer, change biggest integer to be that number. also record the row and column the number was on
      if matrix[row][column] > biggest_integer:
        biggest_integer = matrix[row][column]
        big_row = row
        big_column  = column
      #then update columns to reflect changing number in list
      column = column + 1

    #turns 0 into 1 in answer to follow the example on the PA3 page
    return(big_row,big_column)

  #concludes that number is divisble by neither 5 or 9
  else: 
    #for item in range of matrix
    for i in range(len(matrix)):
      #puts sum of each item in matrix into variable (adds together all numbers within each list one by one)
      sums = sum(matrix[i])
      #puts each sum of each list in matrix into list before moving onto the next one
      aList.append(sums)  
    #returns the sum of all the sums put into the list to get the final amount
    return(sum(aList))