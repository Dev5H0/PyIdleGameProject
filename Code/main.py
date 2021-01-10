# Imports
from enum import auto
import xml.etree.ElementTree as ET
from time import sleep
from tkinter import *
from tkinter import ttk
from gameConfig import wTitle,wRes

# XML
dataFile = "Code/data.xml"
xmlTree = ET.parse(dataFile) 
xmlData = xmlTree.find("data")
xmlClicks = xmlData.get("clicks")

xmlUpgrades = xmlTree.find("upgrades")
ugAutoClick = xmlUpgrades.find("autoClicker")
xmlAutoClick = ugAutoClick.get("l")


# Upgrade Prices
acPrice = 10


# Data Variables
autoClick = int(xmlAutoClick)
clicks = int(xmlClicks)


# Tkinter
root = Tk()
root.title(wTitle)
root.geometry(wRes)


# String Variables
svClicks = StringVar()
svACUpgrade = StringVar()


# Functions
def updateClicks():
   global svClicks
   svClicks
   svClicks.set("Clicks: "+str(clicks))
updateClicks()

def onMainClick():
   global clicks
   clicks += 1
   svClicks.set("Clicks: "+str(clicks))
   sleep(.1)

def onSave():
   global clicks 
   global autoClick
   xmlData.set("clicks",str(clicks))
   ugAutoClick.set(("l"),str(autoClick))
   xmlTree.write(dataFile)

def onUpgrade(upgrade):
   global clicks,ugPrice,ugName,ugNameV,ugNameW
   if upgrade == "AC":
      global autoClick,acPrice
      ugNameV = autoClick
      ugPrice = acPrice
      ugName = "Auto Clicker "
      ugNameW = svACUpgrade
#   elif upgrade == "":
#      global upgrade,upgradePrice
#      ugNameV = upgrade
#      ugPrice = upgradePrice
#      ugName = "Upgrade "
#      ugNameW = svUpgradeWidget

   if clicks >= ugPrice:
      autoClick += 1
      print("Upgrade")
      clicks = clicks-ugPrice
      updateClicks()
      ugName = ugName+str(ugNameV+2)+": "
      ugPrice = int(round(ugPrice*1.3))
      ugNameW.set(ugName+str(ugPrice))
svACUpgrade.set("Auto Clicker "+str(int(autoClick)+1)+": "+str(acPrice))

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


# Tabs
tkTabs = ttk.Notebook(root)
mainTab = ttk.Frame(tkTabs)
upgradeTab = ttk.Frame(tkTabs)
settingsTab = ttk.Frame(tkTabs)

tkTabs.add(mainTab,text="Main")
tkTabs.add(upgradeTab,text="Upgrades")
tkTabs.add(settingsTab,text="Settings")
tkTabs.pack()


# Main Tab
clickLabel = Label(mainTab,textvariable=svClicks)
clickButton = Button(mainTab,text="Click Me",command=onMainClick)
clickLabel.pack(pady=5)
clickButton.pack()


# Upgrades Tab
upgradesLabel = Label(upgradeTab,text="UPGRADES")
upgradesLabel.pack()

ugClickLabel = Label(upgradeTab,textvariable=svClicks)
ugClickLabel.pack(pady=5)

acButton = Button(upgradeTab,textvariable=svACUpgrade,command=lambda: onUpgrade("AC"))
acButton.pack()

acToggle = "Disabled"
acToggleButton = Button(upgradeTab,text="Auto Clicker "+acToggle,command=toggleUpgrade)
if xmlAutoClick >= "1":
   acToggleButton.pack()


# Settings Tab
saveButton = Button(settingsTab,text="Save",command=onSave)
saveButton.pack()



root.mainloop()
