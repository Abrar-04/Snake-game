import turtle
import time
import random

delay=0.1

#score
score=0
high_score=0


wn=turtle.Screen()
wn.title("Snake Game --ABRAR")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)


#snake heaad
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0,0)
head.direction="stop"

#food
food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)


segments=[]

#pen
pen=turtle.Turtle()
pen.speed(0)
pen.shape("circle")
pen.color("blue")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0  HighScore: 0", align="center",font=("arial",21,"normal"))


def go_up():
    if head.direction !="down":
        head.direction="up"
def go_down():
    if head.direction !="up":
        head.direction="down"
def go_left():
    if head.direction !="right":
        head.direction="left"

def go_right():
    if head.direction !="left":
        head.direction="right"


def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)

wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_left,"a")
wn.onkeypress(go_right,"d")



#main game loop
while True:
    wn.update()


    #collision with border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"
        
        #hide those segments at new game
        for segment in segments:
            segment.goto(1000,1000)

        #clear segments
        segments.clear()

        #reset delay
        score=0.1

        #reset score
        score=0
        pen.clear() 
        pen.write("Score: {}  HighScore: {}".format(score,high_score),align="center",font=("arial",21,"normal")) 

    
    #check for collision wid food
    if head.distance(food)<20:
       #change food location
       x=random.randint(-290,290)
       y=random.randint(-290,290)
       food.goto(x,y)
       
    
       #create a new segment
       new_segment=turtle.Turtle()
       new_segment.speed(0)
       new_segment.shape("circle")
       new_segment.color("grey")
       new_segment.penup()
       segments.append(new_segment)

       #shorten the delay
       delay=delay-0.001

       #increase score
       score=score+1

       if score>high_score:
           high_score=score
       pen.clear() 
       pen.write("Score: {}  HighScore: {}".format(score,high_score),align="center",font=("arial",21,"normal")) 
 


    # move the end segments first in reverse
    for index in range(len(segments)-1,0,-1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)

    #move zeroth segment wid head
    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)

    move()

    #check for chead collisions wid segments
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"

            #hide the segments
            for segment in segments:
                segment.goto(1000,1000)

            #clear segments
            segments.clear()

            #reset the delay
            delay=0.1
            
            #reset score
            score=0
            pen.clear() 
            pen.write("Score: {}  HighScore: {}".format(score,high_score),align="center",font=("arial",21,"normal"))     

   
    time.sleep(delay)

wn.mainloop()