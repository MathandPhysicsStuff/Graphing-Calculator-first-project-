"Graphing Calculator"

import pygame, sys, math
from math import *

pygame.init()
clock = pygame.time.Clock()

screenW = 700
extraW = 400
screenH = 500

screen = pygame.display.set_mode((screenW+extraW, screenH))
pygame.display.set_caption("Graphing Calculator")


font1 = pygame.font.SysFont("verdana",16)
font2 = pygame.font.SysFont("serif", 24)
background = (30, 30, 30)
black = (0, 0, 0)
gridcolor = (200, 200, 200)
titlecolor = (200, 0, 150)


def grid(k):
    screen.set_clip(0,0,screenW,screenH)
    screen.fill(background)
    
    for i in range(int(screenW/k)):
        gridx = i*k
        gridy = i*k
        pygame.draw.line(screen, gridcolor, (gridx, 0), (gridx, screenH), 1)
        pygame.draw.line(screen, gridcolor, (0, gridy), (screenW, gridy), 1)

    pygame.draw.line(screen, gridcolor, (screenW, 0), (screenW, screenH), 5)
    #x and y axis lines
    pygame.draw.line(screen, gridcolor, (screenW/2, 0), (screenW/2, screenH), 5)
    pygame.draw.line(screen, gridcolor, (0, screenH/2), (screenW, screenH/2), 5)
    
    screen.set_clip(None)

def mainfunc():

    k = 25

    grid(k)

    title = font2.render("Graphing Calculator", 1, titlecolor)
    screen.blit(title, (screenW + 10, 20))

    instruct = font1.render("Press 'Enter' to graph equation.", 1, titlecolor)
    screen.blit(instruct, (screenW + 20, 70))

    instruct = font1.render("Press 'backspace' to undo.", 1, titlecolor)
    screen.blit(instruct, (screenW + 20, 100))

    instruct = font1.render("Press 'Ctrl' to refresh.", 1, titlecolor)
    screen.blit(instruct, (screenW + 20, 130))


    equation = []
    done = False

    active = True

    while active:
        
        
        screen.set_clip(screenW + 10, screenH - 30, screenW + extraW, screenH)
        screen.fill(black)

        eq = ""
        eq = eq.join(equation)

        showeq = font1.render("y = "+eq, 1, titlecolor)
        screen.blit(showeq, (screenW + 10, screenH - 30))

        pygame.display.update()
        clock.tick(60)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False
                done = True

            elif event.type == pygame.KEYDOWN:

                if event.unicode == u'*':
                    equation.append("*")
                elif event.unicode == u'^':
                    equation.append("**")
                elif event.unicode == u'+':
                    equation.append("+")
                elif event.unicode == u'-':
                    equation.append("-")
                elif event.unicode == u'/':
                    equation.append("/")
                elif event.unicode == u'(':
                    equation.append("(")
                elif event.unicode == u')':
                    equation.append(")")


                elif event.key == pygame.K_i:
                    k = 10
                    grid(k)
                elif event.key == pygame.K_o:
                    k = 25
                    grid(k)
                elif event.key == pygame.K_p:
                    k = 50
                    grid(k) 

                elif event.key == pygame.K_1:
                    equation.append("1")
                elif event.key == pygame.K_2:
                    equation.append("2")
                elif event.key == pygame.K_3:
                    equation.append("3")
                elif event.key == pygame.K_4:
                    equation.append("4")
                elif event.key == pygame.K_5:
                    equation.append("5")
                elif event.key == pygame.K_6:
                    equation.append("6")
                elif event.key == pygame.K_7:
                    equation.append("7")
                elif event.key == pygame.K_8:
                    equation.append("8")
                elif event.key == pygame.K_9:
                    equation.append("9")
                elif event.key == pygame.K_0:
                    equation.append("0")

                elif event.key == pygame.K_x:
                    equation.append("x")

                elif event.key == pygame.K_s:
                    equation.append("sin(")
                elif event.key == pygame.K_c:
                    equation.append("cos(")
                elif event.key == pygame.K_t:
                    equation.append("tan(")
                elif event.key == pygame.K_q:
                    equation.append("sqrt(")
                elif event.key == pygame.K_a:
                    equation.append("fabs(")
                elif event.key == pygame.K_e:
                    equation.append("e")
                elif event.key == pygame.K_p:
                    equation.append("pi")


                elif event.key == pygame.K_RETURN:
                    active = False
                elif event.key == pygame.K_BACKSPACE:
                    equation = equation[:-1]


    if done:
        pygame.quit()
        sys.exit()
                    
    else:
        screen.set_clip(screenW,0,screenW+extraW,screenH-30)
        screen.fill(black)
        screen.set_clip(None)

        GraphEq(eq,k)



