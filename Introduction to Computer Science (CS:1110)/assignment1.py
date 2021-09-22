
#Problem 1 
def convertUnits(feet):
    if type(feet) == int:
        if feet >= 0:
            return feet * 12
        else:
            return "I do not understand the input."
    elif type(feet)==str:
        if feet.isdigit():
            return int(feet) * 12
        elif feet.isalpha():
            return "Enter digits, not letters."
        else:
            return "I do not understand the input."
    else:
         return "I do not understand the input."


#Problem 2 
def compareToFifty(value1, value2):
    #both inputs are integers
    if type(value1) == int and type(value2) == int:
      if value1 and value2 >= 0:
        if ((value1 + value2) / 2) > 50:
          return "Above 50"
        elif ((value1 + value2) / 2) < 50:
            return "Below 50"
        else:
          return "Equal to 50"
      else:
        return "Invalid input"

    #first input is string
    elif type(value1) == str and type(value2) == int:
      if value1.isdigit():
        if ((int(value1) + value2) / 2) > 50:
            return "Above 50"
        elif ((int(value1) + value2) / 2) < 50:
          return "Below 50"
        else:
          return "Equal to 50"
      else:
          return "Invalid input"

    #second input is string
    elif type(value1) == int and type(value2) == str:
      if value2.isdigit():
        if ((value1 + int(value2)) / 2) > 50:
            return "Above 50"
        elif ((value1 + int(value2)) / 2) < 50:
          return "Below 50"
        else:
          return "Equal to 50"
      else:
          return "Invalid input"

    #both inputs are strings
    elif type(value1) == str and type(value2) == str:
      if value1.isdigit() and value2.isdigit():
        if ((int(value1) + int(value2)) / 2) > 50:
            return "Above 50"
        elif ((int(value1) + int(value2)) / 2) < 50:
          return "Below 50"
        else:
          return "Equal to 50"
      else:
          return "Invalid input"

#Problem 3
def amIDigits(aList):
  count = 0
  strs = 0
  elems = " "
  for item in aList:
    if type(aList[count]) == int:
      count += 1
      elems = elems + str(item)
    else:
      if aList[count].isdigit():
        count += 1
        elems = elems + item 

      elif aList[count].isalpha():
        count += 1
        strs += 1

  if strs > 0:
    return "The length of the input is " + str(count) + "."
  else:
    return elems

      
      








