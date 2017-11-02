#Morgan Baughman
#11/1/17
#whackaMole.py

from ggame import *
from random import randint

def mouseClick(event):
    if event.x <= 100 and event.y <= 100:
        print('Morgan')
    if event.x >= 100 and event.x <=200 and event.y <= 100:
        print('Charlie')
    if event.x >=200 and event.x <=300 and event.y <=100:
        print('Greg')
    if event.x <= 100 and event.y >= 100 and event.y <= 200:
        print('Jack')
    if event.x >= 100 and event.x <=200 and event.y >= 100 and event.y <= 200:
        print('Gary')
    if event.x >=200 and event.x <=300 and event.y >= 100 and event.y <= 200:
        print('Pedro')



def updateScore():
    data['score'] =+ 10
    data['scoreText'].destroy()
    scoreBox = TextAsset('Score = '+str(data['score']))
    data['scoreText'] = Sprite(scoreBox,(400,50))


if __name__ == '__main__':
    
    data = {}
    data['score'] = 0







red = Color(0xFF0000,1)
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)

blackOutline = LineStyle(1,black) #pixels, color
redCircle = CircleAsset(50,blackOutline,red) #Radius, outline, fill.
regCircle = CircleAsset(50,blackOutline, black) #Radius, outline, fill.
regCircle1 = CircleAsset(50,blackOutline, black) #Radius, outline, fill.
regCircle2 = CircleAsset(50,blackOutline, black) #Radius, outline, fill.
regCircle3 = CircleAsset(50,blackOutline, black) #Radius, outline, fill.
regCircle4 = CircleAsset(50,blackOutline, black) #Radius, outline, fill.

for i in range(1,5):
    if i == 1:
        Sprite(redCircle,(50,50))
    if i == 2:
        Sprite(redCircle,(50,50))

Sprite(regCircle,(50,50))
Sprite(regCircle1,(150,50))
Sprite(regCircle2,(250,50))
Sprite(regCircle3,(50,150))
Sprite(regCircle4,(150,150))
Sprite(regCircle,(250,150))



App().listenMouseEvent("click", mouseClick)
App().run()
