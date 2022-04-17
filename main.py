from turtle import *
import time
import random

#SCREEN
root=Screen()
root.title("Snake Game")
root.setup(width=600,height=600)
root.bgcolor('#66CD00')
root.bgpic("border.gif")
root.tracer(False)
root.addshape("upmouth.gif")
root.addshape("downmouth.gif")
root.addshape("leftmouth.gif")
root.addshape("rightmouth.gif")
root.addshape("food.gif")
root.addshape("body.gif")



#BASE_SNAKE
head=Turtle()
head.shape('upmouth.gif')
head.penup()
head.goto(0,0)
head.ditrction='stop'


#BASE_FOOD
food=Turtle()
food.shape('food.gif')
food.penup()
food.goto(0,100)



#SCORE BOARD
text=Turtle()
text.penup()
text.goto(0,268)
text.color("white")
text.write("SCORE :- 0",font=('courier',25,'bold'),align='center')
#FOOTER
text1=Turtle()
text1.penup()
text1.goto(0,-294)
text1.color("white")
text1.write("Devloped by @Rupam Chakraborty",font=('courier',15,'bold'),align='center')

lost=Turtle()
lost.color('black')
lost.penup()
lost.hideturtle()


#MOVE FUNCTION BASED ON THE CONDITION
def move_snake():
    if head.ditrction=='up':
        y=head.ycor()
        y=y+20
        head.sety(y)

    if head.ditrction=='down':
        y=head.ycor()
        y=y-20
        head.sety(y)


    if head.ditrction=='right':
        x=head.xcor()
        x=x+20
        head.setx(x)


    if head.ditrction=='left':
        x=head.xcor()
        x=x-20
        head.setx(x)


#RUN DIRECTIONS
def go_Up():
    if head.ditrction!='down':
        head.ditrction='up'
        head.shape("upmouth.gif")

def go_Down():
    if head.ditrction != 'up':
        head.ditrction='down'
        head.shape("downmouth.gif")

def go_Right():
    if head.ditrction != 'left':
        head.ditrction = 'right'
        head.shape("rightmouth.gif")

def go_Left():
    if head.ditrction != 'right':
         head.ditrction='left'
         head.shape("leftmouth.gif")



#TAKING INPUTS FROM KEYBOARD
root.listen()
root.onkeypress(go_Up,'Up')
root.onkeypress(go_Down,'Down')
root.onkeypress(go_Left,'Left')
root.onkeypress(go_Right,'Right')

seg=[]
score=0

while True:
    root.update()
    if head.xcor() > 260 or head.xcor()<-260 or head.ycor()>257 or head.ycor()<-257:
        lost.write("GAME LOST",align='center',font=('courier',40,'bold'))
        time.sleep(2)
        lost.clear()
        time.sleep(1)
        head.goto(0,0)
        head.direction='stop'

        for bodies in seg:
            bodies.goto(1000,1000)
        score=0
        seg.clear()
        text.clear()
        text.write("SCORE :- 0",font=('courier',25,'bold'),align='center')

    if head.distance(food)<20:
        x=random.randint(-255,255)
        y=random.randint(-255,255)
        food.goto(x,y)

        body=Turtle()
        body.penup()
        body.shape('body.gif')
        seg.append(body)

        score=score+10
        text.clear()
        text.write(f"SCORE :- {score}",font=('courier',25,'bold'),align='center')


    for i in range(len(seg)-1,0,-1):
            x=seg[i-1].xcor()
            y=seg[i-1].ycor()
            seg[i].goto(x,y)

    if len(seg)>0:
            x=head.xcor()
            y=head.ycor()
            seg[0].goto(x,y)

    move_snake()

    for bodies in seg:
        if bodies.distance(head)<20:
            head.goto(0,0)
            head.ditrction='stop'

            for bodies in seg:
                bodies.goto(1000,1000)
            seg.clear()
            score=0
            lost.write("GAME LOST", align='center', font=('courier', 40, 'bold'))
            time.sleep(2)
            lost.clear()
            text.clear()
            text.write("SCORE :- 0",font=('courier',25,'bold'),align='center')


    time.sleep(0.1)