def GraphEq(eq,k):


    for i in range(screenW):
        try:
            x = (screenW/2 - i)/float(k)
            y = eval(eq)
            pos1 = (screenW/2+x*k, screenH/2-y*k)

            nx = x = (screenW/2 - (i + 1))/float(k)
            ny = eval(eq)
            pos2 = (screenW/2+nx*k, screenH/2-ny*k)
            
            pygame.draw.line(screen, titlecolor, pos1, pos2, 3)
        except:
            pass

    screen.set_clip(screenW,0,screenW+extraW,screenH-30)
    

    title = font2.render("Graphing Calculator", 1, titlecolor)
    screen.blit(title, (screenW + 10, 20))

    instruct = font1.render("Press 'Enter' to graph equation.", 1, titlecolor)
    screen.blit(instruct, (screenW + 20, 70))

    instruct = font1.render("Press 'backspace' to undo.", 1, titlecolor)
    screen.blit(instruct, (screenW + 20, 100))

    instruct = font1.render("Press 'Ctrl' to refresh.", 1, titlecolor)
    screen.blit(instruct, (screenW + 20, 130))

    x = 0
    try:
        yint = eval(eq)
        yint = round(yint,2)
    except:
        yint = "dne"

    instruct = font1.render("y-intercept (0, "+str(yint)+")", 1, titlecolor)
    screen.blit(instruct, (screenW + 20, 180))

    xValue = []
    xVal = "?"
    yVal = "?"

    screen.set_clip(None)

    active = True

    while active:
        screen.set_clip(screenW,150,screenW+extraW,180)
        screen.fill(black)
        xDisplay = ""
        xDisplay = xDisplay.join(xValue)
        plotx = font1.render("x = "+str(xDisplay),1,(0,0,200))
        screen.blit(plotx, (screenW+10, 150))
        ploty = font1.render(("("+str(xVal)+","+str(yVal)+")"),1,(0,0,200))
        screen.blit(ploty, (screenW+210,150)) 

        screen.set_clip(None)


        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL:
                    mainfunc()
                elif event.key == pygame.K_RCTRL:
                    mainfunc()

                elif event.key == pygame.K_i:
                    k = 10
                    grid(k)
                    GraphEq(eq,k)
                elif event.key == pygame.K_o:
                    k = 25
                    grid(k)
                    GraphEq(eq,k)
                elif event.key == pygame.K_p:
                    k = 50
                    grid(k)
                    GraphEq(eq,k) 

                elif event.key == pygame.K_RETURN:
                    try:
                        x = xVal = float(xDisplay)
                        yVal = round(eval(eq), 2)

                        pygame.draw.circle(screen, (200,0,0), (screenW/2+x*k, screenH/2-yVal*k), 4)
                        xValue = []
                    except:
                        pass

                elif event.key == pygame.K_BACKSPACE:
                    xValue = xValue[:-1]

                elif event.key == pygame.K_1:
                    xValue.append("1")
                elif event.key == pygame.K_2:
                    xValue.append("2")
                elif event.key == pygame.K_3:
                    xValue.append("3")
                elif event.key == pygame.K_4:
                    xValue.append("4")
                elif event.key == pygame.K_5:
                    xValue.append("5")
                elif event.key == pygame.K_6:
                    xValue.append("6")
                elif event.key == pygame.K_7:
                    xValue.append("7")
                elif event.key == pygame.K_8:
                    xValue.append("8")
                elif event.key == pygame.K_9:
                    xValue.append("9")
                elif event.key == pygame.K_0:
                    xValue.append("0")

                elif event.unicode == u'.':
                    xValue.append(".")
                elif event.unicode == u'-':
                    xValue.append("-")






    pygame.quit()
    sys.exit()


if __name__=="__main__":
    mainfunc()
















