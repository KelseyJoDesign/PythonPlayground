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
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1

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