#problem 1
def two_to_ten(input_string):
  #counts until it reaches range
  count = 0
  #makes rangeString equal to the length of the input
  rangeString = len(input_string)
  #variable that each number gets added to, creates the end result
  end = 0
  #for the while statement to stay in range
  countRange = rangeString

  #while the counter isn't equal to the range of the input
  while count != countRange:
    #assigns two's exponent  
    exponent = (rangeString - 1)
    #piece of the formula to convert binary to decimal, while loop converts number by number
    #formula: (binary num * 2^exponent equal to length of binary num - 1)
    end = end + (int(input_string[count]) * (2 ** exponent))

    #moves on to the next number
    count = count + 1
    #makes exponent go down for the next number to be converted
    rangeString = rangeString - 1

  return end

#problem 2
def ten_to_two(decimal_number,binary_length):
  #counts amount of while processes to accomidate binary length
  count = 0
  #makes the end result 
  end = ''
  #sets quotient to be the same as decimal 
  quotient = abs(decimal_number)

  #while the decimal number is not 0 
  while quotient != 0:
    #finds remainder
    remainder = quotient % 2
    #computes the end result
    end = str(remainder) + end
    #processes the quiotent, divide by 2 each time
    quotient = quotient // 2
    count = 1 + count

    #checks if the binary length gets exceeded 
    if count > binary_length:
      return "overflow error"

  #accounts for the binary length, adds length to answer
  #while the counter doesnt match up to the specified length
  while count != binary_length:
    #adds 0s to the answer
    end = str(0) + end
    count = count + 1

  #checks if decimal number is negative
  if decimal_number < 0:
    #adds negative symbol in front of answer
    end = '-' + end

  return end