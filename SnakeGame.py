import pygame,sys
import time
import random

pygame.init()

white=(255,255,255)
black=(100,0,0)
red=(255,0,0)
winheight=600
winwidth=800

gamedisplay=pygame.display.set_mode((winheight,winwidth))
pygame.display.set_caption('Snake')
font=pygame.font.SysFont(None,25,bold=True)

def myquit():
    pygame.quit()
    sys.exit(0)
    
'''----------------------------------------------------------------------------------------------------------------------------------------------'''

clock=pygame.time.Clock()                                               #create an object to track time
fps=5
blocksize=20
nopixel=0

'''----------------------------------------------------------------------------------------------------------------------------------------------'''

def snake(blocksize,snakelist):
    for size in snakelist:
        pygame.draw.rect(gamedisplay,black, [size[0]+5,size[1],blockSize,blockSize],2)

def msg_to_screen(msg,color):
    text=font.render(msg,True,color)
    gamedisplay.blit(text,[winwidth/2,winheight/2])

'''----------------------------------------------------------------------------------------------------------------------------------------------'''

def gameloop():
    gameexit=False
    gameover=False                                  #deteremine if loop stops or continue

    leadx=winwidth/2
    leady=winheight/2

    changepixelsofx=0
    changepixelsofy=0

    snakelist=[]
    snakelength=1

    randomapplex=round(random.randrange(0,winwidth-blocksize)/10)*10
    randomappley=round(random.randrange(0,winheight-blocksize)/10)*10    

    while not gameexit:

        while gameover==True:
            gamedisplay.fill(white)
            message_to_screen('Game over! press c to play again or q to quit...!')
            pygame.display.update()

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    gameover=False
                    gameexit=True

                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K__q:
                        gameexit=True
                        gameover=False
                    if event.key==pygame.K__c:
                        gameloop()


            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    gameexit=True

                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:
                        myquit()
                    left=event.key==pygame.K_LEFT
                    right=event.key==pygame.K_RIGHT
                    up=event.key==pygame.K_UP
                    down=event.key==pygame.K_DOWN

                    if left:
                        changepixelsofx=-blocksize
                        changepixelsofy=nopixel
                    if right:
                        changepixelsofx=blocksize
                        changepixelsofy=nopixel
                    if up:
                        changepixelsofx=nopixel
                        changepixelsofy=-blocksize
                    if down:
                        changepixelsofx=nopixel
                        changepixelsofy=blocksize

                if leadx>=winwidth or leadx<0 or leady>=winheight or leady<0:
                    gameover=True

            leadx+=changepixelsofx
            leady+=changepixelsofy
            gamedisplay.fill(white)

            applethickness=20

            print([int(randomapplex),int(randomappley),applethickness,applethickness])
            pygame.draw.rect(gamedisplay,red,[randomapplex,randomappley,applethickness,applethickness])

            allspriteslist = []

            allspriteslist.append(leadx)
            allspriteslist.append(leady)
            snakelist.append(allspriteslist)

            if len(snakelist) > snakeLength:
                del snakelist[0]

            for eachSegment in snakelist [:-1]:
                if eachSegment == allspriteslist:
                    gameover = True

            snake(blockSize, snakelist)
            pygame.display.update()
        if leadx >= randomapplex and leadx <= randomapplex + applethickness:
            if leady >= randomappley and leady <= randomappley + applethickness:
                randomapplex = round(random.randrange(0, winwidth-blocksize)/10.0)*10.0
                randomAppleY = round(random.randrange(0, winheight-blocksize)/10.0)*10.0
                snakelength += 1

        clock.tick(fps)
    pygame.quit()
    quit()

gameloop()

