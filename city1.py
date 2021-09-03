import turtle
import random
import colorsys
import time
from math import *
from random import randint
screen = turtle.Screen()
screen.setup(1435,1000)
screen.setworldcoordinates(-1000,-1000,1000,1000)
screen.title("Project 2 : City skyline")
screen.bgcolor("navy")
colors = ["yellow"]
colors1 = ["aqua","turquoise","springgreen","lime"]
colors2 = ["pink","aquamarine","lightgreen","darkturquoise"]
    
#1st line of building :
line = turtle.Turtle()
line.pensize(3)
line.hideturtle()
line.speed(0)
line.shape("triangle")
line.color("dark cyan")
line.up()
line.goto(-1000,400)
line.down()
line.forward(200)
line.right(90)
line.forward(1450)
line.backward(800)
line.left(90)
line.forward(200)
line.right(90)
line.forward(800)
line.backward(400)
line.left(90)
line.forward(400)
line.right(90)
line.forward(500)
line.backward(300)
line.left(180)
line.forward(1000)
line.right(90)
line.forward(300)
line.right(90)
line.forward(1400)
line.backward(1150)
line.left(90)
line.forward(400)
line.right(90)
line.forward(1000)
line.backward(650)
line.left(90)
line.forward(200)
line.right(90)
line.forward(600)
line.backward(400)
line.left(180)
line.forward(1200)
line.right(90)
line.forward(400)
line.up()

#2nd line of building :
line.goto(-800,400)
line.down()
line.left(45)
line.forward(200)
line.left(225)
line.forward(780)
line.backward(600)
line.left(90)
line.forward(250)
line.right(90)
line.forward(1020)
line.up()
line.goto(-1000,550)
line.down()
line.left(90)
line.forward(340)
line.up()
line.goto(-50,400)
line.down()
line.right(90)
line.forward(250)
line.backward(100)
line.left(180)
line.forward(350)
line.left(90)
line.forward(400)
line.left(90)
line.forward(247)
line.up()
line.goto(503,-99)
line.down()
line.left(130)
line.forward(255)
line.left(142)
line.forward(400)
line.left(35)
line.forward(249)

square = turtle.Turtle()
square.shape('square')
square.pensize(2)
square.color(random.choice(colors))
square.speed('fastest')
square.up()

for i in range(10):
    y = 35*(i**2)
    for j in range(6):
        x =35*(j**2)
        square.goto(-x,-y-250)
        square.stamp()
        square.goto(-x,-y-250)
        square.stamp()
##
square1 = turtle.Turtle()
square1.shape('square')
square1.pensize(2)
square1.color(random.choice(colors1))
square1.speed('fastest')
square1.up()

for i in range(1,9):
    y = 25*(i**2)
    for j in range(4):
        x = 20*(j*3)
        square1.goto(x+750,-y+350)
        square1.stamp()
        square1.goto(x+750,-y+350)
        square1.stamp()
##
##
square2 = turtle.Turtle()
square2.shape('square')
square2.color(random.choice(colors1))
square2.speed('fastest')
square2.up()
##square2.left(35)

for i in range(1,10):
    y = 25*(i**2)
    for j in range(1):
        x = 25*(j*3)
        square2.goto(-x-950,-y+350)
        square2.stamp()
        square2.goto(-x-950,-y+350)
        square2.stamp()

##
dimond_turtle = turtle.Turtle() 
  
# the coordinates 
# of each corner
#B,D,A,C
##shape =((20, 35), (35, 35), (20, 20), (35, 20)) 
##shape =((95, 90), (105, 75), (95,75), (85, 90))
shape =((95, 120), (106, 90), (96,90), (85, 120))
# registering the new shape 
turtle.register_shape('diamond', shape) 
  
# changing the shape to 'diamond' 
dimond_turtle.shape('diamond')
dimond_turtle.speed(0)
##dimond_turtle.goto(-890,600)
dimond_turtle.color("magenta")
dimond_turtle.up()
for i in range(1,6):
    y = 20*(i**2)
    for j in range(2):
        x = 20*(j*3)
        dimond_turtle.goto(-x-850,-y+650)
        dimond_turtle.stamp()
        dimond_turtle.goto(-x-850,-y+650)
        dimond_turtle.stamp()

dimond_turtle1 = turtle.Turtle()
shape1 =((95, 120), (106, 90), (96,90), (85, 120))
turtle.register_shape('diamond', shape) 
dimond_turtle1.shape('diamond')
dimond_turtle1.speed(0)
dimond_turtle1.color("cyan")
dimond_turtle1.up()
for i in range(1,4):
    y = 20*(i**2)
    for j in range(2):
        x = 20*(j*4)
        dimond_turtle1.goto(-x+480,-y+150)
        dimond_turtle1.stamp()
        dimond_turtle1.goto(-x+480,-y+150)
        dimond_turtle1.stamp()
##
square3 = turtle.Turtle()
square3.shape('square')
##square2.pensize(2)
square3.color(random.choice(colors2))
square3.speed('fastest')
square3.up()
for i in range(1,6):
    y = 30*(i**2)
    for j in range(5):
        x = 30*(j*2)
        square3.goto(-x+406,-y-140)
        square3.stamp()
        square3.goto(-x+406,-y-140)
        square3.stamp()
####
square4 = turtle.Turtle()
square4.shape('square')
square4.color("deeppink")
square4.speed('fastest')
square4.up()
for i in range(6):
    y = 30*(i**2)
    for j in range(3):
        x = 20*(j*3)
        square4.goto(-x-650,-y-450)
        square4.stamp()
        square4.goto(-x-650,-y-450)
        square4.stamp()
