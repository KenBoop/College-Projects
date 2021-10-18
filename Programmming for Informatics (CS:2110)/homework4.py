# Question 1
def textCleaner(s):
  #a
  s = s.replace("\n"," ")
  s = s.replace(","," ")
  s = s.replace("."," ")
  s = s.replace(";"," ")
  ns = s
  #b
  ns = " ".join(ns.split())
  ns1 = ns
  #c
  ns1 = ns1.lower()
  ns2 = ns1
  #d
  word_count = ns2.count("it was")
  #e
  ns2 = ns2.replace("was", "is")
  ns3 = ns2
  #f
  l = [ns]
  print(ns, ns2, ns3, word_count, l)
  
# Question 2:
def printFancy(first, last, middle):
  print(last + ', ' + first + ' ' + middle)
  print(last + ', ' + first + ' ' + middle[0])
  print(first + ' ' + middle[0] + ', ' + last)
  print(last + ', ' + first[0])

# Question 3:
def average(s):
  wordCounter = 0
  lengthStore = 0
  for word in s.split():
    lengthStore = lengthStore + len(word)
    wordCounter = wordCounter + 1
  print(lengthStore / wordCounter)

#Question 4:
def vowelCount(s):
  a = 0
  e = 0
  iv = 0
  o = 0
  u = 0
  s = s.lower()
  for i in s:
    if i == 'a':
      a = a + 1
    elif i == 'e':
      e = e + 1
    elif i == 'i':
      iv = iv + 1
    elif i == 'o':
      o = o + 1
    elif i == 'u':
      u = u + 1
  print("a, e, I, o, and u appear, respectively " + str(a) + ', ' + str(e) +  ', ' + str(iv) +  ', ' + str(o) +  ', ' + str(u) + " times.")


# Run each function with reproducible example
#textCleaner("It was the best of times, it was the worst of times;\n \
#            it was the age of wisdom, it was the age\n of foolishness; \
#            it was the epoch of belief, it was the epoch of \
#            incredulity; it was...")

#printFancy("Robert", "Lucas", "Winston")


#average("A sample sentence")

#vowelCount("Le Tour de France")
