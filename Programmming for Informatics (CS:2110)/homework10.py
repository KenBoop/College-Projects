# Part a - recursive GCD
def rgcd(a,b):
    if b == 0:
        return(a)
    else:
        rgcd(b, a%b)
# Part b - iterative GCD
def gcd(a,b):
    while b != 0: #while b isn't 0, set temp variables a1 to b and b1 to a%b 
        a1 = b
        b1 = a%b
        a = a1 #then set a and b to equal a1 and b1
        b = b1
    return(a) #once done going through the loop, return a


# Part c - time evaluation
import time
def timing(func,n):

    input1 = n[0] #splits n into two variables once timing starts
    input2 = n[1]
    
    start = time.time() #gets the time at the beginning
    func(input1, input2) #runs the function that its on
    end = time.time() #gets the time at the end

    print(end - start) #execution time is printed, returning it returns nothing at all for some reason

def test(listInput):
    numberCounter = 0  #if its 1, then execute test, otherwise reset to test new numbers
    firstNumber = 0 #set to become the first number in row
    secondNumber = 0 #set to become second number in row
    
    for element in listInput:
        for number in element:
            if numberCounter == 1: #if numnerCounter is 1, execute tests
                secondNumber = number #sets second number as current number before starting tests
                
                inputElement = firstNumber, secondNumber #allows for both numbers to be inputted
                timing(rgcd, inputElement) #first test
                timing(gcd, inputElement) #second test
                
                print('') #blank line to seperate the tests              
                numberCounter = 0 #resets to test the next batch of numbers
                
            else: #first number step, sets the first number 
                firstNumber = number #set the first number
                numberCounter = numberCounter + 1 #go on to the next step

    
test_values=[[180324,1934,512,1803274],[124810,1492,64,4858]]
#it seems like for majority of the times, the iterative version is faster than recursion

# Question 2 - Permumations        
def permutations(lst):
    l = []
    if len(lst) < 2:
        return [lst]
    
    #for number within range of list
    for i in range(len(lst)):
        first = lst[i] #set to the first number in list
        
#puts together remaining numbers for process
#starts with batch of two nums ex. [2,3]
        remainding = lst[:i] + lst[i+1:]
        
        
#for each number in remainding, put it through this program to create variation
#the program puts them together in remainding process, creates variations
        for num in permutations(remainding):
            l.append([first] + num) #append, add l[0] to the variation within list
    return l
    
# Question 3 - Pascal's triangle
def pascalLine(n):
    if n < 0:
        return "Can't be negative."

    elif n == 1: #when the num is 1, return 0 which gets appended to the list or simply returns 0 if 1 is inputted
        return [0]
    
    else:
        line = [1] #initializes first row, which is just 1
        previousLine = pascalLine(n - 1)
        #initially zero but grows as the program recursively goes to the next row and adds together more numbers, stores
        #the previois row before next additions

        for i in range(len(previousLine) - 1): #for the length of the previousLine number - 1
            line.append(previousLine[i] + previousLine[i + 1]) #adds previous line number next to the next number, would
            #grow as more numbers appear with each row

        line = line + [1] #adds another 1 for the next row, list grows with each row
    return line
