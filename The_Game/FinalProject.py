#######################################################
# WENDY XU - FINAL PROJECT               #
#######################################################

from pygame import *
from pprint import *
from random import *

size = width,height = 450,750
screen = display.set_mode(size)
display.set_caption("Tetris Marathon")
display.set_icon(image.load("Images/TetrisIcon.ico"))

load = image.load("Images/Menu/Logo.png")
screen.blit(load,(0,0))
display.flip()
mixer.init()
font.init()
arialFont = font.SysFont("Times New Roman",20)
highscore,highlines = open("Statistics.txt").read().strip().split(",")

matrixPos = (93,117)       # x,y
hold = False    # checks if user just used hold
music = True    # if music is on
##music = False
##sfx = True      # if sound effects are on 
sfx = False
ghost = True    # if ghost pieces are on
game = False    # if user is currently playing
played = False  # if user has a saved game
gameover = False    # if user finished or lost the game

# MENU IMAGES -------------------------------------------------

# main menu images
mainmenu = image.load("Images/Menu/Main-Menu.png")
mainstatistics = image.load("Images/Menu/Main-Statistics.png")
mainmarathon = image.load("Images/Menu/Main-Marathon.png")
mainoptions = image.load("Images/Menu/Main-Options.png")
mainhelp = image.load("Images/Menu/Main-Help.png")
mainexit = image.load("Images/Menu/Main-Exit.png")

# pause menu images
pausemenu = image.load("Images/Menu/Pause-Menu.png")
pauseresume = image.load("Images/Menu/Pause-Resume.png")
pauserestart = image.load("Images/Menu/Pause-Restart.png")
pauseoptions = image.load("Images/Menu/Pause-Options.png")
pausehelp = image.load("Images/Menu/Pause-Help.png")
pausemain = image.load("Images/Menu/Pause-MainMenu.png")

# help menu images
helpmenu = image.load("Images/Menu/Help-Menu.png")
helpintro = image.load("Images/Menu/Help-Intro.png")
helpbasics = image.load("Images/Menu/Help-Basics.png")
helpmarathon = image.load("Images/Menu/Help-Marathon.png")
helpcontrols = image.load("Images/Menu/Help-Controls.png")
helpspecials = image.load("Images/Menu/Help-SpecialMoves.png")
helpoptions = image.load("Images/Menu/Help-Options.png")

# selection menu images
selectionmenu = image.load("Images/Menu/Selection-Menu.png")
selectioncontinue = image.load("Images/Menu/Selection-Continue.png")
selectionnewgame = image.load("Images/Menu/Selection-NewGame.png")

#confirm menu images
confirmmenu = image.load("Images/Menu/Confirm-Menu.png")
confirmyes = image.load("Images/Menu/Confirm-Yes.png")
confirmno = image.load("Images/Menu/Confirm-No.png")

# menu pages
statisticspage = image.load("Images/Menu/StatisticsPage.png")
optionsblankpage = image.load("Images/Menu/OptionsBlankPage.png")
intropage = image.load("Images/Menu/IntroPage.png")
basics1page = image.load("Images/Menu/BasicsPage1.png")
basics2page = image.load("Images/Menu/BasicsPage2.png")
marathonpage = image.load("Images/Menu/MarathonPage.png")
controlspage = image.load("Images/menu/ControlsPage.png")
specials1page = image.load("Images/Menu/SpecialsPage1.png")
specials2page = image.load("Images/Menu/SpecialsPage2.png")
optionspage = image.load("Images/Menu/OptionsPage.png")

# pause restart images
pauserestartpage = image.load("Images/Menu/PauseRestart.png")
pauserestartyes = image.load("Images/Menu/PauseRestartYes.png")
pauserestartno = image.load("Images/Menu/PauseRestartNo.png")

# pause exit images
pauseexitpage = image.load("Images/Menu/PauseExitPage.png")
pauseexityes = image.load("Images/Menu/PauseExit-Yes.png")
pauseexitno = image.load("Images/Menu/PauseExit-No.png")

# main exit images
mainexitpage = image.load("Images/Menu/MainExitPage.png")
mainexityes = image.load("Images/Menu/MainExit-Yes.png")
mainexitno = image.load("Images/Menu/MainExit-No.png")

# option images
musicon = image.load("Images/Menu/MusicOn.png")
musiconhover = image.load("Images/Menu/MusicOnHover.png")
musicoff = image.load("Images/Menu/MusicOff.png")
musicoffhover = image.load("Images/Menu/MusicOffHover.png")

sfxon = image.load("Images/Menu/SfxOn.png")
sfxonhover = image.load("Images/Menu/SfxOnHover.png")
sfxoff = image.load("Images/Menu/SfxOff.png")
sfxoffhover = image.load("Images/Menu/SfxOffHover.png") 

ghoston = image.load("Images/Menu/GhostOn.png")
ghostonhover = image.load("Images/Menu/GhostOnHover.png")
ghostoff = image.load("Images/Menu/GhostOff.png")
ghostoffhover = image.load("Images/Menu/GhostOffHover.png")

# game over/winner images
gamepage = image.load("Images/Menu/GamePage.png")
gamehover = image.load("Images/Menu/GameHover.png")

# IN GAME IMAGES -----------------------------------------------

grid = image.load("Images/Grid.png")

# solid blocks in matrix
skyblock = image.load("Images/SkyBlock.png")
yellowblock = image.load("Images/YellowBlock.png")
greenblock = image.load("Images/GreenBlock.png")
redblock = image.load("Images/RedBlock.png")
orangeblock = image.load("Images/OrangeBlock.png")
blueblock = image.load("Images/BlueBlock.png")
purpleblock = image.load("Images/PurpleBlock.png")