##
square5 = turtle.Turtle()
square5.shape('square')
square5.left(90)
square5.color("deepskyblue")
square5.speed('fastest')
square5.up()
for i in range(3):
    y = 50*(i**2)
    for j in range(3):
        x = 20*(j*3)
        square5.goto(-x-250,-y+250)
        square5.stamp()
        square5.goto(-x-250,-y+250)
        square5.stamp()
####
square6 = turtle.Turtle()
square6.shape('square')
square6.color("chartreuse")
square6.speed('fastest')
square6.up()
for i in range(6):
    y = 30*(i**2)
    for j in range(3):
        x = 20*(j*3)
        square6.goto(-x+650,-y-650)
        square6.stamp()
        square6.goto(-x+650,-y-650)
        square6.stamp()
####
square7 = turtle.Turtle()
square7.shape('square')
square7.left(90)
square7.color("hotpink")
square7.speed('fastest')
square7.up()
for i in range(3):
    y = 50*(i**2)
    for j in range(3):
        x = 20*(j*3)
        square7.goto(-x-450,-y+250)
        square7.stamp()
        square7.goto(-x-450,-y+250)
        square7.stamp()
######
moon = turtle.Turtle()
moon.hideturtle()
moon.speed(0)
def draw_moon(pos,color): # position and color of the moon
    x,y = pos
    moon.color(color)
    moon.begin_fill()
    moon.penup()
    moon.goto(x,y)
    moon.pendown()
    moon.circle(90)
    moon.end_fill()

draw_moon((410,576),"gold")
draw_moon((350,583),"navy")
#######
star = turtle.Turtle()
star.hideturtle()
star.speed(0)
def draw_star(pos,color,length): # position, color and length(size) of star
    x,y = pos
    star.color(color)
    star.penup()
    star.goto(x,y)
    star.pendown()
    star.begin_fill()
    for i in range(5):
        star.forward(length)
        star.right(144)
        star.forward(length)
##        star.forward(length)
##        star.left(90)
    star.end_fill()

draw_star((100,600),"gold",10)
def random_pos():
    return (random.randint(-800,900),random.randint(800,1000))
def random_length():
    return random.randint(5,25)

for i in range(30):
    color = "gold"
    pos = random_pos()
    length = random_length()
    draw_star(pos,color,length)
#######
##while True:
##    dot.shape("square")
##    time.sleep(0.5)
##    dot.shape("circle")
##    dot.color("red")
##    time.sleep(0.5)
##
##screen.mainloop()
######
##firefly = turtle.Turtle() # turtle for drawing the lighting dot
##firefly.hideturtle()
##firefly.up()
##
### Constants
##H_YELLOWGREEN = 0.22 # constant: hue value of yellow green color.
##V_DARK = 0.1 # constant: brightness value of initial dark state
##V_BRIGHT = 1 # constant: brightness value of the brightest state
##FPS = 30 # constant: refresh about 30 times per second
##TIMER_VALUE = 1000//FPS # the timer value in milliseconds for timer events
##CYCLE = 5 # costant: 5 second cycle for firefly to light up
##LIGHTUP_TIME = 1 # constant: 1 second light up and dim
##
### Variables
##v = V_DARK # initial brightness state
##t = 0 # current time
##should_draw = True # this variable is used to decide if drawing is necessary to save CPU time
##
##def update_brightness():
##    global t,v,should_draw
##    t += TIMER_VALUE/1000 # every time this function is called, time increases by this value
##    lastv = v # lastv is v before potential change
##    if t > CYCLE:
##        t -= CYCLE # make sure time stays within CYCLE
##    if t < CYCLE-LIGHTUP_TIME:
##        v = V_DARK # dormant period
##    elif t < CYCLE-LIGHTUP_TIME/2: # gradually (linearly) lighting up period
##        v = V_DARK + (V_BRIGHT-V_DARK)*(t-(CYCLE-LIGHTUP_TIME))/(LIGHTUP_TIME/2)
##    else: # gradually (linearly) dimming period
##        v = V_BRIGHT - (V_BRIGHT-V_DARK)*(t-(CYCLE-LIGHTUP_TIME/2))/(LIGHTUP_TIME/2)
##
##    if v != lastv:
##        should_draw = True # v has changed, so set should_draw to True
###    print(t,v)
##    screen.ontimer(update_brightness,TIMER_VALUE)
##
##def draw():
##    global v,firefly,should_draw
##    if should_draw == False: # There is no change. Don't draw and return immediately
##        return
##    firefly.clear() # clear the current drawing
##    color = colorsys.hsv_to_rgb(H_YELLOWGREEN,1,v) # use colorsys to convert HSV to RGB color
##    firefly.color(color)
##    firefly.dot(400)
##    should_draw = False # just finished drawing, set should_draw to False
##    
##screen.ontimer(update_brightness,TIMER_VALUE)
##while True:
##    draw() # draw forever
##    screen.update()
##import sys, pygame
##pygame.init()
##
##size = width, height = 320, 240
##speed = [2, 2]
##black = 0, 0, 0
##
##screen = pygame.display.set_mode(size)
##
##ball = pygame.image.load("intro_ball.gif")
##ballrect = ball.get_rect()
##
##while 1:
##    for event in pygame.event.get():
##        if event.type == pygame.QUIT: sys.exit()
##
##    ballrect = ballrect.move(speed)
##    if ballrect.left < 0 or ballrect.right > width:
##        speed[0] = -speed[0]
##    if ballrect.top < 0 or ballrect.bottom > height:
##        speed[1] = -speed[1]
##
##    screen.fill(black)
##    screen.blit(ball, ballrect)
##    pygame.display.flip()
