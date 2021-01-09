import xml.etree.ElementTree as ET

from time import sleep
from tkinter import *
from tkinter import ttk
from gameConfig import wTitle,wRes


dataFile = "Code/data.xml" # Location of data file
xmlTree = ET.parse(dataFile) 
xmlData = xmlTree.find("data") # Looks for the "data" tag
xmlClicks = xmlData.get("clicks") # Looks for the "clicks" attribute inside of the data tag

xmlUpgrades = xmlTree.find("upgrades")
ugAutoClick = xmlUpgrades.find("autoClicker")
xmlAutoClick = ugAutoClick.get("l")
acPrice = 10

autoClick = int(xmlAutoClick)
clicks = int(xmlClicks) # Takes the string from <data clicks="">, converts it into an integer and puts it into a variable

root = Tk()
root.title(wTitle) # Window title, change in "gameConfig.py"
root.geometry(wRes) # Window size, change in "gameConfig.py"

tkTabs = ttk.Notebook(root)
mainTab = ttk.Frame(tkTabs)
upgradeTab = ttk.Frame(tkTabs)
settingsTab = ttk.Frame(tkTabs)

tkTabs.add(mainTab,text="Main") # Creates main tab
tkTabs.add(upgradeTab,text="Upgrades") # Creates upgrade tab
tkTabs.add(settingsTab,text="Settings") # Creates settings tab
tkTabs.pack() # Adds the tabs to the gui

upgradesLabel = Label(upgradeTab,text="Upgrades")
clickLabel = Label(mainTab,text="Clicks: "+str(clicks))
ugClickLabel = Label(upgradeTab,text="Clicks: "+str(clicks))


def onMainClick():
   global clicks
   clicks += 1
   ugClickLabel.config(text="Clicks: "+str(clicks))
   clickLabel.config(text="Clicks: "+str(clicks))
   ugClickLabel.update_idletasks
   clickLabel.update_idletasks
   sleep(.1)
def onSave(): # Save progress
   global clicks # Gets the amount clicks 
   global autoClick
   xmlData.set("clicks",str(clicks)) # Saves "Clicks"
   ugAutoClick.set(("l"),str(autoClick)) # Saves "Auto Clicker" upgrade
   xmlTree.write(dataFile) # Saves the data file with the new attribute value
def upgrade(number):
   global clicks
   global acPrice
   if clicks >= acPrice:
      global autoClick
      print(clicks)
      autoClick += number
      clicks = clicks-acPrice
      print(clicks)
      acPrice = int(round(float(acPrice)*float(1.3)))
      ugClickLabel.config(text="Clicks: "+str(clicks))
      clickLabel.config(text="Clicks: "+str(clicks))
      ugClickLabel.update_idletasks
      clickLabel.update_idletasks
def autoClicking():
   global acToggle
   if acToggle == "Enabled":
      global clicks
      global autoClick
      clicks += autoClick
      ugClickLabel.update_idletasks
      clickLabel.update_idletasks
      sleep(1)
   else: sleep(.5)
def toggleUpgrade():
   global acToggle
   global acToggleButton
   if acToggle == "Disabled":
      acToggle = "Enabled"
      acToggleButton = Button(upgradeTab,text="Auto Clicker "+acToggle,command=toggleUpgrade)
      acToggleButton.update_idletasks
   elif acToggle == "Enabled":
      acToggle = "Disabled"
      acToggleButton = Button(upgradeTab,text="Auto Clicker "+acToggle,command=toggleUpgrade)
      acToggleButton.update_idletasks
clickButton = Button(mainTab,text="Click Me",command=onMainClick)
saveButton = Button(settingsTab,text="Save",command=onSave)

acButton = Button(upgradeTab,text="Auto Clicker "+str(int(autoClick)+1)+": "+str(acPrice)+" Clicks",command=lambda: upgrade(1))
acToggle = "Disabled"
acToggleButton = Button(upgradeTab,text="Auto Clicker "+acToggle,command=toggleUpgrade)

clickLabel.pack(pady=5)
clickButton.pack()
saveButton.pack()

ugClickLabel.pack(pady=5)
upgradesLabel.pack()
acButton.pack()
if xmlAutoClick >= "1":
   acToggleButton.pack()

root.mainloop()