# ghost blocks
gsky = image.load("Images/GhostSky.png")
gyellow = image.load("Images/GhostYellow.png")
ggreen = image.load("Images/GhostGreen.png")
gred = image.load("Images/GhostRed.png")
gorange = image.load("Images/GhostOrange.png")
gblue = image.load("Images/GhostBlue.png")
gpurple = image.load("Images/GhostPurple.png")

# held piece/first piece in queue
hsky = image.load("Images/HoldSky.png")
hyellow = image.load("Images/HoldYellow.png")
hgreen = image.load("Images/HoldGreen.png")
hred = image.load("Images/HoldRed.png")
horange = image.load("Images/HoldOrange.png")
hblue = image.load("Images/HoldBlue.png")
hpurple = image.load("Images/HoldPurple.png")

# other pieces in queue
qsky = image.load("Images/QueueSky.png")
qyellow = image.load("Images/QueueYellow.png")
qgreen = image.load("Images/QueueGreen.png")
qred = image.load("Images/QueueRed.png")
qorange = image.load("Images/QueueOrange.png")
qblue = image.load("Images/QueueBlue.png")
qpurple = image.load("Images/QueuePurple.png")

# level numbers
level1 = image.load("Images/Numbers/Level1.png")
level2 = image.load("Images/Numbers/Level2.png")
level3 = image.load("Images/Numbers/Level3.png")
level4 = image.load("Images/Numbers/Level4.png")
level5 = image.load("Images/Numbers/Level5.png")
level6 = image.load("Images/Numbers/Level6.png")
level7 = image.load("Images/Numbers/Level7.png")
level8 = image.load("Images/Numbers/Level8.png")
level9 = image.load("Images/Numbers/Level9.png")
level10 = image.load("Images/Numbers/Level10.png")
level11 = image.load("Images/Numbers/Level11.png")
level12 = image.load("Images/Numbers/Level12.png")
level13 = image.load("Images/Numbers/Level13.png")
level14 = image.load("Images/Numbers/Level14.png")
level15 = image.load("Images/Numbers/Level15.png")

# goal numbers
goal1 = image.load("Images/Numbers/Goal1.png")
goal2 = image.load("Images/Numbers/Goal2.png")
goal3 = image.load("Images/Numbers/Goal3.png")
goal4 = image.load("Images/Numbers/Goal4.png")
goal5 = image.load("Images/Numbers/Goal5.png")
goal6 = image.load("Images/Numbers/Goal6.png")
goal7 = image.load("Images/Numbers/Goal7.png")
goal8 = image.load("Images/Numbers/Goal8.png")
goal9 = image.load("Images/Numbers/Goal9.png")
goal10 = image.load("Images/Numbers/Goal10.png")

# score numbers
score0 = image.load("Images/Numbers/Score0.png")
score1 = image.load("Images/Numbers/Score1.png")
score2 = image.load("Images/Numbers/Score2.png")
score3 = image.load("Images/Numbers/Score3.png")
score4 = image.load("Images/Numbers/Score4.png")
score5 = image.load("Images/Numbers/Score5.png")
score6 = image.load("Images/Numbers/Score6.png")
score7 = image.load("Images/Numbers/Score7.png")
score8 = image.load("Images/Numbers/Score8.png")
score9 = image.load("Images/Numbers/Score9.png")

# start numbers
start1 = image.load("Images/Numbers/One.png")
start2 = image.load("Images/Numbers/Two.png")
start3 = image.load("Images/Numbers/Three.png")

# RECTANGLES ------------------------------------

backRect = Rect(18,138,49,49)
playAgainRect = Rect(90,609,266,35)

# main menu rects
mainMarathonRect = Rect(92,290,266,35)
mainStatisticsRect = Rect(92,360,266,35)
mainOptionsRect =Rect(92,430,266,35)
mainHelpRect = Rect(92,500,266,35)
mainExitRect = Rect(92,570,266,35)
mainExitYesRect = Rect(92,326,266,35)
mainExitNoRect = Rect(92,396,266,35)

# pause menu rects
pauseResumeRect = Rect(92,240,266,35)
pauseRestartRect = Rect(92,310,266,35)
pauseOptionsRect = Rect(92,380,266,35)
pauseHelpRect = Rect(92,450,266,35)
pauseMainRect = Rect(92,520,266,35)
pauseExitYesRect = Rect(100,353,266,35)
pauseExitNoRect = Rect(100,423,266,35)
pauseRestartYesRect = Rect(90,327,266,35)
pauseRestartNoRect = Rect(90,397,266,35)

# help menu rects
helpIntroRect = Rect(92,250,266,35)
helpBasicsRect = Rect(92,320,266,35)
nextPage = Rect(195,672,30,20)
previousPage = Rect(208,672,30,20)
helpMarathonRect = Rect(92,390,266,35)
helpControlsRect = Rect(92,460,266,35)
helpSpecialsRect = Rect(92,530,266,35)
helpOptionsRect = Rect(92,600,266,35)

# options rects
musicRect = Rect(232,240,125,45)
sfxRect = Rect(232,310,125,45)
ghostRect = Rect(232,380,125,45)

# selection menu rects
continueRect = Rect(90,253,266,35)
newGameRect = Rect(90,320,266,35)

# confirm menu rects
confirmYesRect = Rect(90,410,266,35)
confirmNoRect = Rect(90,480,266,35)

