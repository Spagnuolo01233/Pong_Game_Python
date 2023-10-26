# Simple Pong Game in Python.

import turtle

# The Window for the game.
window = turtle.Screen()
window.title("Pong Game By Pietro")
window.bgcolor("green")
window.setup(width=800, height=600)
window.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)



# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color('red')
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)



# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color('white')
ball.penup()
ball.goto(0,0)
ball.dx = 3.5
ball.dy = -3.5

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A : {} Player B : {}".format(score_a,score_b), align="center", font=("Italic",24, "normal"))


# Function for the movement of paddles and ball.
def paddle_a_up():
    y = paddle_a.ycor()
    y += 25
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 25
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 25
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 25
    paddle_b.sety(y)

# Keyboard binding
window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "o")
window.onkeypress(paddle_b_down, "l")

# Variable to track if the game is over
game_over = False


# Main game loop
while not game_over:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking for the ball
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A : {} Player B : {}".format(score_a,score_b), align="center", font=("Italic",24, "normal"))
        if score_a == 2:
            pen.clear()
            pen.write("Player A Win!!!!!",align="center", font=("Italic",24, "normal" ))
            window.update()
            result = window.textinput("Game Over", "Press Enter to restart or type 'exit to close the game")
            if result == "exit":
                game_over = True
            else:
                score_a = 0
                score_b = 0
                pen.clear()
                pen.write("Player A : {} Player B : {}".format(score_a,score_b), align="center", font=("Italic",24, "normal"))


    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A : {} Player B : {}".format(score_a,score_b), align="center", font=("Italic",24, "normal"))
        if score_b == 2:
            pen.clear()
            pen.write("Player B Win!!!!!",align="center", font=("Italic",24, "normal" ))
            window.update()
            result = window.textinput("Game Over", "Press Enter to restart or type 'exit to close the game")
            if result == "exit":
                game_over = True
            else:
                score_a = 0
                score_b = 0
                pen.clear()
                pen.write("Player A : {} Player B : {}".format(score_a,score_b), align="center", font=("Italic",24, "normal"))

    # Paddle & ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
