#problem 1
def celsiusToFahrenheit(temperature):
   return temperature * 9/5 + 32

def m_to_km(m):
   return m/1000


#problem 2
def celsiusToFahrenheitWords(temperature):
  if -273.15<temperature<1000:
    fah = temperature * 9/5 + 32
    return "Notice: " + str(temperature) + " degrees Celsius is equivalent to " + str(fah) + " degrees Fahrenheit." 
  else:
      return "Temperature out of range."

def m_to_km_words(m):
   if -100<m<100:
      return m/1000
   else:
      return "It's not in the range"

#problem 3
def amIBinary(aString):
  if aString.isdigit():
    for each_number in aString:
      if int(each_number) > 1:
        return False
    else:
      return True
  else:
    return False


