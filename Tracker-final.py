import random
import time
import math
import turtle
import sys
sys.setrecursionlimit(3000)


destarray=[]
tiles=[]
tracker=[]
small_distance=[]
#Creates Screen
window=turtle.Screen()
window.bgcolor('black')
window.setup(750,750)
window.title('Maze')
window.tracer(0)



class Grid(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color('green')
        self.shape('circle')
        self.penup()
        self.speed(0)

class Destination(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color('red')
        self.shape('square')
        self.penup()
        self.speed(0)

class Tracker(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.color('orange')
        self.shape('square')
        self.penup()
        self.speed(0)
        self.goto(x,y)
        self.counter=0

    def move(self):
        xright = destarray[0][0] - (self.xcor() + 24)
        yright = destarray[0][1] - self.ycor()
        d_right=math.sqrt((xright**2) + (yright**2))
        small_distance.append(d_right)

        xleft = destarray[0][0] - (self.xcor() - 24)
        yleft= destarray[0][1] - self.ycor()
        d_left=math.sqrt((xleft**2)+ (yleft**2))
        small_distance.append(d_left)

        xup= destarray[0][0] - (self.xcor())
        yup= destarray[0][1] - (self.ycor() + 24)
        d_up=math.sqrt((xup**2) + (yup**2))
        small_distance.append(d_up)

        xdown= destarray[0][0] - (self.xcor())
        ydown= destarray[0][1] - (self.ycor() - 24)
        d_down=math.sqrt((xdown**2)+ (ydown**2))
        small_distance.append(d_down)

        xne= destarray[0][0] - (self.xcor() + 24)
        yne= destarray[0][1] - (self.ycor() + 24)
        d_ne=math.sqrt((xne**2)+(yne**2))
        small_distance.append(d_ne)

        xnw= destarray[0][0] - (self.xcor() -24)
        ynw= destarray[0][1] - (self.ycor() + 24)
        d_nw=math.sqrt((xnw**2)+(ynw**2))
        small_distance.append(d_nw)

        xsw= destarray[0][0] - (self.xcor() -24)
        ysw= destarray[0][1] - (self.ycor() - 24)
        d_sw=math.sqrt((xsw**2)+(ysw**2))
        small_distance.append(d_sw)
        
        xse= destarray[0][0] - (self.xcor() + 24)
        yse= destarray[0][1] - (self.ycor() - 24)
        d_se=math.sqrt((xse**2)+(yse**2))
        small_distance.append(d_se)
        
        small_distance.sort()

        if small_distance[0] == d_right:
            dx=24
            dy=0
        elif small_distance[0] == d_left:
            dx=-24
            dy=0
        elif small_distance[0] == d_down:
            dy=-24
            dx=0
        elif small_distance[0] == d_up:
            dy=24
            dx=0
        elif small_distance[0] == d_nw:
            dx=-24
            dy=24
        elif small_distance[0] == d_ne:
            dx= 24
            dy= 24
        elif small_distance[0] == d_sw:
            dx=-24
            dy=-24
        elif small_distance[0] == d_se:
            dx= 24
            dy=-24
        else:
            dx=0
            dy=0
            print(self.counter)
            time.sleep(5000)
            
            
        
        self.goto(self.xcor() + dx ,self.ycor() + dy)
        self.counter += 1

        turtle.ontimer(self.move,t=700)
    


levels=[""]
level=[  "XXXXXXXXXXXXXXXXXXXXXXXXX",
         "XXXXXXXXXXXXXXXXXXXXXXXXX",
         "XXXXXXXXXXXXXXXXXXXXXXXXX",
         "XXXXXXXXXXXXXXXXXXXXXXXXX",
         "XXXXXXXXXXXXXXXXXXXXXXXXX",
         "XXXXXXXXXXXXXXXXXXXXXXXXX",
         "XXXXXXXXXXXXXXXXXXXXXXXXX",
         "XXXXXXXXXXXXXXXXXXXXXXXXX",
         "XXXXXXXXXXXXXXXXXXXXXXXXX",
         "XXXXXXXXXXXXXXXXXXXXXXXXX",
         "XXXXXXXXXXXXXXXXXXXXXXXXX",
         "XXXXXXXXXXXXXXXXXXXXXXXXX",
         "XXXXXXXXXXXXXXXXXXXXXXXXX",
         "XXXXXXXXXXXXXXXXXXXXXXXXX",
         "XXXXXXXXXXXXXXXXXXXXXXXXX",
         "XXXXXXXXXXXXXXXXXXXXXXXXX",
         "XXXXXXXXXXXXXXXXXXXXXXXXX",
         "XXXXXXXXXXXXXXXXXXXXXXXXX",
         "XXXXXXXXXXXXXXXXXXXXXXXXX",
         "XXXXXXXXXXXXXXXXXXXXXXXXX",
         "XXXXXXXXXXXXXXXXXXXXXXXXX",
         "XXXXXXXXXXXXXXXXXXXXXXXXX",
         "XXXXXXXXXXXXXXXXXXXXXXXXX",
         "XXXXXXXXXXXXXXXXXXXXXXXXX",
         "XXXXXXXXXXXXXXXXXXXXXXXXX"]

levels.append(level)

def setup_maze(level):

    print("Dimension of this maze is 25 x 25")
    ask1=int(input("Enter starting row from (0 to 24): "))
    ask2=int(input("Enter the starting column from (0 to 24): "))
    ask3=int(input("Enter the endpoint from (0 to 24): "))
    ask4=int(input("Enter the endpoint from (0 to 24): "))
    askx= -288 + (ask1*24)
    asky= 288 - (ask2*24)
    askendx= -288 + (ask3*24)
    askendy= 288 - (ask4*24)

    for y in range(len(level)):
        for x in range(len(level[y])):
            
            character=level[y][x]
            screen_x=-288 + (x*24)
            screen_y= 288 - (y*24)
            
            if character == 'X':
                Grid().goto(screen_x,screen_y)
                Grid().stamp()
                tiles.append((screen_x,screen_y))
            
            
            Destination().goto(askendx,askendy)
            destarray.append((askendx,askendy))

            tracker.append(Tracker(askx,asky))

turtle.listen()

setup_maze(levels[1])

for track in tracker:
    turtle.ontimer(track.move,t=1000)
while True:
    window.update()


turtle.done()