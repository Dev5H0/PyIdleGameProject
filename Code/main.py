import xml.etree.ElementTree as ET
from time import sleep
from tkinter import *
from gameConfig import wTitle,wRes

dataFile = "Code/data.xml"
xmlTree = ET.parse(dataFile)
xmlData = xmlTree.find("data")
xmlClicks = xmlData.get("clicks")

clicks = int(xmlClicks)

root = Tk()
root.title(wTitle)
root.geometry(wRes)

clickLabel = Label(root,text="Clicks: "+str(clicks))

def onClick():
   global clicks
   clicks += 1
   clickLabel.config(text="Clicks: "+str(clicks))
   clickLabel.update_idletasks
   sleep(.1)
def onSave():
   global clicks
   xmlData.set("clicks",str(clicks))
   xmlTree.write(dataFile)

clickButton = Button(root,text="Click Me",command=onClick)
saveButton = Button(root,text="Save",command=onSave)

clickLabel.pack()
clickButton.pack()
saveButton.pack()

root.mainloop()
