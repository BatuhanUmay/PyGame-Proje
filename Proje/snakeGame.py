import pygame
import time
import random
import sqlite3

db = sqlite3.connect("snake.db")

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Slither")

icon = pygame.image.load("slither.jpg")
pygame.display.set_icon(icon)

img = pygame.image.load("snakeHead.png")
appleimg = pygame.image.load("apple.png")
doubleimg = pygame.image.load("double.png")
poisonimg = pygame.image.load("poison.png")
accelerateimg = pygame.image.load("accelerate.png")
slowimg = pygame.image.load("slow.png")

clock = pygame.time.Clock()
# FPS = 15
block_size = 20
AppleThickness = 30
doubleThickness = 30
poisonThickness = 30
AccelerateThickness = 30
SlowThickness = 30

direction = "right"

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)


def pause():
    paused = True
    
    message_to_screen("Duraklatıldı"
                        ,black, -100, size = "medium")
    message_to_screen("Oyuna devam etmek için C, Çıkmak için Q tuşuna basınız",
                        black, 25)
    pygame.display.update()

    
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False  
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                    
        gameDisplay.fill(white)
        clock.tick(5)
            

def score(score):
    text = smallfont.render("Puan : " + str(score), True, black)    
    gameDisplay.blit(text, [0,0])
    

def randAppleGen():
    randAppleX = round(random.randint(0, display_width - AppleThickness))
    randAppleY = round(random.randint(0, display_height - AppleThickness))

    return randAppleX, randAppleY


def randDoubleGen():
    randDoubleX = round(random.randint(0, display_width - doubleThickness))
    randDoubleY = round(random.randint(0, display_height - doubleThickness))

    return randDoubleX, randDoubleY


def randPoisonGen():
    randPoisonX = round(random.randint(0, display_width - poisonThickness))
    randPoisonY = round(random.randint(0, display_height - poisonThickness))

    return randPoisonX, randPoisonY


def randAccelerateGen():
    randAccelerateX = round(random.randint(0, display_width - AccelerateThickness))
    randAccelerateY = round(random.randint(0, display_height - AccelerateThickness))

    return randAccelerateX, randAccelerateY


def randSlowGen():
    randSlowX = round(random.randint(0, display_width - SlowThickness))
    randSlowY = round(random.randint(0, display_height - SlowThickness))

    return randSlowX, randSlowY


def game_intro():
    intro = True

    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        gameDisplay.fill(white)
        message_to_screen("Yılan Oyununa Hoşgeldiniz",
                            green,
                            -100,
                            "medium")
        message_to_screen("Ana amaç kırmızı elmaları yiyerek büyümektir",
                            black,
                            -30,)
        message_to_screen("Her kırmızı elmayı yediğinizde bir skor alırsınız",
                            black,
                            10,)
        message_to_screen("Oyun alanının dışına çıkarsanız elenirsiniz!",
                            black,
                            50,)
        message_to_screen("Oyuna devam etmek için C, Çıkmak için Q tuşuna basınız",
                            black,
                            180,)
                       
        pygame.display.update()
        clock.tick(15)


def snake(block_size, snakelist):

    if direction == "right":
        head = pygame.transform.rotate(img, 270)
    if direction == "left":
        head = pygame.transform.rotate(img, 90)
    if direction == "up":
        head = img
    if direction == "down":
        head = pygame.transform.rotate(img, 180)

    gameDisplay.blit(head, (snakelist[-1][0], snakelist[-1][1]))

    for XnY in snakelist[:-1]:
        pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1], block_size, block_size])


def text_objects(text, color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)
  
    return textSurface, textSurface.get_rect()


