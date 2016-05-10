###########################
## Pause Menu for Tetris ##
###########################

from pygame import *

screen = display.set_mode((450,750))
display.set_caption("Tetris")

background = image.load("pausemenu.png")
screen.blit(background,(0,0))

resumeRect = Rect(92,240,266,35)
resume = image.load("pause-resume.png")
restartRect = Rect(92,310,266,35)
restart = image.load("pause-restart.png")
optionsRect = Rect(92,380,266,35)
options = image.load("pause-options.png")
pausehelpRect = Rect(92,450,266,35)
pausehelp = image.load("pausemenu-help.png")
mainmenuRect = Rect(92,520,266,35)
mainmenu = image.load("pause-mainmenu.png")
grid = image.load("grid copy.png")
exitmm = image.load("exitmm.png")
yesRect = Rect(92,350,266,35)
yes = image.load("yes.png")
noRect = Rect(92,420,266,35)
no = image.load("no.png")

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
            
    if resumeRect.collidepoint(mx,my):
        screen.blit(resume,(0,0))
        if click:
            action = "game"
    if action == "game":
        screen.blit(grid,(0,0))
        
    if restartRect.collidepoint(mx,my):
        screen.blit(restart,(0,0))
        if click:
            action = "restart"
    if action == "restart":
        screen.blit(grid,(0,0))
        
    if optionsRect.collidepoint(mx,my):
        screen.blit(options,(0,0))
        
    if pausehelpRect.collidepoint(mx,my):
        screen.blit(pausehelp,(0,0))
        
    if mainmenuRect.collidepoint(mx,my):
        screen.blit(mainmenu,(0,0))
        if click:
            action = "main menu"
    if action == "main menu":
        screen.blit(exitmm,(0,0))
        if yesRect.collidepoint(mx,my):
            screen.blit(yes,(0,0))
        if noRect.collidepoint(mx,my):
            screen.blit(no,(0,0))
        
      
        
    print(mx,my)
    display.flip()
quit()
