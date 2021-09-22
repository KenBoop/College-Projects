#problem 1
def isPalindrome(input_string):
  #empty string to fill in with reversed string
  reversed_string = ''
  #for loop to go through each letter in the string
  for i in reversed(range(len(input_string))):
    #states the current indexxed character the current character varaible
    current_character = input_string[i]
    #adds the current character to reversed string 
    reversed_string = reversed_string + current_character

  #sees if the reversed string matches up with the input string (sees if its the same in reverse)
  if input_string == reversed_string:
    return True
  else:
    return False

def modifying_string(input1,input2):
  #checks if input1 is a string while input2 is
  if type(input1) != str and type(input2) == str:
    #if input1 is not a string
    return 'The first input is not a string.'

  #checks if input2 is not a string while input1 is
  elif type(input2) != str and type(input1) == str:
    #result if input2 is not a string
    return 'The second input is not a string.'

  #checks if both inputs aren't strings
  elif type(input1) != str and type(input2) != str:
    #result if input 1 and 2 are not string
    return 'Both of inputs are not string.'

  #both are strings scenario
  else:
    #checks if input 1 is a palindrome and 2 isn't
    if isPalindrome(input1) == True and isPalindrome(input2) == False:
      #returns length of input2
      return len(input2)

    #checks if input 1 isn't a palindrome and 2 is
    elif isPalindrome(input1) == False and isPalindrome(input2) == True:
      #returns length of input1
      return len(input1)
    
    #checks if both aren't palindrome, not accounted for in original problem but felt like it should be included
    elif isPalindrome(input1) == False and isPalindrome(input2) == False:
      #decided to make it add the lengths of input 1 and 2 together if both inputs aren't palindromes
      return len(input1) + len(input2)

    #if both are palindromes
    else: 
      #empty string to add reversed input1, input2, and length 
      reversed_strings = ''
      #combines length of both inputs
      lengths = len(input1) + len(input2)

      #for loop to go through each letter in string1
      for i in reversed(range(len(input1))):
        current_character = input1[i]
        #adds the current character to reversed strings
        reversed_strings = reversed_strings + current_character
      
      #for loop to go through each letter in string2
      for i in reversed(range(len(input2))):
        current_character = input2[i]
        #adds the current character to reversed strings
        reversed_strings = reversed_strings + current_character
      
      return (reversed_strings) + str(lengths)
      
#problem2 #input 1 = matrix, input 2 = integer
def modify_matrix(input1,input2):
  #receives length of rows and columns 
  row = len(input1)
  column = len(input1[0])

  #input1[0] should be representative of the column length of the whole matrix
  #checks if input2 is bigger than matrix's row length but smaller than matrix's column length
  if row >= input2 and column <= input2: 
    #list of lists in matrix
    alist=[]

    #for reversed lists within column, code inspired by what Airi posted on Discord
    for item in reversed(range(len(input1[input2]))):
      #appends reversed item to list
      alist.append(input1[input2][item])
    return alist
  
  #checks if input2 is bigger than matrix's column length but smaller than matrix's row length
  elif row <= input2 and column > input2:
    #second list of lists in matrix
    blist=[]
    for item in reversed(range(len(input1))):
        blist.append(input[item])
    return blist

  #checks if input2 is bigger than matrix's column length and row length
  elif row <= input2 and column <= input2:
    #returns input 2 squared
    return(input2 ** 2)
  
  #else stands in place for the result of input2 being smaller than both column length and row length
  else:
    #returns row length multiplied by column length
    return row * column