# LISTS --------------------------------------------

# block lists
colours = [(0,0,0),(0,240,239),(241,240,0),(1,240,0),(240,0,1),(240,160,0),(0,0,245),(159,0,240)]
blocks = [None,skyblock,yellowblock,greenblock,redblock,orangeblock,blueblock,purpleblock]
ghostblocks = [None,gsky,gyellow,ggreen,gred,gorange,gblue,gpurple]
holdblocks = [None,hsky,hyellow,hgreen,hred,horange,hblue,hpurple]
queueblocks = [None,qsky,qyellow,qgreen,qred,qorange,qblue,qpurple]

# number lists
levelnums = [None,level1,level2,level3,level4,level5,level6,level7,level8,level9,level10,level11,level12,level13,level14,level15]
goalnums = [None,goal1,goal2,goal3,goal4,goal5,goal6,goal7,goal8,goal9,goal10]
scorenums = [score0,score1,score2,score3,score4,score5,score6,score7,score8,score9]

matrix = [[0]*10 for i in range (23)]
level = 1   # current level
goal = 10   # lines cleared in each level, renewed every level
lines = 0   # total lines completed 
score = 0   # starting score for the game
dropcounter = 16-level  # how fast pieces fall down depend on the level
timer = 20      # how much time you have to manipulate block when it hits the bottom

heldpiece = 0       # held piece idn number
holdcheck = False   # checks if you just used hold or not since you can only use hold once per active piece

# piece matrixes
I = [[0,0,0,0],         # 1 piece number (idn) --> identification
     [1,1,1,1],
     [0,0,0,0],
     [0,0,0,0]]

O = [[2,2],           # 2
     [2,2]]

S = [[0,0,0],         # 3 
     [0,3,3],
     [3,3,0]]

Z = [[0,0,0],         # 4 
     [4,4,0],
     [0,4,4]]

L = [[0,0,5],         # 5 
     [5,5,5],
     [0,0,0]]

J = [[6,0,0],         # 6
     [6,6,6],
     [0,0,0]]

T = [[0,7,0],         # 7 
     [7,7,7],
     [0,0,0]]

pieces = [0,I,O,S,Z,L,J,T]

queue = []
while len(queue) != 4:  # randomly chooses 3 pieces that don't repeat
    new = randint(1,7)
    if new not in queue:
        queue.append(new)

idn = queue.pop(0)  # identification number of piece
letter = pieces[idn]    # letter of piece according to piece idn

# determines starting position of piece
miny = 9999     # temporary value to check for min position
for a in range(len(letter)):
    for b in range(len(letter[0])):
        if letter[a][b] != 0:
            miny = min(miny,a)  # compares positions and finds most high block

if letter == I:     # I piece has a different starting position than others
    piecePos = [-1,3]
else:
    piecePos = [(miny+1)*-1,6-len(letter[0])]


# IN GAME FUNCTIONS ---------------------------------------------------------------

def marathon():
    # when user is playing tetris marathon
    global dropcounter,timer,score,highscore,highlines,game,played
    
    if music == True:
        mixer.music.load("Music/TetrisPlayingThemes.mp3")
        mixer.music.play(-1)

    running = True
    played = True
    myClock = time.Clock()
    
    if game == False:       # countdown
        screen.blit(grid,(0,0))
        screen.blit(start3,(200,340))
        display.flip()
        time.wait(1000)
        screen.blit(grid,(0,0))
        screen.blit(start2,(200,340))
        display.flip()
        time.wait(1000)
        screen.blit(grid,(0,0))
        screen.blit(start1,(200,340))
        display.flip()
        time.wait(1000)

    game = True
    
    while running:
        mx,my = mouse.get_pos()
        for e in event.get():
            if e.type == QUIT:
                return "quit"
            if e.type == KEYDOWN:
                if e.key == K_SPACE:
                    if sfx == True:
                        mixer.music.load("Music/SpaceBar.mp3")
                        mixer.music.play()
                    dropPiece()
                elif e.key == K_UP or e.key == K_x:
                    rotateRight()
                elif e.key == K_z or e.key == K_LCTRL:
                    rotateLeft()
                elif e.key == K_c or e.key == K_LSHIFT:
                    holdPiece()
                elif e.key == K_p:
                    return "pauseMenu"
                
        keys = key.get_pressed()  
    
        if keys[K_LEFT]:
            # moves left only if it doesn't move out of matrix or collide into another block
            if sfx == True:
                mixer.music.load("Music/LeftRight.mp3")
                mixer.music.play()
            if boundaryCheck("Left") and collisionCheck("Left"):     
                move("Left")
                
        if keys[K_RIGHT]:
            # moves right only if it doesn't move out of matrix or collide into another block
            if sfx == True:   
                mixer.music.load("Music/LeftRight.mp3")
                mixer.music.play()
            if boundaryCheck("Right") and collisionCheck("Right"):
                move("Right")
                
        if keys[K_DOWN]:
            # moves down only if it doesn't move out of matrix or collide into another block
            if sfx == True:
                mixer.music.load("Music/Down.mp3")
                mixer.music.play()
            if boundaryCheck("Down") and collisionCheck("Down"):
                move("Down")
                dropcounter = 16-level
                timer = 20
                score += 1*level

            if not boundaryCheck("Down") or not collisionCheck("Down"):
                # if down key is held when piece can no longer fall, quickly goes onto next piece
                if timer < 15:
                    setPiece()
                    nextPiece()
            
        dropcounter -= 1
        timer -= 1
        
        if dropcounter == 0:
            # moves piece one unit down per second if it doesn't move out of matrix and doesn't
            # collide into other blocks

            if boundaryCheck("Down") and collisionCheck("Down"):
                move("Down")
                timer = 20
            dropcounter = 16-level

        if not boundaryCheck("Down") or not collisionCheck("Down"):     
            # sets piece on matrix and goes to next piece on queue if piece can no longer move
            if timer == 0:
                setPiece()
                nextPiece()

        if timer == 0:
            timer = 20

        if gameover == True:
            return "endPage"
        
        if music == True:
            mixer.music.load("Music/TetrisPlayingThemes.mp3")
            mixer.music.play(-1)
            
        drawMatrix(matrixPos)
        display.flip()
        clear()
        myClock.tick(15)


