#Morgan Baughman
#11/1/17
#whackaMole.py

print('Use the mouse to click on the red circle.')
print('Only press on each red circle once to avoid glitching.')

from ggame import *
from random import randint

#The moveCircle function sprites red circles and toggles data['moleX'] true or false. 
#This function also randomly moves the redCircle between the six circle areas with help by the step function.

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

#The mouseClick function connects certain bountries to a click.
#The mouseClick function also corresponds score with the combination of data['moleX'] == True and the bountry.

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

#The step function is necessary for the movement of the redCircles.
#The step function controls frames of the "game"

def step():
    data['frames'] += 1
    if data['frames'] == 100:
        moveCircle()
#The updateScore function is triggered by the mouseClick function to add 100 points when critea is met.
#The updateScore function sprites the score box
#When 1000 points are scored the game is won; triggering a white screen and printing "you win!"

def updateScore():
    data['score'] += 100
    data['scoreText'].destroy()
    scoreBox = TextAsset('Score = '+str(data['score']))
    data['scoreText'] = Sprite(scoreBox,(0,300))
    if data['score'] == 1000:
        Sprite(whiteRectangle) == True
        print('you win!')


#All data inside __name__ == '__main__' consists of graphics, sprites, and run functions. 

if __name__ == '__main__':

#starting points for frames and score.

    data = {}
    data['score'] = 0
    data['frames'] = 0

    scoreBox = TextAsset('Score = 0')

    red = Color(0xFF0000,1)
    black = Color(0x000000,1)
    white = Color(0xFFFFFF,1)
    
    blackOutline = LineStyle(1,black) #pixels, color
    redCircle = CircleAsset(50,blackOutline,red) #Radius, outline, fill.
    regCircle = CircleAsset(50,blackOutline, black) #Radius, outline, fill.
    whiteRectangle = RectangleAsset(1000, 1000, blackOutline, white) 

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