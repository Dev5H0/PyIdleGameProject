# <imports>
import xml.etree.ElementTree as ET
import keyboard

from time import sleep
from tkinter import *
from tkinter import ttk
from gameConfig import wTitle,wRes
# </imports>

# <data>
# <xml setup>
dataFile = "Code/data.xml" # Location of data file
xmlTree = ET.parse(dataFile) 
xmlData = xmlTree.find("data") # Looks for the "data" tag
xmlClicks = xmlData.get("clicks") # Looks for the "clicks" attribute inside of the data tag
xmlUpgrades = xmlTree.find("upgrades")
# </xml setup>
# <upgrades>
ugAutoClick = xmlUpgrades.find("autoClicker")
autoClick = ugAutoClick.get("l")
acPrice = 10
print(autoClick)
# </upgrades>
clicks = int(xmlClicks) # Takes the string from <data clicks="">, converts it into an integer and puts it into a variable
# </data>

# <tkinter setup>
root = Tk()
root.title(wTitle) # Window title, change in "gameConfig.py"
root.geometry(wRes) # Window size, change in "gameConfig.py"
# </tkinter setup>

# <tkinter tabs>
#tkTabs = ttk.Notebook(root)
#mainTab = ttk.Frame(tkTabs)
#upgradeTab = ttk.Frame(tkTabs)

#tkTabs.add(mainTab,text="Main") # Creates a tab called "Main"
#tkTabs.add(upgradeTab,text="Upgrades") # See above comment
#tkTabs.pack() # Adds the tabs

#mainTabFrame = ttk.Frame(tkTabs)
#upgradeTabFrame = ttk.Frame=(tkTabs)

#mainTabFrame.pack(fill="both",expand=1)
#upgradeTabFrame.pack(fill="both",expand=1)

#tkTabs.add(mainTabFrame,text="Main")
#tkTabs.add(upgradeTabFrame,text="Upgrades")
# </tkinter tabs>

# <tkinter widgets setup>
emptyLabel = Label(root,text="")

upgradesLabel = Label(root,text="Upgrades")

clickLabel = Label(root,text="Clicks: "+str(clicks))
def onMainClick():
   global clicks
   clicks += 1
   clickLabel.config(text="Clicks: "+str(clicks))
   clickLabel.update_idletasks
   sleep(.1)
def onSave(): # Save progress
   global clicks # Gets the amount clicks 
   global autoClick
   xmlData.set("clicks",str(clicks)) # Replaces the "clicks" data attribute inside of the data file
   # <save upgrades>
   ugAutoClick.set(("l"),str(autoClick))
   # </save upgrades>
   xmlTree.write(dataFile) # Saves the data file with the new attribute value
#def upgrade():

clickButton = Button(root,text="Click Me",command=onMainClick)
upgradeButton = Button(root,text="Auto Clicker "+str(int(autoClick)+1)+": "+str(acPrice),)
saveButton = Button(root,text="Save",command=onSave)

clickLabel.pack()
clickButton.pack()

saveButton.pack()

emptyLabel.pack()
upgradesLabel.pack()
upgradeButton.pack()
# </tkinter widgets setup>

root.mainloop()