def drawMatrix(matrixPos):        # draws current state of matrix
    global colours,matrix,end,collide,piecePos,idn,dropcounter,piece
    
    screen.blit(grid,(0,0))
    # draws current blocks on matrix        
    for x in range(10):     
        for y in range(20):
            if matrix[y][x] != 0:
                screen.blit(blocks[matrix[y][x]],(matrixPos[0]+x*27,matrixPos[1]+y*27))

    # draws held piece
    if heldpiece != 0:
        heldletter = pieces[heldpiece]   # letter id of held piece
        screen.blit(holdblocks[heldpiece],(matrixPos[0]-78,matrixPos[1]+10))
                    
    # draws pieces in queue
    for a in range(len(queue)):
        queueletter = pieces[queue[a]]
        if a == 0:
            screen.blit(holdblocks[queue[a]],(matrixPos[0]+268,matrixPos[1]+10))
        else:
            screen.blit(queueblocks[queue[a]],(matrixPos[0]+285,matrixPos[1]+60+a*50))
            
    # draws score
    for a in range(len(str(score))-1,-1,-1):
        screen.blit(scorenums[int(str(score)[a])],(matrixPos[0]+250-(len(str(score))-a)*26,matrixPos[1]-40))

    # draws level
    for a in range(16):
        if level == a:
            screen.blit(levelnums[a],(matrixPos[0]+170,matrixPos[1]+546))

    # draws goal
    for a in range(11):
        if goal == a:
            screen.blit(goalnums[a],(matrixPos[0]+288,matrixPos[1]+495))
    
    # find ghost piece postition

    if ghost == True:
        tempPos = piecePos[::]  # temporary variable to remember original spot of piece
        
        while boundaryCheck("Down") and collisionCheck("Down"):
            # keeps moving ghost piece down to lowest posible spot
            move("Down")

        # draws ghost piece on newSurface
        for a in range(len(letter)):      
            for b in range(len(letter[0])):
                if letter[a][b] == idn:
                    if piecePos[0]+a >= 0:
                        screen.blit(ghostblocks[idn],((matrixPos[0]+piecePos[1]*27)+27*b,(matrixPos[1]+piecePos[0]*27)+27*a))

        piecePos = tempPos      # resets active piece to original spot 

    # draws active piece 
    for a in range(len(letter)):      
        for b in range(len(letter[0])):
            if letter[a][b] == idn:
                if piecePos[0]+a >= 0:
                    screen.blit(blocks[idn],((matrixPos[0]+piecePos[1]*27)+27*b,(matrixPos[1]+piecePos[0]*27)+27*a))

            
def move(direction):   
    # Moves pieces regardless of collisions, collisions will be checked before
    global piecePos
    
    if direction == "Right":
        piecePos[1] +=1
    if direction == "Left":
        piecePos[1] -=1
    if direction == "Down":
        piecePos[0] +=1


def dropPiece():
    # used when spacebar is pressed down for "smashing" pieces down
    global score

    count = 0
    while boundaryCheck("Down") and collisionCheck("Down"):
        move("Down")    # keeps on moving piece down until it collides
        count += 1

    score += count*level    # points are added depending on how high the piece is dropped
    display.flip()
    setPiece()
    nextPiece()
    
    
def boundaryCheck(direction):
    # checks for the boundaries of the piece on the matrix 
    
    if direction == "Left":
        # checks for block on piece matrix most on left
        minx = 9999     # temporary value to check for min position
        for a in range(len(letter)):
            for b in range(len(letter[0])):
                if letter[a][b] != 0:
                    minx = min(minx,b)  # compares positions and finds most left block
        if minx+piecePos[1] < 1:  # if passes left boundary of matrix returns False
            return False
        
    elif direction == "Right":
        # checks for block on piece matrix most on right
        maxx = 0    #temporary value to check for max position
        for a in range(len(letter)):
            for b in range(len(letter[0])): 
                if letter[a][b] != 0:
                    maxx = max(maxx,b)  # compares positions and finds most right block
        if maxx+piecePos[1] > 8:  # if passes right boundary of matrix returns False
            return False
        
    elif direction == "Down":
        # checks for block on piece matrix most on right
        maxy = 0    #temporary value to check for max position
        for a in range(len(letter)):
            for b in range(len(letter[0])):
                if letter[a][b] != 0:
                    maxy = max(maxy,a)  # compares positions and finds most bottom block
        if maxy+piecePos[0]+1 > 19: # if passes bottom boundary of matrix returns False
            return False
        
    return True     # if it passes boundary check, returns True


