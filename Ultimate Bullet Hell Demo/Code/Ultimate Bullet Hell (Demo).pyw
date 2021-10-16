#This is a demo game, that is inspired by Danganronpa.
#Author: Kyle Hendrickson
########################################################

#The imports are used for :
#---The random numbers that the enemies use as their X coordinates.
#---The gui.
#---The ability to open my github page.
import random, pygame, webbrowser

def main():
    #This function calls the gui and begins the game loop.
    gui()

def getPoints():
    #This function generates the x values for the monokumas.
    pointsX = []

    #Create four random points for the X values of the monokumas.
    pointsX = [random.randint(25,993), random.randint(25,993),
               random.randint(25,993), random.randint(25,993),
               random.randint(25,993), random.randint(25,993),
               random.randint(25,993), random.randint(25,993)]

    #Determine the amount of monokumas that will drop.
    monokumaNumber = random.randint(10,16)
    
    #Remove the extra points(if any exist) from the pointsX list.
    pointsX = pointsX[0:monokumaNumber]

    #Return a list of points.
    return pointsX

def hitboxCheck(mousePos,monokumaX,startingPosition):
    #This function will determine if the player's hitbox collides with an enemy.

    #Set the collision flag to false by default.
    collision = False

    #Create list of monokuma coords.
    monokumaPos = (monokumaX,startingPosition)

    #Create two variables that determine the distance between the player,
    #and the monokuma.
    hitboxYDifference = abs(monokumaPos[1]) - abs(mousePos[1])
    hitboxXDifference = abs(monokumaPos[0]) - abs(mousePos[0])
    
    #If the Y axis is colliding.
    if(hitboxYDifference < 140 and hitboxYDifference > -120):
        #If the X axis is also colliding.
        if(hitboxXDifference < 55 and hitboxXDifference > -90):
            #Set the collision to true.
            collision = True

    #Return the collision boolean.
    return collision

def getMouseBounds(menuFlag):
    #This function gets the correct position for the mouse cursor
    #the flag menuFlag determines which set of bounds to use.

    #Get rough mouse position.
    mousePos = pygame.mouse.get_pos()

    #If the gui is focused on the game screen.
    if(menuFlag == False):

        #Create the coordinate ranges the player can move within.(Play area)
        acceptableXRange = range(10,994)
        acceptableYRange = range(17,914)

        #Tweak the mouse positon in order to place the player sprite correctly.
        mousePos = mousePos[0] - 50 , mousePos[1] - 70

        #If the mouse position at X is outside the play area.
        if mousePos[0] not in acceptableXRange:
            #Set the mouse position to the min or max value for X based on mousePos[0](X)
            mousePos = min(994,max(10,mousePos[0])), mousePos[1]

        #If the mouse position at Y is outside the play area.
        if mousePos[1] not in acceptableYRange:
            #Set the mouse position to the min or max value for Y based on mousePos[1](Y)
            mousePos = mousePos[0], min(914,max(17,mousePos[1]))

    #If the gui is on the main menu.
    elif(menuFlag == True):

        #Create the coordinate ranges for the main menu.
        acceptableXRange = range(20,1850)
        acceptableYRange = range(20,1010)

        #If the mouse position at X is outside the main menu screen.
        if mousePos[0] not in acceptableXRange:
            #Set the mouse position to the min or max value for X based on mousePos[0](X)
            mousePos = min(1850,max(20,mousePos[0])), mousePos[1]

        #If the mouse position at Y is outside the main menu screen.
        if mousePos[1] not in acceptableYRange:
            #Set the mouse position to the min or max value for Y based on mousePos[1](Y)
            mousePos = mousePos[0], min(1010,max(20,mousePos[1]))

    #If the gui is on the retry screen.
    else:

        #Tweak the mouse positon in order to place the player sprite correctly.
        mousePos = mousePos[0] - 50 , mousePos[1] - 70
        
        #Create the coordinate ranges for the retry screen.
        acceptableXRange = range(20,1795)
        acceptableYRange = range(54,946)

        #If the mouse position at X is outside the main menu screen.
        if mousePos[0] not in acceptableXRange:
            #Set the mouse position to the min or max value for X based on mousePos[0](X)
            mousePos = min(1795,max(20,mousePos[0])), mousePos[1]

        #If the mouse position at Y is outside the main menu screen.
        if mousePos[1] not in acceptableYRange:
            #Set the mouse position to the min or max value for Y based on mousePos[1](Y)
            mousePos = mousePos[0], min(946,max(54,mousePos[1]))

    #Return the new mouse position.
    return mousePos

