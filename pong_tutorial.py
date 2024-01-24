# follow along code by freeCodeCamp YouTube
# Part 1: Getting Started

# turtle lets you import basic game graphics; built in and simpler compared to PyGame
import turtle
import time

# create a window with manual window updating (tracer) for speed performance
win = turtle.Screen()
win.title("Pong by freeCodeCamp")
win.bgcolor("navy")
win.setup(width=800, height=600)
win.tracer(0)

# Score
score_a = 0
score_b = 0

# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=5)
paddle_a.penup()
paddle_a.goto(-350, 0)

# paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("orange")
paddle_b.shapesize(stretch_wid=5, stretch_len=5) 
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("purple")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

# keep score with pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Silkscreen", 24, "normal"))


# Function of paddles *yay*
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 250:  # Check if paddle a is below the top boundary
        y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    if y > -250:  # Check if paddle a is below the top boundary
        y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    if y < 250:  # Check if paddle b is below the top boundary
        y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    if y > -250:  # Check if paddle b is below the top boundary
        y -= 20
    paddle_b.sety(y)

# buttons to mash
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")



# Create a screen
win = turtle.Screen()
win.title("Yarn Ball")
win.bgcolor("blue")
win.setup(width=800, height=600)

# Title
title = turtle.Turtle()
title.hideturtle()
title.penup()
title.color("white")
title.goto(0, 150)
title.write("Yarn Ball", align="center", font=("Arial", 24, "normal"))

# "Go!" Button
button = turtle.Turtle()
button.shape("square")
button.color("purple")
button.shapesize(stretch_wid=2, stretch_len=3)
button.penup()
button.goto(0, -150)
button_label = turtle.Turtle()
button_label.hideturtle()
button_label.penup()
button_label.goto(0, -160)
button_label.write("Go!", align="center", font=("Arial", 16, "normal"))

# Function to start the game
def start_game(x, y):
    # Hide home screen elements
    title.clear()
    button.hideturtle()
    button_label.clear()

    # Start the game loop
    # (Place your game loop code here)

# Bind the click event to the "Go!" button
button.onclick(start_game)




# Main game loop
while True:
    win.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)



    # Ball go boyoyoiiing top and bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        
    # ball go bye bye left and right
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Silkscreen", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Silkscreen", 24, "normal"))



   # Ball bounces off paddle B
    if (ball.xcor() > paddle_b.xcor() - 50 and ball.xcor() < paddle_b.xcor() - 40) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(paddle_b.xcor() - 50)
        ball.dx *= -1
       
    # Ball bounces off paddle A
    if (ball.xcor() < paddle_a.xcor() + 50 and ball.xcor() > paddle_a.xcor() + 40) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(paddle_a.xcor() + 50)
        ball.dx *= -1
    


    #Control Frame rate from going bonkers
    time.sleep(1/60)