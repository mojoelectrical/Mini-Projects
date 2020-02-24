#!/usr/bin/env python
# coding: utf-8

# In[3]:


import random
import math
import turtle

window=turtle.Screen()
window.bgcolor('black')
window.setup(750,750)
window.title('Maze')
window.tracer(0)

wall1=[]
treasure_chest=[]
enemies=[]
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('square')
        self.color('white')
        self.penup()
        self.speed(0)
        
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('circle')
        self.color('yellow')
        self.penup()
        self.speed(0)
        self.gold=0
        
    def go_up(self):
        
        if (self.xcor(), self.ycor() + 24) not in wall1:
            self.goto(self.xcor(), self.ycor() + 24)
            
    def go_down(self):
        if (self.xcor(),self.ycor() -24) not in wall1:
            self.goto(self.xcor(), self.ycor() - 24)
    def go_right(self):
        if (self.xcor() + 24, self.ycor()) not in wall1:
            self.goto(self.xcor() + 24, self.ycor())
    def go_left(self):
        if (self.xcor() - 24, self.ycor()) not in wall1:
            self.goto(self.xcor() - 24, self.ycor())
            
    def if_collision(self, other):
        a=self.xcor() - other.xcor()
        b=self.ycor() - other.ycor()
        dist= math.sqrt((a**2) + (b**2))
        
        if dist < 5:
            return True
        else:
            return False

class Treasure(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.color('gold')
        self.penup()
        self.gold=200
        self.speed(0)
        self.shape('triangle')
        self.goto(x,y)
    
    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()

class Enemy(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.color('red')
        self.penup()
        self.gold=200
        self.speed(0)
        self.shape('square')
        self.goto(x,y)
        self.direction=random.choice(["up","down","right","left"])
        
    def move(self):
        x=wall1
        if self.direction == "up":
            dx=0
            dy=24
        elif self.direction == "down":
            dx=0
            dy=-24
        elif self.direction == "right":
            dx=24
            dy=0
        elif self.direction == "left":
            dx=-24
            dy=0
        else:
            dx=0
            dy=0
        
        moveto_x=self.xcor() + dx
        moveto_y=self.ycor() + dy
        
        if (self.xcor() + dx,self.ycor() + dy) not in x:
            self.goto(self.xcor() + dx,self.ycor() + dy)
        else:
            self.direction=random.choice(["up","down","right","left"])
        
        turtle.ontimer(self.move, t=random.randint(100,300))
    

levels=[""]
level_1=["#########################",
         "#P    #######E         ##",
         "##   #######      #### ##",
         "##   ########E    #### ##",
         "##   #######      #### ##",
         "#               ###### ##",
         "#            ####E      #",
         "########      ####      #",
         "#####       ######T    ##",
         "####     ####   ####    #",
         "##      #####   ####    #",
         "##      E###E  ####    ##",
         "###     T###   ####     #",
         "##   #######         ####",
         "##   ########     #######",
         "##   #######E     #######",
         "#                  ######",
         "# E          ####       #",
         "########      ####      #",
         "#####       ### E      ##",
         "####    T####   ####    #",
         "##      #####   ####    #",
         "##      E###    ###T   ##",
         "###      ###   ####     #",
         "#########################"]

levels.append(level_1)

def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character=level[y][x]
            screen_x=-288 + (x*24)
            screen_y=288- (y*24)
            
            if character == '#':
                pen.goto(screen_x,screen_y)
                pen.stamp() 
                wall1.append((screen_x,screen_y))
             
            if character == 'P':
                player.goto(screen_x,screen_y)
                
            if character == 'T':
                treasure_chest.append(Treasure(screen_x,screen_y))
            
            if character == 'E':
                enemies.append(Enemy(screen_x,screen_y))
    
            
pen=Pen()
player=Player()
turtle.listen()
turtle.onkey(player.go_up,"Up")
turtle.onkey(player.go_down,"Down")
turtle.onkey(player.go_left,"Left")
turtle.onkey(player.go_right,"Right")

setup_maze(levels[1])

for enemy in enemies:
        turtle.ontimer(enemy.move, t=1000)

while True:
    for treasure in treasure_chest:
        if player.if_collision(treasure):
            print("Player added 200 Gold")
            treasure.destroy()
            treasure_chest.remove(treasure)
    
    for enemy in enemies:
        if player.if_collision(enemy):
            print('Player loses')
            
    window.update()
                        
turtle.done()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