def collisionCheck(direction):
    # will not be called if boundaryCheck returns False, already a collision
    # checks for collisions with already set blocks on matrix
    
    if direction == "Left":
        for a in range(len(letter)):
            for b in range(len(letter[0])):
                if letter[a][b] != 0:   
                    if matrix[piecePos[0]+a][piecePos[1]+b-1] != 0:
                        # if one spot over to left has collision, returns False
                        return False
                
    if direction == "Right":
        for a in range(len(letter)):
            for b in range(len(letter[0])):
                if letter[a][b] != 0:
                    if matrix[piecePos[0]+a][piecePos[1]+b+1] != 0:
                        # if one spot over to right has collision, returns False
                        return False
                    
    if direction == "Down":
        for a in range(len(letter)):
            for b in range(len(letter[0])):
                if letter[a][b] != 0:
                    if matrix[piecePos[0]+a+1][piecePos[1]+b] != 0:
                        # if one spot lower has collision, returns False
                        return False
                    
    return True     # if theres no collision, returns True
                    

def rotateRight():
    # rotates piece clockwise
    global letter
    
    tempPiece = letter # remember original piece matrix just incase you can't rotate
    letter = list(zip(*letter[::-1]))   # rotates piece matrix clockwise
    if checkOverlap() and rotationNudge():
        # if theres an overlap or no space to nudge, doesn't rotate and changes piece back
        letter = tempPiece


def rotateLeft():       
    # rotates piece counterclockwise
    global letter

    tempPiece = letter
    letter = list(zip(*letter))[::-1]   # rotates piece matrix counterclockwise
    if checkOverlap() and rotationNudge():
        letter = tempPiece


def checkOverlap():
    # used to when rotating pieces, to check if rotation on spot is possible
    
    for a in range(len(letter)):
        for b in range(len(letter[0])):
            if letter[a][b] != 0:
                if piecePos[0]+a > 19 or piecePos[1]+b > 9 or piecePos[1]+b < 0:
                    # check if its out of matrix bounds
                    return True 
                if matrix[piecePos[0]+a][piecePos[1]+b] != 0:
                    # check if it overlaps with already set blocks on matrix
                    return True
                
    return False    # no overlap, returns False


def rotationNudge():
    # used when checkOverlap is True, then checks if piece can nudge over by a unit to rotate
    global piecePos

    if len(letter) == 4:
        for direc in [[0,1],[0,-1],[-1,0],[0,2],[0,-2],[-2,0]]:     # "I" piece has more cases because of its shape
            count = 0
            for a in range(len(letter)):
                for b in range(len(letter[0])):
                    if letter[a][b] != 0:
                        # checks if all block positions of the piece are unoccupied 
                        if piecePos[0]+a+direc[0] <= 19 and piecePos[1]+b+direc[1] <= 9 and piecePos[1]+b+direc[1] >= 0 :
                            if matrix[piecePos[0]+a+direc[0]][piecePos[1]+b+direc[1]] == 0:
                                count += 1
                if count == 4:  # if all are unoccupied, nudges piece in the direction
                    piecePos = [piecePos[0]+direc[0],piecePos[1]+direc[1]]
                    return False
        
    else:
        for direc in [[0,1],[0,-1],[-1,0]]:     # all possible directions you can nudge piece
            count = 0
            for a in range(len(letter)):
                for b in range(len(letter[0])):
                    if letter[a][b] != 0:
                        if piecePos[0]+a+direc[0] <= 19 and piecePos[1]+b+direc[1] <= 9 and piecePos[1]+b+direc[1] >= 0 :
                            if matrix[piecePos[0]+a+direc[0]][piecePos[1]+b+direc[1]] == 0:
                                count += 1
                if count == 4:  
                    piecePos = [piecePos[0]+direc[0],piecePos[1]+direc[1]]
                    return False
    return True


def setPiece():
    # sets piece onto matrix if there are no collisions
    global matrix
    
    for a in range(len(letter)):
        for b in range(len(letter[0])):
            if letter[a][b] != 0:
                matrix[piecePos[0]+a][piecePos[1]+b] = idn


def nextPiece():
    # restarts with next piece in queue when previous piece is set
    global idn,queue,piecePos,letter,hold,dropcounter,gameover

    # if player did not already lose, goes onto next piece
    if not endGame():
        idn = queue.pop(0)
        letter = pieces[idn]

        # determines starting position of piece
        miny = 9999     # temporary value to check for min position
        for a in range(len(letter)):
            for b in range(len(letter[0])):
                if letter[a][b] != 0:
                    miny = min(miny,a)  # compares positions and finds most high block
        
        if letter == I:
            piecePos = [-1,3]
        else:
            piecePos = [(miny+1)*-1,6-len(letter[0])]
        
        newpiece = randint(1,7)
        while newpiece in queue:
            newpiece = randint(1,7)
        queue.append(newpiece)  # adds another piece to queue since took one out       
        hold = False     # new piece lets you hold once per turn
        dropcounter = 16-level
        timer = 20

    # if player loses, quits game    
    else:
        gameover = True
        

def endGame():
    # checks if player lost the game
    
    if matrix[0][4] != 0:   # all starting pieces use this position
        return True
    return False
    

def holdPiece():
    # switches active piece with heldpiece
    global heldpiece,idn,letter,piecePos,hold

    if hold == False:
        if heldpiece == 0:
            heldpiece = idn
            nextPiece()
        else:
            heldpiece, idn = idn, heldpiece
            letter = pieces[idn]
            piecePos = [0,4]
        hold = True


