import tkinter
import math
import ssl
from urllib.request import urlopen, urlretrieve
from urllib.parse import urlencode, quote_plus
import json


#
# In HW10 and 11, you will use two Google services, Google Static Maps API
# and Google Geocoding API.  Both require use of an API key.
# 
# When you have the API key, put it between the quotes in the string below
GOOGLEAPIKEY = "" #put your own key here

# To run the HW10 program, call the last function in this file: HW10().

# The Globals class demonstrates a better style of managing "global variables"
# than simply scattering the globals around the code and using "global x" within
# functions to identify a variable as global.
#
# We make all of the variables that we wish to access from various places in the
# program properties of this Globals class.  They get initial values here
# and then can be referenced and set anywhere in the program via code like
# e.g. Globals.zoomLevel = Globals.zoomLevel + 1
#


class Globals:
   rootWindow = None
   mapLabel = None

   defaultLocation = "Mauna Kea, Hawaii"
   mapLocation = defaultLocation
   mapFileName = 'googlemap.gif'
   mapSize = 400
   zoomLevel = 9
   mapType = "roadmap"
   buttonChose = 1

def increase():
   Globals.zoomLevel = Globals.zoomLevel + 1
   displayMap()

def decrease():
   if Globals.zoomLevel > 0:
      Globals.zoomLevel = Globals.zoomLevel - 1
      displayMap()

def radioButtonChosen():
   if Globals.buttonChose == 1:
      Globals.mapType = "roadmap"
      displayMap()
      
   elif Globals.buttonChose == 2:
      Globals.mapType = "satellite"
      displayMap()
      
   elif Globals.buttonChose == 3:
      Globals.mapType = "terrain"
      displayMap()
      
   else:
      Globals.mapType = "hybrid"
      displayMap()

# Given a string representing a location, return 2-element tuple
# (latitude, longitude) for that location 
#
# See https://developers.google.com/maps/documentation/geocoding/
# for details about Google's geocoding API.
#
#
def geocodeAddress(addressString):
   urlbase = "https://maps.googleapis.com/maps/api/geocode/json?address="
   geoURL = urlbase + quote_plus(addressString)
   geoURL = geoURL + "&key=" + GOOGLEAPIKEY

   # required (non-secure) security stuff for use of urlopen
   ctx = ssl.create_default_context()
   ctx.check_hostname = False
   ctx.verify_mode = ssl.CERT_NONE
   
   stringResultFromGoogle = urlopen(geoURL, context=ctx).read().decode('utf8')
   jsonResult = json.loads(stringResultFromGoogle)
   if (jsonResult['status'] != "OK"):
      print("Status returned from Google geocoder *not* OK: {}".format(jsonResult['status']))
      result = (0.0, 0.0) # this prevents crash in retrieveMapFromGoogle - yields maps with lat/lon center at 0.0, 0.0
   else:
      loc = jsonResult['results'][0]['geometry']['location']
      result = (float(loc['lat']),float(loc['lng']))
   return result

# Contruct a Google Static Maps API URL that specifies a map that is:
# - is centered at provided latitude lat and longitude long
# - is "zoomed" to the Google Maps zoom level in Globals.zoomLevel
# - Globals.mapSize-by-Globals.mapsize in size (in pixels), 
# - will be provided as a gif image
#
# See https://developers.google.com/maps/documentation/static-maps/
#
# YOU WILL NEED TO MODIFY THIS TO BE ABLE TO
# 1) DISPLAY A PIN ON THE MAP
# 2) SPECIFY MAP TYPE - terrain vs road vs ...
#
def getMapUrl():
   lat, lng = geocodeAddress(Globals.mapLocation)
   urlbase = "http://maps.google.com/maps/api/staticmap?"
   args = "center={},{}&zoom={}&size={}x{}&format=gif&maptype={}&markers={},{}".format(lat,lng,Globals.zoomLevel,Globals.mapSize,Globals.mapSize,Globals.mapType,lat,lng)
   args = args + "&key=" + GOOGLEAPIKEY
   mapURL = urlbase + args
   return mapURL

# Retrieve a map image via Google Static Maps API, storing the 
# returned image in file name specified by Globals' mapFileName
#
def retrieveMapFromGoogle():
   url = getMapUrl()
   urlretrieve(url, Globals.mapFileName)

########## 
#  basic GUI code

def displayMap():
   retrieveMapFromGoogle()    
   mapImage = tkinter.PhotoImage(file=Globals.mapFileName)
   Globals.mapLabel.configure(image=mapImage)
   # next line necessary to "prevent (image) from being garbage collected" - http://effbot.org/tkinterbook/label.htm
   Globals.mapLabel.mapImage = mapImage

   
def readEntryAndDisplayMap():
   #### you should change this function to read from the location from an Entry widget
   #### instead of using the default location
   location = locationEntry.get()
   Globals.mapLocation = location
   displayMap()

     
def initializeGUIetc():

   Globals.rootWindow = tkinter.Tk()
   Globals.rootWindow.title("HW10")
   
   mainFrame = tkinter.Frame(Globals.rootWindow) 
   mainFrame.pack()
   
   global locationEntry
   L1 = tkinter.Label(text="Enter the location:")
   L1.pack(side=tkinter.LEFT)
   locationEntry = tkinter.Entry()
   locationEntry.pack(side=tkinter.LEFT)

   # radio buttons
   
   choice4 = tkinter.Radiobutton(text="Hybrid", command=buttonChoice4, value=4)
   choice4.pack(side=tkinter.RIGHT)

   choice3 = tkinter.Radiobutton(text="Terrain", command=buttonChoice3, value=3)
   choice3.pack(side=tkinter.RIGHT)

   choice2 = tkinter.Radiobutton(text="Satellite", command=buttonChoice2, value=2)
   choice2.pack(side=tkinter.RIGHT)
   
   choice1 = tkinter.Radiobutton(text="Roadmap", command=buttonChoice1, value=1)
   choice1.pack(side=tkinter.RIGHT)


   # increases the zoom level on the map
   increaseButton = tkinter.Button(text="+", command=increase)
   increaseButton.pack(side=tkinter.TOP)
   decreaseButton = tkinter.Button(text="-", command=decrease)
   decreaseButton.pack(side=tkinter.TOP)

   # until you add code, pressing this button won't change the map (except
   # once, to the Beijing location "hardcoded" into readEntryAndDisplayMap)
   # you need to add an Entry widget that allows you to type in an address
   # The click function should extract the location string from the Entry widget
   # and create the appropriate map.
   readEntryAndDisplayMapButton = tkinter.Button(mainFrame, text="Show me the map!", command=readEntryAndDisplayMap)
   readEntryAndDisplayMapButton.pack(side=tkinter.BOTTOM)


   # we use a tkinter Label to display the map image
   Globals.mapLabel = tkinter.Label(mainFrame, width=Globals.mapSize, bd=2, relief=tkinter.FLAT)
   Globals.mapLabel.pack()

def buttonChoice1():
   Globals.buttonChose = 1
   radioButtonChosen()

def buttonChoice2():
   Globals.buttonChose = 2
   radioButtonChosen()

def buttonChoice3():
   Globals.buttonChose = 3
   radioButtonChosen()

def buttonChoice4():
   Globals.buttonChose = 4
   radioButtonChosen()

def HW10():
    initializeGUIetc()
    displayMap()
    Globals.rootWindow.mainloop()
