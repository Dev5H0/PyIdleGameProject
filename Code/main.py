# Imports
from config import *
import xml.etree.ElementTree as ET
import threading as tr
from tkinter import *
from tkinter import ttk
from time import sleep as wait
import keyboard as kb
from keymap import scSave,scExit

# XML
dataFile = "data.xml"
xmlTree = ET.parse(dataFile) 
xmlData = xmlTree.find("data")

xmlUpgrades = xmlTree.find("upgrades")
ugAutoClick = xmlUpgrades.find("autoClicker")
xmlAutoClick = ugAutoClick.get("l")


# Data Variables
autoClick = int(xmlAutoClick)
clicks = int(xmlData.get("clicks"))
totalClicks = int(xmlData.get("total"))


# Upgrade Prices
acPrice = int(ugAutoClick.get("price"))


# Tkinter
root = Tk()
root.title(wTitle)
root.geometry(wRes)


# String Variables
svClicks = StringVar()
svTotalClicks = StringVar()
svACUpgrade = StringVar()


# Functions
def updateClicks():
   global svClicks
   svClicks
   svClicks.set("Clicks: "+str(clicks))
   svTotalClicks.set("Total Clicks: "+str(totalClicks))
updateClicks()

def onClick():
   global clicks,totalClicks
   clicks += 1
   totalClicks += 1
   svClicks.set("Clicks: "+str(clicks))
   wait(.1)

def onSave():
   global clicks 
   global autoClick
   xmlData.set("clicks",str(clicks))
   xmlData.set(("total"),str(totalClicks))
   ugAutoClick.set(("l"),str(autoClick))
   ugAutoClick.set(("price"),str(acPrice))
   xmlTree.write(dataFile)


# Upgrade Buttons
def acUpgrade():
   global clicks, acPrice, autoClick
   if clicks >= acPrice:
      autoClick += 1
      print("Upgrade")
      clicks = clicks-acPrice
      updateClicks()
      ugName = "Auto Clicker "+str(autoClick+1)+": "
      acPrice = int(round(acPrice*1.30))
      svACUpgrade.set(ugName+str(acPrice))
svACUpgrade.set("Auto Clicker "+str(int(autoClick)+1)+": "+str(acPrice))


# Upgrade Functions
def ac(ac):
   global clicks
   while True:
      clicks += autoClick
      updateClicks()
      wait(1)


# Shortcuts
def sc(sc):
   while True:
      if kb.is_pressed(scSave):
         onSave()
         print("Saving...")
         wait(1)
      if kb.is_pressed(scExit):
         print("Stopping...")
         onSave()
         wait(.5)
         root.destroy()


# Threading
acThread = tr.Thread(target=ac, daemon=True)
ac

threads = list()
for t in range(1):
   tAc = tr.Thread(target=ac, daemon=True, args=(t,))
   tSc = tr.Thread(target=sc, daemon=True, args=(t,))
   tList = [tAc, tSc]
   threads.append(tList)
   tAc.start()
   tSc.start()


# Tabs
tkTabs = ttk.Notebook(root)
mainTab = ttk.Frame(tkTabs)
upgradeTab = ttk.Frame(tkTabs)
settingsTab = ttk.Frame(tkTabs)

tkTabs.add(mainTab,text="Main")
tkTabs.add(upgradeTab,text="Upgrades")
tkTabs.add(settingsTab,text="Settings")


# Main Tab
clickLabel = Label(mainTab,textvariable=svClicks)
clickButton = Button(mainTab,text="Click Me",command=onClick)
clickLabel.pack(pady=5)
clickButton.pack()


# Upgrades Tab
upgradesLabel = Label(upgradeTab,text="UPGRADES")
upgradesLabel.pack()

ugClickLabel = Label(upgradeTab,textvariable=svClicks)
ugClickLabel.pack(pady=5)

acButton = Button(upgradeTab,textvariable=svACUpgrade,command=acUpgrade)
acButton.pack()


# Settings Tab
saveButton = Button(settingsTab,text="Save",command=onSave)
saveButton.pack()

totalClicksLabel = Label(settingsTab,textvariable=svTotalClicks)
totalClicksLabel.pack()

# -
updateClicks()
tkTabs.pack()
root.mainloop()