def clear():
    # clears full lines and also checks if player goes onto next level
    global matrix,goal,level,score,lines

    full = []   # list of lines that are full to clear
    for a in range(20):
        count = 0 # counter to check if line 'a' is full
        for b in range(10):
            if matrix[a][b] != 0:
                count += 1
        if count == 10:     # if full adds full line into list 
            full.append(a)
            count = 0
        if a == 19 and len(full) != 0:
            lines += len(full)
            goal -= len(full)
            time.wait(200)
            score += len(full)*100*level
            for c in range(len(full)):
                del matrix[full[c]]
                matrix = [[0 for i in range(10)]] + matrix  

    if newLevel():
        level += 1

def newLevel():
    global goal,gameover
    # checks if player has completed enough lines to go onto next level
    
    if goal <= 0 and level < 15:
        goal = goal + 10
        return True
    if goal <= 0 and level == 15:
        gameover = True
    return False

def newGame():
    # sets everything to default for a new game
    global matrix,level,score,lines,dropcounter,timer,queue,idn,letter,heldpiece,holdcheck,piecePos,game

    game = False
    matrix = [[0]*10 for i in range (23)]
    level = 1
    score = 0
    lines = 0
    dropcounter = 16-level
    timer = 20
    queue = []
    while len(queue) != 4:
        new = randint(1,7)
        if new not in queue:
            queue.append(new)

    idn = queue.pop(0)
    letter = pieces[idn]
    heldpiece = 0
    holdcheck = False

    miny = 9999
    for a in range(len(letter)):
        for b in range(len(letter[0])):
            if letter[a][b] != 0:
                miny = min(miny,a)

    if letter == I:
        piecePos = [-1,3]
    else:
        piecePos = [(miny+1)*-1,6-len(letter[0])]
    
# MENU FUNCTIONS ----------------------------------------------------------------
            
def mainMenu():
    global pause, menu
    
    running = True
    while running:
        click = False
        for e in event.get():
            if e.type == QUIT:
                return "quit"
            if e.type == MOUSEBUTTONDOWN:
                if e.button == 1:
                    click = True

        mx,my = mouse.get_pos() 
        pause = False
        menu = True
        screen.blit(mainmenu,(0,0))
        
        if mainMarathonRect.collidepoint(mx,my):
            screen.blit(mainmarathon,(0,0))
            if click and played == False:   # if there is no saved game, starts a new game
                return "marathon"
            elif click:
                return "selection"

        if mainStatisticsRect.collidepoint(mx,my):
            screen.blit(mainstatistics,(0,0))
            if click:
                return "statistics"

        if mainOptionsRect.collidepoint(mx,my):
            screen.blit(mainoptions,(0,0))
            if click:
                return "options"

        if mainHelpRect.collidepoint(mx,my):
            screen.blit(mainhelp,(0,0))
            if click:
                return "helpp"

        if mainExitRect.collidepoint(mx,my):
            screen.blit(mainexit,(0,0))
            if click:
                return "mainexitt"

        display.flip()


def selection():
    running = True
    while running:
        click = False
        for e in event.get():          
            if e.type == QUIT:
                return "quit"
            if e.type == MOUSEBUTTONDOWN:
                click = True
        display.flip()
        mx,my = mouse.get_pos()
        screen.blit(selectionmenu,(0,0))

        if continueRect.collidepoint(mx,my):
            screen.blit(selectioncontinue,(0,0))
            if click:
                return "marathon"

        if newGameRect.collidepoint(mx,my):
            screen.blit(selectionnewgame,(0,0))
            if click:
                return "confirm"
            
        if backRect.collidepoint(mx,my):
            if click:
                return "mainMenu"
                 

def confirm():
    running = True
    while running:
        click = False
        for e in event.get():          
            if e.type == QUIT:
                return "quit"
            if e.type == MOUSEBUTTONDOWN:
                click = True
        display.flip()
        mx,my = mouse.get_pos()
        screen.blit(confirmmenu,(0,0))

        if confirmYesRect.collidepoint(mx,my):
            screen.blit(confirmyes,(0,0))
            if click:
                newGame()
                return "marathon"

        if confirmNoRect.collidepoint(mx,my):
            screen.blit(confirmno,(0,0))
            if click:
                return "selection"    


def statistics():
    global highscore,highlines
    
    running = True
    screen.blit(statisticspage,(0,0))
    highscore,highlines = open("Statistics.txt").read().strip().split(",")  # gets highscores from textfile
    text = arialFont.render(highscore,True,(255,255,255))
    text2 = arialFont.render(highlines,True,(255,255,255))
    screen.blit(text,(250,313))
    screen.blit(text2,(250,355))
    while running:
        click = False
        for e in event.get():          
            if e.type == QUIT:
                return "quit"
            if e.type == MOUSEBUTTONDOWN:
                click = True
        display.flip()
        mx,my = mouse.get_pos()
        
        if backRect.collidepoint(mx,my):
            if click:
                return "mainMenu"


def options():
    global music,sfx,ghost
    
    running = True
    while running:
        click = False
        for e in event.get():          
            if e.type == QUIT:
                return "quit"
            if e.type == MOUSEBUTTONDOWN:
                click = True
        display.flip()
        mx,my = mouse.get_pos()
        screen.blit(optionsblankpage,(0,0))

        # draws current state of options
        if music == True:
            screen.blit(musicon,(91,228))
        if music == False:
            screen.blit(musicoff,(90,228))
            
        if sfx == True:
            screen.blit(sfxon,(91,299))
        if sfx == False:
            screen.blit(sfxoff,(90,301))
        
        if ghost == True:
            screen.blit(ghoston,(90,370))
        if ghost == False:
            screen.blit(ghostoff,(90,372))
            

        if musicRect.collidepoint(mx,my):
            if music == True:
                screen.blit(musiconhover,(90,231))
                if click:
                    music = False
            elif music == False:
                screen.blit(musicoffhover,(90,234))
                if click:
                    music= True

        if sfxRect.collidepoint(mx,my):
            if sfx == True:
                screen.blit(sfxonhover,(91,303))
                if click:
                    sfx = False
            elif sfx == False:
                screen.blit(sfxoffhover,(90,306))
                if click:
                    sfx= True
                    
        if ghostRect.collidepoint(mx,my):
            if ghost == True:
                screen.blit(ghostonhover,(90,373))
                if click:
                    ghost = False
            elif ghost == False:
                screen.blit(ghostoffhover,(90,374))
                if click:
                    ghost= True  
        
        if backRect.collidepoint(mx,my):
            if click:
                if menu == True:    # checks from which menu you came from
                    return "mainMenu"  
                if pause == True:
                    return "pauseMenu"


