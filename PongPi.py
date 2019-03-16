import pygame
import random
import time

pygame.init()

display_width = 1200
display_height = 600

black = (0,0,0)
white = (255,255,255)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('PongPi')
clock = pygame.time.Clock()

#ballImg = pygame.image.load('ball.jpg')
#paddleImg = pygame.image.load('paddle.png')

def game_loop():
    
    #TODO
    #Make the boxes invulnerable to ball bouncing back

    speeds = [-4, -3, -2.5, 2.5, 3, 4]
    
    def ball(x,y):
        rectBall = pygame.draw.rect(gameDisplay, white, (x,y,25,25))
    
    def pad1(x,y):
        rectPad1 = pygame.draw.rect(gameDisplay, white, (xp1,yp1,25,100))
        
    def pad2(x,y):
        rectPad2 = pygame.draw.rect(gameDisplay, white, (xp2,yp2,25,100))

    def centreLine():
        rectLine1 = pygame.draw.line(gameDisplay, white, (600, 0), (600, 50), 5)
        rectLine2 = pygame.draw.line(gameDisplay, white, (600, 100), (600, 150), 5)
        rectLine3 = pygame.draw.line(gameDisplay, white, (600, 200), (600, 250), 5)
        rectLine4 = pygame.draw.line(gameDisplay, white, (600, 300), (600, 350), 5)
        rectLine5 = pygame.draw.line(gameDisplay, white, (600, 400), (600, 450), 5)
        rectLine6 = pygame.draw.line(gameDisplay, white, (600, 500), (600, 550), 5)

    x = ((display_width/2)-25/2)
    y = ((display_height/2)-25/2)

    xp1 = ((display_width * 0.15)-25/2)
    yp1 = ((display_height * 0.5)-100/2)

    xp2 = ((display_width * 0.85)-25/2)
    yp2 = ((display_height * 0.5)-100/2)
    
    xb_change = random.choice(speeds)
    yb_change = random.choice(speeds)
    #xb_change = 2
    #yb_change = 0
    yp1_change = 0
    yp2_change = 0
    
    sc1 = 0
    sc2 = 0
    
    def text_objects(text, font):
        textSurface = font.render(text, True, white)
        return textSurface, textSurface.get_rect()

    def message_display1(text1, text2):
        largeText = pygame.font.Font('freesansbold.ttf', 50)
        TextSurf1, TextRect1 = text_objects(text1, largeText)
        TextRect1.center = ((display_width/4),(display_height/4))
        TextSurf2, TextRect2 = text_objects(text2, largeText)
        TextRect2.center = ((display_width/4 * 3),(display_height/4))
        gameDisplay.blit(TextSurf1, TextRect1)
        gameDisplay.blit(TextSurf2, TextRect2)
        
        pygame.display.update()
        
        time.sleep(2)
        
        if int(text1) == 10 or int(text2) == 10:
            quit()
    
    def score(numb1, numb2):
        message_display1(str(numb1), str(numb2))
    
    gameExit = False
    paused = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    yp2_change = -5
                elif event.key == pygame.K_DOWN:
                    yp2_change = 5
                elif event.key == pygame.K_w:
                    yp1_change = -5
                elif event.key == pygame.K_s:
                    yp1_change = 5
                elif event.key == pygame.K_ESCAPE:
                    paused = True
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    yp2_change = 0
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    yp1_change = 0
        
        gameDisplay.fill(black)
        ball(x,y)
        pad1(xp1,yp1)
        pad2(xp2,yp2)
        centreLine()
        
        if y < 0:
            yb_change *= -1
        elif y > display_height - 25:
            yb_change *= -1
          
        if y + 25 >= yp1 and y <= yp1 + 100 and x <= xp1 + 25 and x >= xp1:
            xb_change *= -1.1
            yb_change *= 1.1
        
        if y + 25 >= yp2 and y <= yp2 + 100 and x + 25 <= xp2 + 25 and x + 25 >= xp2:
            xb_change *= -1.1
            yb_change *= 1.1
        
        x += xb_change
        y += yb_change
        
        if x < 0:
            x = (display_width * 0.5)
            y = (display_height * 0.5)
            xb_change = (random.choice(speeds))
            yb_change = (random.choice(speeds))
            sc2 += 1
            score(sc1, sc2)
        if x > display_width:
            x = (display_width * 0.5)
            y = (display_height * 0.5)
            xb_change = (random.choice(speeds))
            yb_change = (random.choice(speeds))
            sc1 += 1
            score(sc1, sc2)
        
        if yp1 < 0:
            yp1 += 1
        elif yp1 > display_height - 100:
            yp1 -= 1
        else:
            yp1 += yp1_change
            
        if yp2 < 0:
            yp2 += 1
        elif yp2 > display_height - 100:
            yp2 -= 1
        else:
            yp2 += yp2_change
        
        pygame.display.flip()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
