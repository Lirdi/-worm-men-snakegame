import turtle
import time
import random

delay = 0.1
#Setting up the screen

wn = turtle.Screen()
wn.title("Worm men")
wn.bgpic("wormbackground.gif")
wn.bgcolor("black")
wn.setup(width=610, height=610)
wn.tracer(0) #Turns of screen updates


#Worm Skull

wn.addshape("worm.gif")
wn.addshape("bloodbugs.gif")
skull = turtle.Turtle()
skull.speed(0)
skull.shape("worm.gif")
skull.color("brown")
skull.penup()
skull.goto(0,0)
skull.direction = "stop"



#food
food = turtle.Turtle()
food.speed(0)
food.shape("bloodbugs.gif")
food.color("red")
food.shapesize(0.5,0.5)
food.penup()
food.goto(0,100)


#fetus for functions

def move():
    if skull.direction == "up":
        y = skull.ycor()
        skull.sety(y + 20)

    if skull.direction == "down":
        y = skull.ycor()
        skull.sety(y - 20)

    if skull.direction == "left":
        x = skull.xcor()
        skull.setx(x - 20)

    if skull.direction == "right":
        x = skull.xcor()
        skull.setx(x + 20)

#worm segments

segments = []


#score

score = 0
high_score = 0

#pen
pen = turtle.Turtle()
pen.speed()
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0 Highscore: 0", align="center",font="NSimSun 12 bold")

def goup():
    skull.direction = "up"

def godown():
    skull.direction = "down"

def goleft():
    skull.direction = "left"

def goright():
    skull.direction = "right"

#Keyboard Bindings
wn.listen()
wn.onkey(goup, "Up")
wn.onkey(godown, "Down")
wn.onkey(goleft, "Left")
wn.onkey(goright, "Right")
#main game loop
while True:
    wn.update()

    if skull.xcor() > 290 or skull.xcor() < -290 or skull.ycor() > 290 or skull.ycor() < -290:
        time.sleep(1)
        skull.goto(0, 0)
        skull.direction = "stop"



        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        # Clear the segments list
        segments.clear()
        score = 0

        pen.clear()
        pen.write("Score: {} Highscore: {}".format(score,high_score),align="center", font="NSimSun 12 bold")


    if skull.distance(food) < 20:
        x = random.randrange(-250, 300,20)
        y = random.randrange(-270, 300,20)
        food.goto(x,y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        wn.addshape("wormskin.gif")

        new_segment.shape("wormskin.gif")
        new_segment.shapesize(1)
        new_segment.color("yellow")
        new_segment.penup()
        segments.append(new_segment)
        pen.clear()
        score += 10
        if score > high_score:
            high_score = score

            pen.clear()

        pen.write("Score: {} Highscore: {}".format(score,high_score),align="center", font="NSimSun 12 bold")



    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

    if len(segments) > 0:
        y = skull.ycor()
        x = skull.xcor()
        segments[0].goto(x,y)

    move()
    #body collision

    for segment in segments:
        if segment.distance(skull) < 20:
            time.sleep(1)
            skull.goto(0,0)
            skull.direction = "stop"
            for segment in segments:
                segment.goto(1000, 1000)
            pen.clear()
            score = 0
            pen.write("Score: {} Highscore: {}".format(score, high_score), align="center", font="NSimSun 12 bold")

            # Clear the segments list
            segments.clear()








    time.sleep(delay)


wn.mainloop()