#########################
## MAIN MENU OF TETRIS ##
#########################


from pygame import *
from pprint import *
from random import *

screen = display.set_mode((450,750))
display.set_caption("Tetris")

#start up page
load = image.load("logo.png")
screen.blit(load,(0,0))
display.flip()
time.wait(1000)

background = image.load("mainmenu.png")
screen.blit(background,(0,0))

#Rects and Image Loading
marathonRect = Rect(92,290,266,35)
marathon = image.load("mainmenu - marathon.png")
statisticsRect = Rect(92,360,266,35)
statistics = image.load("mainmenu - statistics.png")
optionsRect = Rect(92,430,266,35)
options = image.load("mainmenu - options.png")
helpaboutRect = Rect(92,500,266,35)
helpabout = image.load("mainmenu - help.png")
mmexitRect = Rect(92,570,266,35)
mmexit = image.load("mainmenu - exit.png")
grid = image.load("grid.png")

action = ""

running = True
while running:
    click = False
    for e in event.get():
        if e.type == QUIT:
            running = False
        if e.type == MOUSEBUTTONDOWN:
            click = True

    mx,my = mouse.get_pos()
    mb=mouse.get_pressed()

    screen.blit(background,(0,0))
            
    if marathonRect.collidepoint(mx,my):
        screen.blit(marathon,(0,0))
        if click:
            action = "game"
        
    if statisticsRect.collidepoint(mx,my):
        screen.blit(statistics,(0,0))
        if click:
            action = "statistics"
        
    if optionsRect.collidepoint(mx,my):
        screen.blit(options,(0,0))
        if click:
            action = "options"
        
    if helpaboutRect.collidepoint(mx,my):
        screen.blit(helpabout,(0,0))
        if click:
            action = "help"
        
    if mmexitRect.collidepoint(mx,my):
        screen.blit(mmexit,(0,0))
        if click:
            action = "exit"

    if action == "game":
        screen = display.set_mode((450,750))
        background = image.load("Grid.png")
        screen.blit(background,(0,0))
        #matrixPos = [400,100]       # x,y
        matrixPos = [92,117]

        matrix = [[0]*10 for i in range (20)]
        dropcounter = 10

        colours = [(0,0,0),(0,240,239),(241,240,0),(1,240,0),(240,0,1),(240,160,0),(0,0,245),(159,0,240)]

        heldpiece = 0       # held piece idn number
        holdcheck = False   # checks if you just used hold or not since you can only use hold once per active piece

        queue = []
        while len(queue) != 4:  # randomly chooses 3 pieces that don't repeat
            new = randint(1,7)
            if new not in queue:
                queue.append(new)

        idn = queue.pop(0)  # identification number of piece 

        piecePos = [0,4]   #row, column of (0,0) of piece matrixes on actual matrix 

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

        letter = pieces[idn]    # letter of piece according to piece idn

        def drawMatrix(matrixPos):        # draws current state of matrix
            global colours,matrix,end,collide,piecePos,idn,dropcounter,piece

            # draws grid
            for s in range(20):         
                for e in range(10):
                    draw.rect(screen,(175,175,175),(matrixPos[0]+e*27,matrixPos[1]+s*27,27,27),1)
                    
            # draws current blocks on matrix        
            for x in range(10):     
                for y in range(20):
                    draw.rect(screen,colours[matrix[y][x]],(matrixPos[0]+x*27+1,matrixPos[1]+y*27+1,25,25))

        ##    # draws held piece
        ##    if heldpiece != 0:
        ##        heldletter = pieces[heldpiece]   # letter id of held piece
        ##        draw.rect(screen,(255,255,255),(matrixPos[0]-100,matrixPos[1],80,80))
        ##        for a in range(4):      # draws held piece on side     
        ##            for b in range(4):
        ##                if heldletter[a][b] == heldpiece:
        ##                    draw.rect(screen,colours[heldpiece],((matrixPos[0]-100)+20*b,(matrixPos[1])+20*a,20,20))
                            
            # draws active piece 
            for a in range(len(letter)):      
                for b in range(len(letter[0])):
                    if letter[a][b] == idn:
                        draw.rect(screen,colours[idn],((matrixPos[0]+piecePos[1]*27)+27*b+1,(matrixPos[1]+piecePos[0]*27)+27*a+1,25,25))

            # draws ghost piece
            newSurface = Surface((800,800),SRCALPHA)    # allows transparency on newSurface 
            tempPos = piecePos[::]  # temporary position to reset active piece to 
            
            while boundaryCheck("Down") and collisionCheck("Down"):
                # keeps moving ghost piece down to lowest posible spot
                move("Down")

            # draws ghost piece on newSurface
            for a in range(len(letter)):      
                for b in range(len(letter[0])):
                    if letter[a][b] == idn:
                        draw.rect(newSurface,list(colours[idn])+[175],((matrixPos[0]+piecePos[1]*27)+27*b+1,(matrixPos[1]+piecePos[0]*27)+27*a+1,25,25))
                        
            screen.blit(newSurface,(0,0))   # blits on surface so you can see ghost piece
            piecePos = tempPos      # resets active piece to original spot
            
        def clear():
            global matrix
            
            for a in range(20):
                count = 0 # counter to check if line 'a' is full
                for b in range(10):
                    if matrix[a][b] != 0:
                        count += 1
                if count == 10:     # if full, deletes line and adds new line on top
                    time.wait(300)
                    del matrix[a]
                    matrix = [[0 for i in range(10)]] + matrix

        running = True
        myClock = time.Clock()

        def boundaryCheck(direction):
            if direction == "Left":
                minx = 9999 # temporary value to check for minimum
                for a in range(len(letter)):
                    for b in range(len(letter[0])):
                        if letter[a][b] != 0:
                            minx = min(minx,b)
                if minx+piecePos[1]-1 < 0:
                    return False
            elif direction == "Right":
                maxx = 0 #temporary value to check for max position
                for a in range(len(letter)):
                    for b in range(len(letter[0])):
                        if letter[a][b] != 0:
                            maxx = max(maxx,b)
                
                if maxx+piecePos[1]+1 > 9:
                    return False
            elif direction == "Down":
                maxy = 0
                for a in range(len(letter)):
                    for b in range(len(letter[0])):
                        if letter[a][b] != 0:
                            maxy = max(maxy,a)
                if maxy+piecePos[0]+1 > 19:
                    return False
            return True

        #will not be called if boundaryCheck returns false
        def collisionCheck(direction):
            if direction == "Left":
                for a in range(len(letter)):
                    for b in range(len(letter[0])):
                        if letter[a][b] != 0:
                            if matrix[piecePos[0]+a][piecePos[1]+b-1] != 0:
                                return False
                        
            if direction == "Right":
                for a in range(len(letter)):
                    for b in range(len(letter[0])):
                        if letter[a][b] != 0:
                            if matrix[piecePos[0]+a][piecePos[1]+b+1] != 0:
                                return False
            if direction == "Down":
                for a in range(len(letter)):
                    for b in range(len(letter[0])):
                        if letter[a][b] != 0:
                            if matrix[piecePos[0]+a+1][piecePos[1]+b] != 0:
                                return False
            return True
                            
        #Makes a move regardless of collisions (should be checked before this
        #function is called

        def move(direction):
            global piecePos
            if direction == "Right":
                piecePos[1] +=1
            if direction == "Left":
                piecePos[1] -=1
            if direction == "Down":
                piecePos[0] +=1

        def setPiece():
            global matrix
            for a in range(len(letter)):
                for b in range(len(letter[0])):
                    if letter[a][b] != 0:
                        matrix[piecePos[0]+a][piecePos[1]+b] = letter[a][b]

        def nextPiece():
            global idn,queue,piecePos,letter
            
            idn = queue.pop(0)
            letter = pieces[idn]

            newpiece = randint(1,7)
            while newpiece in queue:
                newpiece = randint(1,7)
            queue.append(newpiece)
            piecePos = [1,4]

        def dropPiece():
            while boundaryCheck("Down") and collisionCheck("Down"):
                move("Down")
            setPiece()
            nextPiece()

        def checkOverlap():
            for a in range(len(letter)):
                for b in range(len(letter[0])):
                    if letter[a][b] != 0:
                        if piecePos[0]+a > 19 or piecePos[1]+b > 9 or piecePos[1]+b < 0:
                            return False # check out of bounds
                        if matrix[piecePos[0]+a][piecePos[1]+b] != 0:
                            return False # check overlaps
            return True

        def rotateRight():
            global letter
            tempPiece = letter # remember just incase you can't rotate
            letter = list(zip(*letter[::-1]))
            if not checkOverlap(): #there's overlap
                letter = tempPiece
            
            

        while running:
            for e in event.get():
                if e.type == QUIT:
                    running = False
                if e.type == KEYDOWN:
                    if e.key == K_SPACE:
                        dropPiece()
                    elif e.key == K_UP:
                        rotateRight()
                        
            hold = False
            
            keys = key.get_pressed()                    

            if keys[K_LEFT]:
                # moves left only if it doesn't move out of matrix or collide into another block
                if boundaryCheck("Left") and collisionCheck("Left"):     
                    move("Left")
            if keys[K_RIGHT]:
                # moves right only if it doesn't move out of matrix or collide into another block
                if boundaryCheck("Right") and collisionCheck("Right"):
                    move("Right")
            if keys[K_DOWN]:
                # moves down only if it doesn't move out of matrix or collide into another block
                if boundaryCheck("Down") and collisionCheck("Down"):
                    move("Down")
                else:
                    # sets piece on matrix and goes to next piece on queue if piece can no longer move
                    setPiece()
                    nextPiece()
                dropcounter = 10
                
            dropcounter-=1
            
            if dropcounter == 0:
                # moves piece one unit down per second if it doesn't move out of matrix and doesn't
                # collide into other blocks
                if boundaryCheck("Down") and collisionCheck("Down"):
                    move("Down")
                    dropcounter = 10
                else:
                    # sets piece on matrix and goes to next piece on queue if piece can no longer move
                    setPiece()
                    nextPiece()
                    
            drawMatrix(matrixPos)
            display.flip()
            clear()
            
            myClock.tick(10)
        quit()

##    if action == "statistics"
##
##    if action == "options"
##
##    if action == "help"

    if action == "exit":
        quit()
        break
        
    print(mx,my)
    display.flip()
quit()

