ver = 'InDev.1.2.0'

# Imports
from config import *
import xml.etree.ElementTree as ET
import threading as tr
from tkinter import *
from tkinter import ttk
from time import sleep as wait
import keyboard as kb
from keymap import *

import random

# XML
dataFile = 'data.xml'
xmlTree = ET.parse(dataFile) 
xmlData = xmlTree.find('data')

ugMult = float(xmlTree.find('multipliers').get('upgrade'))
ugAutoClick = xmlTree.find('autoClicker')
xmlAutoClick = ugAutoClick.get('total')


# Data Variables
autoClick = int(xmlAutoClick)
clicks = int(xmlData.get('clicks'))
totalClicks = int(xmlData.get('total'))
resets = int(xmlData.get('resets'))


# Tkinter
root = Tk()
root.title('PyIdleClicker '+ver)
root.geometry(wRes)


# String Variables
svClicks = StringVar()
svTotalClicks = StringVar()
svResets = StringVar()
svResetP = StringVar()
svACUpgrade = StringVar()


# Functions
def updateClicks():
   global svClicks
   svClicks.set('Clicks: '+str(clicks))
   svTotalClicks.set('Total Clicks: '+str(totalClicks))

def onClick():
   global clicks,totalClicks
   clicks += 1
   totalClicks += 1
   svClicks.set('Clicks: '+str(clicks))
   wait(.1)

def onReset():
   global resets,clicks,autoClick
   if resets == 0:
      if clicks > resets+1*1005:
         clicks = 0
         autoClick = 0
         resets += 1
   else:
      if clicks > resets+1*1005:
         clicks = 0
         autoClick = 0
         resets += 1
   svResets.set('Total Resets: '+str(resets))
   svResetP.set('Reset '+str(resets+1)+': '+str(resets+1*1005))

def onSave():
   xmlData.set('clicks',str(clicks))
   xmlData.set(('total'),str(totalClicks))
   xmlData.set(('resets'),str(resets))
   ugAutoClick.set(('total'),str(autoClick))
   xmlTree.write(dataFile)


# Upgrade Buttons
def acUpgrade():
   global clicks, acPrice, autoClick
   if clicks >= acPrice:
      autoClick += 1
      clicks = clicks-acPrice
      acPrice = round(autoClick*ugMult)
      updateClicks()
      ugName = 'Auto Clicker '+str(autoClick+1)+': '
      svACUpgrade.set(ugName+str(acPrice))


# Thread Functions
def ac():
   global clicks
   while True:
      clicks += autoClick
      updateClicks()
      wait(1)

def sc():
   while True:
      if kb.is_pressed(scMainTab):
         ttk.Notebook.select(tkTabs,mainTab)
         wait(.5)
      elif kb.is_pressed(scSettingsTab):
         ttk.Notebook.select(tkTabs,settingsTab)
         wait(.5)
      elif kb.is_pressed(scUpgradeTab):
         ttk.Notebook.select(tkTabs,upgradeTab)
         wait(.5)
      if kb.is_pressed(scSave):
         onSave()
         wait(1)
      elif kb.is_pressed(scExit):
         onSave()
         wait(.1)
         root.destroy()

svMarquee = StringVar()
def marquee():
   while True:
      x = ['Hello World!', 'Click Me!', 'Cookies?','5H0','A Snake?']
      wTime = 60
      while True:
         y = random.choice(x)
         if y == svMarquee: 
            wait(.1)
            wTime -= .1
            continue
         else: break
      svMarquee.set(y)
      wait(wTime)


# Threading
threads = list()
for t in range(1):
   tAc = tr.Thread(target=ac, daemon=True)
   tSc = tr.Thread(target=sc, daemon=True)
   tMarquee = tr.Thread(target=marquee, daemon=True)
   tList = [tAc, tSc, tMarquee]
   threads.append(tList)
   tAc.start()
   tSc.start()
   tMarquee.start()


# Tabs
tkTabs = ttk.Notebook(root)
mainTab = ttk.Frame(tkTabs)
upgradeTab = ttk.Frame(tkTabs)
settingsTab = ttk.Frame(tkTabs)

tkTabs.add(mainTab,text='Main')
tkTabs.add(upgradeTab,text='Upgrades')
tkTabs.add(settingsTab,text='Settings')


# Main Tab
clickLabel = Label(mainTab,textvariable=svClicks)
clickButton = Button(mainTab,text='Click Me',command=onClick)
clickLabel.pack(pady=5)
clickButton.pack()


# Upgrades Tab
upgradesLabel = Label(upgradeTab,text='UPGRADES')
#upgradesLabel.pack()

ugClickLabel = Label(upgradeTab,textvariable=svClicks)
ugClickLabel.pack(pady=5)

acButton = Button(upgradeTab,textvariable=svACUpgrade,command=acUpgrade)
acButton.pack()


# Settings Tab
totalClicksLabel = Label(settingsTab,textvariable=svTotalClicks)
totalClicksLabel.pack()

totalResetLabel = Label(settingsTab,textvariable=svResets)
if resets > 0: 
   totalResetLabel.pack()

resetButton = Button(settingsTab,textvariable=svResetP,command=onReset)
resetButton.pack()

saveButton = Button(settingsTab,text='Save',command=onSave)
saveButton.pack()


# Root
Label(root, textvariable=svMarquee).pack()


# -
def start():
   global acPrice
   if autoClick == 0:
      acPrice = 10
   else: acPrice = round(autoClick*ugMult)
   svACUpgrade.set('Auto Clicker '+str(int(autoClick)+1)+': '+str(acPrice))
   svResets.set('Total Resets: '+str(resets))
   svResetP.set('Reset'+str(resets+1)+': '+str(resets+1*1005))
   updateClicks()
start()
tkTabs.pack()
root.mainloop()