def message_to_screen(msg, color, y_displace = 0, size = "small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (display_width/2),(display_height/2) + y_displace
    gameDisplay.blit(textSurf,textRect)


def gameLoop():
    global direction
    global FPS 
    FPS = 15

    direction = "right"

    gameExit = False
    gameOver = False

    lead_x = display_width / 2
    lead_y = display_height / 2

    lead_x_change = 10
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    randAppleX, randAppleY = randAppleGen()
    randDoubleX, randDoubleY = randDoubleGen()
    randPoisonX, randPoisonY = randPoisonGen()
    randAccelerateX, randAccelerateY = randAccelerateGen()
    randSlowX, randSlowY = randSlowGen()


    while not gameExit:
        if gameOver == True:
            message_to_screen("Oyun Bitti", 
                                red, y_displace = -50, 
                                size = "large")
            message_to_screen("Oyuna devam etmek için C, Çıkmak için Q tuşuna basınız", 
                                black, y_displace = 50, 
                                size = "small")
            pygame.display.update()

        while gameOver == True:
            # gameDisplay.fill(white)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    direction = "up"
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    lead_y_change = block_size
                    lead_x_change = 0
                elif event.key == pygame.K_p:
                    pause()

        if lead_x > display_width or lead_x < 0 or lead_y > display_height or lead_y < 0:
            gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change 

        gameDisplay.fill(white)

        gameDisplay.blit(appleimg, (randAppleX, randAppleY))
        gameDisplay.blit(doubleimg, (randDoubleX, randDoubleY))
        gameDisplay.blit(poisonimg, (randPoisonX, randPoisonY))
        gameDisplay.blit(accelerateimg, (randAccelerateX, randAccelerateY))
        gameDisplay.blit(slowimg, (randSlowX, randSlowY))


        snakeHead = []

        snakeHead.append(lead_x) 
        snakeHead.append(lead_y)

        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

        snake(block_size, snakeList)
        
        score(snakeLength-1)
        
        pygame.display.update()        

        if lead_x > randAppleX and lead_x < randAppleX + AppleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + AppleThickness:
            if lead_y > randAppleY and lead_y < randAppleY + AppleThickness:
                randAppleX, randAppleY = randAppleGen()
                snakeLength += 1
            elif lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness:
                randAppleX, randAppleY = randAppleGen()
                snakeLength += 1
        

        if lead_x > randDoubleX and lead_x < randDoubleX + doubleThickness or lead_x + block_size > randDoubleX and lead_x + block_size < randDoubleX + doubleThickness:
            if lead_y > randDoubleY and lead_y < randDoubleY + doubleThickness:
                randDoubleX, randDoubleY = randDoubleGen()
                snakeLength = 2 * snakeLength - 1
            elif lead_y + block_size > randDoubleY and lead_y + block_size < randDoubleY + doubleThickness:
                randDoubleX, randDoubleY = randDoubleGen()
                snakeLength = 2 * snakeLength - 1
        
        
        if lead_x > randPoisonX and lead_x < randPoisonX + poisonThickness or lead_x + block_size > randPoisonX and lead_x + block_size < randPoisonX + poisonThickness:
            if lead_y > randPoisonY and lead_y < randPoisonY + poisonThickness:
                randPoisonX, randPoisonY = randPoisonGen()
                snakeLength -= 1
                
            elif lead_y + block_size > randPoisonY and lead_y + block_size < randPoisonY + poisonThickness:
                randPoisonX, randPoisonY = randPoisonGen()
                snakeLength -= 1


        if lead_x > randAccelerateX and lead_x < randAccelerateX + AccelerateThickness or lead_x + block_size > randAccelerateX and lead_x + block_size < randAccelerateX + AccelerateThickness:
            if lead_y > randAccelerateY and lead_y < randAccelerateY + AccelerateThickness:
                randAccelerateX, randAccelerateY = randAccelerateGen()
                FPS += random.randint(1,5)
                                
            elif lead_y + block_size > randAccelerateY and lead_y + block_size < randAccelerateY + AccelerateThickness:
                randAccelerateX, randAccelerateY = randAccelerateGen()
                FPS += random.randint(1,5)
                
                
        if lead_x > randSlowX and lead_x < randSlowX + SlowThickness or lead_x + block_size > randSlowX and lead_x + block_size < randSlowX + SlowThickness:
            if lead_y > randSlowY and lead_y < randSlowY + SlowThickness:
                randSlowX, randSlowY = randSlowGen()
                FPS -= random.randint(1,5)
                     
            elif lead_y + block_size > randSlowY and lead_y + block_size < randSlowY + SlowThickness:
                randSlowX, randSlowY = randSlowGen()
                FPS -= random.randint(1,5)

        clock.tick(FPS)


    name = "Oyuncu" + str(random.randint(1,10))
    db.execute(""" INSERT INTO puan(name, score, velocityFps) VALUES(?,?,?)""",(name,snakeLength-1,FPS))
    db.commit()

    pygame.quit()
    quit()

game_intro()
gameLoop()