#Morgan Baughman
#11/1/17
#whackaMole.py

from ggame import *
from random import randint

def mouseClick(event):
    if event.x == 50 and event.y == 150:
        updateScore()

        


def updateScore():
    data['score'] =+ 10
    data['scoreText'].destroy()
    scoreBox = TextAsset('Score = '+str(data['score']))
    data['scoreText'] = Sprite(scoreBox,(0,ROWS*CELL_SIZE))



if __name__ == '__main__':
    
    data = {}
    data['score'] = 0











red = Color(0xFF0000,1)
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)

blackOutline = LineStyle(1,black) #pixels, color
redCircle = CircleAsset(50,blackOutline,red) #Radius, outline, fill.
regCircle1 = CircleAsset(50,blackOutline, black) #Radius, outline, fill.
regCircle2 = CircleAsset(50,blackOutline, black) #Radius, outline, fill.
regCircle3 = CircleAsset(50,blackOutline, black) #Radius, outline, fill.
regCircle4 = CircleAsset(50,blackOutline, black) #Radius, outline, fill.
regCircle5 = CircleAsset(50,blackOutline, black) #Radius, outline, fill.

Sprite(redCircle,(50,50))
Sprite(regCircle,(150,50))
Sprite(regCircle,(250,50))
Sprite(regCircle,(50,150))
Sprite(regCircle,(50,250))
Sprite(regCircle,(50,350))
App().run()