def helpp():
    running = True
    while running:
        click = False
        for e in event.get():          
            if e.type == QUIT:
                return "quit"
            if e.type == MOUSEBUTTONDOWN:
                click = True
        display.flip()
        mx,my = mouse.get_pos()

        screen.blit(helpmenu,(0,0))
        
        if helpIntroRect.collidepoint(mx,my):
            screen.blit(helpintro,(0,0))
            if click:
                return "intro"
        if helpBasicsRect.collidepoint(mx,my):
            screen.blit(helpbasics,(0,0))
            if click:
                return "basics1"
        if helpMarathonRect.collidepoint(mx,my):
            screen.blit(helpmarathon,(0,0))
            if click:
                return "marathonHelp"
        if helpControlsRect.collidepoint(mx,my):
            screen.blit(helpcontrols,(0,0))
            if click:
                return "controls"

        if helpSpecialsRect.collidepoint(mx,my):
            screen.blit(helpspecials,(0,0))
            if click:
                return "specials1"
            
        if helpOptionsRect.collidepoint(mx,my):
            screen.blit(helpoptions,(0,0))
            if click:
                return "aboutoptions"

        if backRect.collidepoint(mx,my):
            if click:
                if menu == True:
                    return "mainMenu"  
                if pause == True:
                    return "pauseMenu"


def intro():
    running = True
    screen.blit(intropage,(0,0))
    while running:
        click = False
        for e in event.get():          
            if e.type == QUIT:
                return "quit"
            if e.type == MOUSEBUTTONDOWN:
                click = True
        display.flip()
        mx,my = mouse.get_pos()
        
        if backRect.collidepoint(mx,my):
            if click:
                return "helpp"


def basics1():
    running = True
    screen.blit(basics1page,(0,0))
    while running:
        click = False
        for e in event.get():          
            if e.type == QUIT:
                return "quit"
            if e.type == MOUSEBUTTONDOWN:
                click = True
        display.flip()
        mx,my = mouse.get_pos()
        
        if nextPage.collidepoint(mx,my):
            if click:
                return "basics2"
        if backRect.collidepoint(mx,my):
            if click:
                return "helpp"


def basics2():
    running = True
    screen.blit(basics2page,(0,0))
    while running:
        click = False
        for e in event.get():          
            if e.type == QUIT:
                return "quit"
            if e.type == MOUSEBUTTONDOWN:
                click = True
        display.flip()
        mx,my = mouse.get_pos()
        
        if previousPage.collidepoint(mx,my):
            if click:
                return "basics1"
        if backRect.collidepoint(mx,my):
            if click:
                return "helpp"


def marathonHelp():
    running = True
    screen.blit(marathonpage,(0,0))
    while running:
        click = False
        for e in event.get():          
            if e.type == QUIT:
                return "quit"
            if e.type == MOUSEBUTTONDOWN:
                click = True
        display.flip()
        mx,my = mouse.get_pos()
        
        if backRect.collidepoint(mx,my):
            if click:
                return "helpp"


def controls():
    running = True
    screen.blit(controlspage,(0,0))
    while running:
        click = False
        for e in event.get():          
            if e.type == QUIT:
                return "quit"
            if e.type == MOUSEBUTTONDOWN:
                click = True
        display.flip()
        mx,my = mouse.get_pos()
        
        if backRect.collidepoint(mx,my):
            if click:
                return "helpp"

    
def specials1():
    running = True
    screen.blit(specials1page,(0,0))
    while running:
        click = False
        for e in event.get():          
            if e.type == QUIT:
                return "quit"
            if e.type == MOUSEBUTTONDOWN:
                click = True
        display.flip()
        mx,my = mouse.get_pos()
        
        if nextPage.collidepoint(mx,my):
            if click:
                return "specials2"
        if backRect.collidepoint(mx,my):
            if click:
                return "helpp"


def specials2():
    running = True
    screen.blit(specials2page,(0,0))
    while running:
        click = False
        for e in event.get():          
            if e.type == QUIT:
                return "quit"
            if e.type == MOUSEBUTTONDOWN:
                click = True
        display.flip()
        mx,my = mouse.get_pos()
        
        if previousPage.collidepoint(mx,my):
            if click:
                return "specials1"
        if backRect.collidepoint(mx,my):
            if click:
                return "helpp"


def aboutoptions():
    running = True
    screen.blit(optionspage,(0,0))
    while running:
        click = False
        for e in event.get():          
            if e.type == QUIT:
                return "quit"
            if e.type == MOUSEBUTTONDOWN:
                click = True
        display.flip()
        mx,my = mouse.get_pos()
        
        if backRect.collidepoint(mx,my):
            if click:
                return "helpp"
    

