#Morgan Baughman
#11/1/17
#whackaMole.py

from ggame import *
from random import randint

def mouseClick(event):
    if event.x <= 100 and event.y <= 100:
        print('Morgan')
    if event.x >= 100 and event.x <=200 and event.y <= 100:
        print('Jack')
    if event.x >=200 and event.x <=300 and event.y <=100:
        print('Pedro')
    if event.x <= 100 and event.y >= 100 and event.y <= 200:
        print('Deigo')
    if event.x >= 100 and event.x <=200 and event.y >= 100 and event.y <= 200:
        print('Greg')
    if event.x >=200 and event.x <=300 and event.y >= 100 and event.y <= 200:
        print('Charlie')
    data['frames'] = 0


def moveCircle():
    num = randint(1,6)
    if num == 1:
        Sprite(redCircle,(50,50))
    else:
        Sprite(regCircle,(50,50))
    if num == 2:
        Sprite(redCircle,(150,50))
    else:
        Sprite(regCircle,(150,50))
    if num == 3:
        Sprite(redCircle,(250,50))
    else:
        Sprite(regCircle,(250,50))
    if num == 4:
        Sprite(redCircle,(50,150))
    else:
        Sprite(regCircle,(50,150))
    if num == 5:
        Sprite(redCircle,(150,150))
    else:
        Sprite(regCircle,(150,150))
    if num == 6:
        Sprite(redCircle,(250,150))
    else:
        Sprite(regCircle,(250,150))
        
    data['frames'] = 0


def step():
    data['frames'] += 1
    if data['frames'] == 30:
        moveCircle()

if __name__ == '__main__':
    
    data = {}
    data['score'] = 0
    data['frames'] = 0


red = Color(0xFF0000,1)
black = Color(0x000000,1)

blackOutline = LineStyle(1,black) #pixels, color
redCircle = CircleAsset(50,blackOutline,red) #Radius, outline, fill.
regCircle = CircleAsset(50,blackOutline, black) #Radius, outline, fill.

Sprite(redCircle,(50,50))
Sprite(regCircle,(50,50))
Sprite(regCircle,(150,50))
Sprite(regCircle,(250,50))
Sprite(regCircle,(50,150))
Sprite(regCircle,(150,150))
Sprite(regCircle,(250,150))
App().listenMouseEvent("click", mouseClick)
App().run(step)
