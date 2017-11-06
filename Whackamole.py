#Morgan Baughman
#11/1/17
#whackaMole.py

from ggame import *
from random import randint

def moveCircle():
    num = randint(1,6)
    if num == 1:
        Sprite(redCircle,(50,50))
        data['mole1'] = True
    else:
        Sprite(regCircle,(50,50))
    if num == 2:
        Sprite(redCircle,(150,50))
        data['mole2'] = True
    else:
        Sprite(regCircle,(150,50))
    if num == 3:
        Sprite(redCircle,(250,50))
        data['mole3'] = True
    else:
        Sprite(regCircle,(250,50))
    if num == 4:
        Sprite(redCircle,(50,150))
        data['mole4'] = True
    else:
        Sprite(regCircle,(50,150))
    if num == 5:
        Sprite(redCircle,(150,150))
        data['mole5'] = True
    else:
        Sprite(regCircle,(150,150))
    if num == 6:
        Sprite(redCircle,(250,150))
        data['mole6'] = True
    else:
        Sprite(regCircle,(250,150)) 
        
    data['frames'] = 0
    
def mouseClick(event):
    if event.x <= 100 and event.y <= 100 and data['mole1'] == True:
        updateScore()
    if event.x >= 100 and event.x <=200 and event.y <= 100 and data['mole2'] == True:
        updateScore()
    if event.x >=200 and event.x <=300 and event.y <=100 and data['mole3'] == True:
        updateScore()
    if event.x <= 100 and event.y >= 100 and event.y <= 200 and data['mole4'] == True:
        updateScore()
    if event.x >= 100 and event.x <=200 and event.y >= 100 and event.y <= 200 and data['mole5'] == True:
        updateScore()
    if event.x >=200 and event.x <=300 and event.y >= 100 and event.y <= 200 and data['mole6'] == True:
        updateScore()
    
    data['mole1'] = False
    data['mole2'] = False
    data['mole3'] = False
    data['mole4'] = False
    data['mole5'] = False
    data['mole6'] = False
    data['frames'] = 0

def step():
    data['frames'] += 1
    if data['frames'] == 50:
        moveCircle()

def updateScore():
    data['score'] += 100
    data['scoreText'].destroy()
    scoreBox = TextAsset('Score = '+str(data['score']))
    data['scoreText'] = Sprite(scoreBox,(0,300))


if __name__ == '__main__':
    
    data = {}
    data['score'] = 0
    data['frames'] = 0
    data['mole1'] = False
    data['mole2'] = False 
    data['mole3'] = False
    data['mole4'] = False
    data['mole5'] = False
    data['mole6'] = False
    
    scoreBox = TextAsset('Score = 0')
     
red = Color(0xFF0000,1)
black = Color(0x000000,1)

blackOutline = LineStyle(1,black) #pixels, color
redCircle = CircleAsset(50,blackOutline,red) #Radius, outline, fill.
regCircle = CircleAsset(50,blackOutline, black) #Radius, outline, fill.

data['scoreText'] = Sprite(scoreBox, (0,300))
Sprite(redCircle,(50,50))
Sprite(regCircle,(50,50))
Sprite(regCircle,(150,50))
Sprite(regCircle,(250,50))
Sprite(regCircle,(50,150))
Sprite(regCircle,(150,150))
Sprite(regCircle,(250,150))
App().listenMouseEvent("click", mouseClick)
App().run(step)