def mainexitt():
    running = True
    while running:
        click = False
        for e in event.get():          
            if e.type == QUIT:
                return "quit"
            if e.type == MOUSEBUTTONDOWN:
                click = True
        display.flip()
        mx,my = mouse.get_pos()

        screen.blit(mainexitpage,(0,0))
        if mainExitYesRect.collidepoint(mx,my):
            screen.blit(mainexityes,(0,0))
            if click:
                return "quit"
        if mainExitNoRect.collidepoint(mx,my):
            screen.blit(mainexitno,(0,0))
            if click:
                return "mainMenu"

            
def pauseMenu():
    global pause, menu, matrix
    
    running = True
    game = False
    while running:
        click = False
        for e in event.get():
            if e.type == QUIT:
                return "quit"
            if e.type == MOUSEBUTTONDOWN:
                if e.button == 1:
                    click = True

        mx,my = mouse.get_pos() 
        pause = True
        menu = False
        screen.blit(pausemenu,(0,0))
        if pauseResumeRect.collidepoint(mx,my):
            screen.blit(pauseresume,(0,0))
            if click:
                return "marathon"

        if pauseRestartRect.collidepoint(mx,my):
            screen.blit(pauserestart,(0,0))
            if click:
                return "pauseRestart"

        if pauseOptionsRect.collidepoint(mx,my):
            screen.blit(pauseoptions,(0,0))
            if click:
                return "options"

        if pauseHelpRect.collidepoint(mx,my):
            screen.blit(pausehelp,(0,0))
            if click:
                return "helpp"

        if pauseMainRect.collidepoint(mx,my):
            screen.blit(pausemain,(0,0))
            if click:
                return "pauseexit"
        display.flip()


def pauseRestart():
    running = True
    while running:
        click = False
        for e in event.get():          
            if e.type == QUIT:
                return "quit"
            if e.type == MOUSEBUTTONDOWN:
                click = True
        display.flip()
        mx,my = mouse.get_pos()

        screen.blit(pauserestartpage,(0,0))
        if pauseRestartYesRect.collidepoint(mx,my):
            screen.blit(pauserestartyes,(0,0))
            if click:
                newGame()
                return "marathon"
        if pauseRestartNoRect.collidepoint(mx,my):
            screen.blit(pauserestartno,(0,0))
            if click:
                return "pauseMenu"
    
    
def pauseexit():
    running = True
    while running:
        click = False
        for e in event.get():          
            if e.type == QUIT:
                return "quit"
            if e.type == MOUSEBUTTONDOWN:
                click = True
        display.flip()
        mx,my = mouse.get_pos()

        screen.blit(pauseexitpage,(0,0))
        if pauseExitYesRect.collidepoint(mx,my):
            screen.blit(pauseexityes,(0,0))
            if click:
                return "mainMenu"
        if pauseExitNoRect.collidepoint(mx,my):
            screen.blit(pauseexitno,(0,0))
            if click:
                return "pauseMenu"


def endPage():
    global gameover,played
    
    running = True
    while running:
        click = False
        for e in event.get():          
            if e.type == QUIT:
                return "quit"
            if e.type == MOUSEBUTTONDOWN:
                click = True
        mx,my = mouse.get_pos()
        screen.blit(gamepage,(0,0))

        gameover = False
        played = False
        if playAgainRect.collidepoint(mx,my):
            screen.blit(gamehover,(0,0))
            if click:
                newGame()
                return "marathon"
        if backRect.collidepoint(mx,my):
            if click:
                newGame()
                return "mainMenu"

        highscore,highlines = open("Statistics.txt").read().strip().split(",")
        
        if score > int(highscore):      # if user's score is higher than highscore, oversaves
            statsFile = open("Statistics.txt","w")
            statsFile.write(str(score)+","+str(highlines))
            statsFile.close()
                        
        if lines > int(highlines):      # same with lines sent
            statsFile = open("Statistics.txt","w")
            statsFile.write(str(highscore)+","+str(lines))
            statsFile.close()
            
        highscore,highlines = open("Statistics.txt").read().strip().split(",")
        text = arialFont.render(highscore,True,(255,255,255))
        text2 = arialFont.render(highlines,True,(255,255,255))
        screen.blit(text,(250,313))
        screen.blit(text2,(250,350))
        display.flip()
    
def playmusic():
    if music == True:
        mixer.music.load("Music/TetrisMenuTheme.mp3")
        mixer.music.play(-1)
    else:
        mixer.music.stop()
        
        
running = True
pause = False
menu = True
action = "mainMenu"

while action != "quit":
    playmusic()
    if action == "mainMenu":
        action = mainMenu()
    if action == "marathon":
        action = marathon()
    if action == "selection":
        action = selection()
    if action == "confirm":
        action = confirm()
    if action == "statistics":
        action = statistics()
    if action == "options":
        action = options()
    if action == "helpp":
        action = helpp()
    if action == "intro":
        action = intro()
    if action == "basics1":
        action = basics1()
    if action == "basics2":
        action = basics2()
    if action == "marathonHelp":
        action = marathonHelp()
    if action == "controls":
        action = controls()
    if action == "specials1":
        action = specials1()
    if action == "specials2":
        action = specials2()
    if action == "aboutoptions":
        action = aboutoptions()
    if action == "pauseMenu":
        action = pauseMenu()
    if action == "pauseRestart":
        action = pauseRestart()
    if action == "pauseexit":
        action = pauseexit()
    if action == "mainexitt":
        action = mainexitt()
    if action == "endPage":
        action = endPage()
    
quit()
    