def checkButtons(mousePos,mainMenu):
    #This function checks if the mouse cursor is over a button on the main menu or retry menu.
    selectedButton = 0

    #Set up the ranges for the main menu play button.
    playButtonXRange = range(70,175)
    playButtonYRange = range(850,930)
    
    #Set up the ranges for the main menu quit button.
    mainMenuQuitButtonXRange = range(90,170)
    mainMenuQuitButtonYRange = range(945,1000)

    #Set up the ranges for the main menu github button.
    mainMenuGithubXRange = range(1730,1870)
    mainMenuGithubYRange = range(975,1040)
    
    
    #Set up the ranges for the retry screen retry button.
    retryButtonXRange = range(950,1080)
    retryButtonYRange = range(400,460)

    #Set up the ranges for the retry screen quit button.
    quitButtonXRange = range(950,1035)
    quitButtonYRange = range(470,530)

    #If the player is on the main menu.
    if mainMenu:

        #If mousePos is over play button on the main menu.
        if mousePos[0] in playButtonXRange and mousePos[1] in playButtonYRange:
            #Set the play button as clickable.
            selectedButton = 1

        #If mousePos is over the quit button on the main menu.
        if mousePos[0] in mainMenuQuitButtonXRange and mousePos[1] in mainMenuQuitButtonYRange:
            #Set the quit button as clickable.
            selectedButton = 2

        #If mousePos is over the github button on the main menu.
        if mousePos[0] in mainMenuGithubXRange and mousePos[1] in mainMenuGithubYRange:
            #Set the github button as clickable.
            selectedButton = 5

    #If the player is on the retry screen.
    else:
    
        #If mousePos if over the retry button on the retry screen.
        if mousePos[0] in retryButtonXRange and mousePos[1] in retryButtonYRange:
            #Set the retry button as clickable.
            selectedButton = 3

        #if mousePos is over the quit button on the retry screen.
        if mousePos[0] in quitButtonXRange and mousePos[1] in quitButtonYRange:
            #Set the quit button as clickable.
            selectedButton = 4

    #Return the button that is clickable.(0-5)
    return selectedButton

def verifyStart(start):
    #This function simplifies the main loop by curating the starting position of the monokumas,
    #once per frame.

    #Remove the negative sign from the starting position.
    start = abs(start)

    #If the starting position is less than the max.
    if start < 1080:
        #Set the flag as true.
        start = True
    #If the starting position is above the max.
    else:
        #Set the flag as false.
        start = False

    #Return the flag.
    return start

def trimList(monokumaX,monokumaDetails):
    #This function removes any monokuma that intersects with the player from the list.

    #If the monokuma list has more than 0 elements.
    if len(monokumaDetails) > 0:
        #Remove the monokuma that the player hit from the list.
        monokumaDetails = monokumaDetails.pop(monokumaDetails.index(monokumaX))

    #Return the new list of monokumas.
    return monokumaDetails

def gui():
    #This function sets up the gui and runs the main loop for the game.
    
    #Load window icon and mouse cursor.
    windowIcon = pygame.image.load('../Images/monokuma.png')
    mouseCursorMainMenu = pygame.image.load('../Images/mainMenuMouse.png')
    
    #Load background images.
    mainMenuScreen = pygame.image.load('../Images/mainMenuScreen.png')
    playAreaBG = pygame.image.load('../Images/playAreaBG.png')
    retryScreen = pygame.image.load('../Images/retryScreen.png')
    
    #Load ibuki images.
    ibukiDead = pygame.image.load('../Images/ibukiDead.png')
    ibukiImage = pygame.image.load('../Images/ibuki.png')

    #Load monokuma image.
    monokumaImage = pygame.image.load('../Images/monokuma.png')

    #Create a sprite for the main character
    mousePos = 0,0
    ibukiHitbox = ibukiImage.get_size()
    ibukiSprite = Sprite(5,ibukiImage,ibukiHitbox,mousePos)

    #Create the game window.
    pygame.init()
    screen = pygame.display.set_mode((1920,1080))
    pygame.display.set_caption('Ultimate Bullet Hell (Demo)')
    pygame.display.set_icon(windowIcon)
    
    #Set up colours.
    pink = (238,0,255)
    black = (0,0,0)
    white = (255,255,255)

    #Set up canvas
    screen.fill(black)

    #Set up font.
    danganFont = pygame.font.Font('../Font/platform_eight.ttf', 70)

    #Set up labels.
    counterLivesLabel = danganFont.render(str(ibukiSprite.getLives()), 1, pink)
    githubLabel = danganFont.render('Github',1,black)

    #Set up the buttons that appear on hover.
    mainMenuPlayButtonSelected = danganFont.render('Play',1,black)
    mainMenuQuitButtonSelected = danganFont.render('Quit',1,black)
    retryScreenResetButtonSelected = danganFont.render('Retry',1,black)
    retryScreenQuitButtonSelected = danganFont.render('Quit',1,black)

    #Set up the music for the window, and set the volume to 10%
    pygame.mixer.music.load('../Music/music.mp3')
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)
    
    #Make mouse cursor invisible.
    pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))

    #Set up flags for swapping screens.
    startScreen = True
    deathScreen = False

    #Set up flag for link opener.
    opened = False

    #Set up default monokuma coordinates.
    startingPosition = -100
    monokumaDetails = getPoints()

