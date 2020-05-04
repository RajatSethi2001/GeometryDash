import pyautogui as pag
import keyboard
#from PIL import ImageGrab
#from PIL import Image
from pyscreeze import *
import time
import random

def AddFrames(InstructList, Amount):
    AddThis = []
    for i in range(Amount):
        AddThis.append(0)
    
    InstructList = InstructList + AddThis
    return InstructList
    
def MutateFrames(InstructList, DeathFrame):
    EditStr = ''
    for i in range(DeathFrame + 1):
        EditStr = EditStr + str(InstructList[i])
    
    FrameLength = len(EditStr)
    CurrentInt = int(EditStr, 2)
    CurrentInt = CurrentInt + 1
    
    NewStr = bin(CurrentInt)
    NewStr = NewStr[2:len(NewStr)]
    
    while (len(NewStr) < FrameLength):
        NewStr = '0' + NewStr
    
    if (not ('0' in NewStr)):
        NewStr = NewStr.replace('1', '0')
    
    for i in range(len(NewStr)):
        InstructList[i] = int(NewStr[i])
        
    return InstructList

def IsPlayerDead():
    global sWidth
    
    x = int(sWidth / 3)
    for y in range(100, 900, 125):
        if (pixelMatchesColor(x, y, (146, 54, 54), tolerance=12)):
            return True
    
    return False

Hold = False
startTime = 1

sWidth, sHeight = pag.size()

input("Press Enter to Start!")

DeathPixel = (146, 54, 54)
InstructList = []
InstructList = AddFrames(InstructList, 1000)
print(InstructList)
time.sleep(0.5)
pag.click("GD.PNG")


time.sleep(3)
pag.click("Play.PNG")

time.sleep(startTime)
currentFrame = -1

while (True):
    PlayerDead = False
    pag.moveTo(sWidth / 2, sHeight / 2)
    pag.click()
    currentFrame = -1
    for i in InstructList:
        currentFrame += 1
        if (i == 0):
            pag.mouseUp()
               
        else:
            pag.mouseDown()
                
        #time.sleep(0.05)
        if (IsPlayerDead()): #Player Dead
            PlayerDead = True
            print('The player is dead!')
            break
            
    try:
        pag.mouseUp()
    except:
        pass
     
    #pag.moveTo(sWidth * 19 / 20, sHeight / 12) #Click Pause Button
    time.sleep(0.25)
    keyboard.press_and_release('Esc')
    #pag.click()
    #pag.moveTo(sWidth * 5 / 8, sHeight * 9 / 16) #Click Menu Button
    time.sleep(0.25)
    keyboard.press_and_release('Esc')
    
    if (PlayerDead):
        InstructList = MutateFrames(InstructList, currentFrame)
    
    else:
        InstructList = AddFrames(InstructList, 500)
    
    print(InstructList)
    time.sleep(1)
    #pag.moveTo(sWidth / 2, sHeight / 3.5) #Click Play Button
    #time.sleep(0.25)
    pag.click("Play.PNG")
    time.sleep(startTime)
              
        
        