#########################################################################################
####GAME LOOP############################################################################
    
    #Main loop for the gui.
    window = True

    #While the window flag is true.
    while window:

        #For any event that pygame catches.
        for event in pygame.event.get():

            #If the event type is a quit event.
            if event.type == pygame.QUIT:

                #Set the window flag to false.
                window = False

#########################################################################################
########DEATH SCREEN#####################################################################
                
        #If the deathScreen flag is true.
        if(deathScreen == True):

            #Set the music volume to 0%
            pygame.mixer.music.set_volume(0.025)

            #Blit the retryScreen elements to the gui.
            screen.blit(retryScreen,(0,0))

            #Update the mouse position based on the focused screen.
            mousePos = getMouseBounds(None)

            #Update the ibukiSprite image and location.
            ibukiSprite.setSprite(ibukiDead)
            ibukiSprite.setLocation(mousePos)

            #Determine which button the player is hovering over.(if any)
            buttonHover = checkButtons(mousePos,False)

            #If the player is hovering over the retry screen's retry button.
            if buttonHover == 3:

                #Blit the black version of the retry screen's retry button.
                screen.blit(retryScreenResetButtonSelected,(950,400))
                
                #If the retry button on the retry screen is clicked.
                if event.type == pygame.MOUSEBUTTONUP:
                    #Reset the player variables.
                    ibukiSprite.setLives(5)
                    ibukiSprite.setSprite(ibukiImage)

                    #Reset the monokuma details.
                    startingPosition = -100
                    monokumaDetails = getPoints()

                    #Update the lives counter label.
                    counterLivesLabel = danganFont.render(str(ibukiSprite.getLives()), 1, pink)

                    #Change the screen that is displayed.
                    deathScreen = False

            #If the player is hovering over the retry screen's quit button.
            if buttonHover == 4:
                
                #Blit the black version of the retry screen's quit button.
                screen.blit(retryScreenQuitButtonSelected,(950,470))

                #If the quit button on the retry screen is clicked.
                if event.type == pygame.MOUSEBUTTONUP:

                    #Set the music volume to default.
                    pygame.mixer.music.set_volume(0.1)
                    #Reset the players lives and swap the flags to default.
                    ibukiSprite.setLives(5)
                    startScreen = True
                    deathScreen = False

                    #Reset the monokumas coordinates.
                    monokumaDetails = getPoints()
                    startingPosition = -100
                    
                    #Update the lives counter.
                    counterLivesLabel = danganFont.render(str(ibukiSprite.getLives()), 1, pink)
                    
            #Blit the player sprite and the main menu cursor together for the death screen.
            screen.blit(ibukiSprite.getSprite(),(mousePos[0] + 20,mousePos[1] - 35))
            screen.blit(mouseCursorMainMenu,(mousePos))
            
            
        #Check if the player is dead.
        if(ibukiSprite.getLives() <= 0):
            
            #If the player is dead.
            #Enable the retry flag.
            deathScreen = True

############################################################################################
########MAIN GAME SCREEN####################################################################
            
        #If the startscreen flag is false.
        elif startScreen == False:

            #Set volume to 10%.
            pygame.mixer.music.set_volume(0.1)
                
            #Check if the mouse is within the play area.
            mousePos = getMouseBounds(False)

            #Set the player's location.
            ibukiSprite.setLocation(mousePos)

            #Blit the images to the screen.
            screen.blit(playAreaBG,(0,0))
            screen.blit(counterLivesLabel,(1850,30))
            screen.blit(ibukiSprite.getSprite(),(mousePos))

            #If the starting position is not in an acceptable range.
            if not verifyStart(startingPosition):
                #Reset the list of XY coordinates for monokumas.
                monokumaDetails = getPoints()
                startingPosition = -100
            
            #For each monokuma in the list of positions.
            for monokumaX in monokumaDetails:

                #If the hitbox detects a collision.
                if hitboxCheck(mousePos,monokumaX,startingPosition):

                    #Remove one life
                    ibukiSprite.removeLife()

                    #Remove the current monokuma from the points list.
                    trimList(monokumaX,monokumaDetails)
                        
                    #Update the lives counter.
                    counterLivesLabel = danganFont.render(str(ibukiSprite.getLives()), 1, pink)

                #Blit the monokuma to the screen.
                screen.blit(monokumaImage,(monokumaX,startingPosition + 0.5))
                    
                #Increase the starting position, which is the Y coord by 0.5
                startingPosition = startingPosition + 0.5
                
###########################################################################################
########STARTING SCREEN####################################################################
                
        #If we are on the start screen.
        elif(startScreen == True):

            #Get the mouse position based on the current screen.
            mousePos = getMouseBounds(True)
            #Check if any buttons are being hovered over.
            buttonHover = checkButtons(mousePos,True)

            #Display the main menu screen elements.
            screen.blit(mainMenuScreen,(0,0))
            
            #If the main menu play button is being hovered over.
            if buttonHover == 1:

                #Blit the black version of the play button.
                screen.blit(mainMenuPlayButtonSelected,(80,860))

                #If the play button is clicked.
                if event.type == pygame.MOUSEBUTTONUP:
                    #Set the starting screen flag to false.
                    startScreen = False
                
            #If the main menu quit button is being hovered over.
            if buttonHover == 2:

                #Blit the black version of the quit button.
                screen.blit(mainMenuQuitButtonSelected,(80,940))
                
                #If the Quit button is clicked.
                if event.type == pygame.MOUSEBUTTONUP:
                    #Set the gui to stop looping.
                    window = False

            #If the main menu github button is being hovered over.
            if buttonHover == 5:

                #Blit the black version of the github button.
                screen.blit(githubLabel,(1730,975))

                #If the player clicks the github button.
                if event.type == pygame.MOUSEBUTTONUP:

                    #If a web browser window has not already been opened.
                    if openedGithub == False:
                        #Open a web browser to the github page.
                        webbrowser.open_new("https://github.com/Kyleh276/")
                        #Switch flag.
                        openedGithub = True
                #If the player is not clicking.
                else:
                    #Switch flag.
                    openedGithub = False

            #Blit the mouse cursor for the main menu to the mouse position.
            screen.blit(mouseCursorMainMenu,(mousePos))
                
                
        #Paint the frame of the gui so that it updates.
        pygame.display.update()

#############################################################################################
#SPRITE CLASS################################################################################
class Sprite():
    #Create the sprite object.
    def __init__(self,lives,sprite,hitbox,location = (-100,-100)):

        #Set up the default values for this constructor.
        self.lives = 5
        self.sprite = sprite
        self.hitbox = hitbox
        self.location = location

####################################################################################
#####SETTERS########################################################################
    
    #Create setters for assignable values.
    def removeLife(self):
        #This function is used when the player is hit to remove one life.
        self.lives = self.lives - 1

    def setLives(self,lives):
        #This function is used to reset the players lives when the player is reset.
        self.lives = lives

    def setSprite(self,sprite):
        #This function sets the image that the player sprite will use.
        self.sprite = sprite

    def setLocation(self,location):
        #This function sets the player location.
        self.location = location
        
####################################################################################
#####GETTERS########################################################################
    
    #Create getters to return values.
    def getLocation(self):
        #This function returns the player's location.
        return self.location

    def getSprite(self):
        #This function returns the sprite image.
        return self.sprite

    def getHitbox(self):
        #This function returns the hitbox for the player.
        return self.hitbox

    def getLives(self):
        #This function returns the lives of the player.
        return self.lives

#Make this file runnable.
if __name__ == '__main__':
    main()
