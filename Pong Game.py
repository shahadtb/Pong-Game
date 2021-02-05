
import turtle
window = turtle.Screen()
window.title("Pong Game by Shahad Ababtain")
window.bgcolor("gray")
window.setup(width=900, height=700)
window.tracer(0)

#Computing Scores
score_one = 0
score_two = 0

# Paddle 1
paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.shapesize(stretch_wid=5, stretch_len=1) # to make it a rectangle
paddle1.color("Black")
paddle1.penup()
paddle1.goto(-400, 0)


#Paddle 2
paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.shapesize(stretch_wid=5, stretch_len=1) # to make it a rectangle
paddle2.color("Black")
paddle2.penup()
paddle2.goto(400, 0)

#Center Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("Black")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2


#upper header
header = turtle.Turtle()
header.color("Black")
header.penup()
header.hideturtle()
header.goto(0, 325)
header.write("Player 1: 0    Player 2: 0", font=("Arial", 16), align="center")


def paddle1_up(): #moving paddle 1 upwards
    y = paddle1.ycor()
    y += 20
    paddle1.sety(y)

def paddle1_down(): #moving paddle 1 downwards
    y = paddle1.ycor()
    y -= 20
    paddle1.sety(y)

def paddle2_up(): #moving paddle 2 upwards
    y = paddle2.ycor()
    y += 20
    paddle2.sety(y)

def paddle2_down(): #moving paddle 2 downwards
    y = paddle2.ycor()
    y -= 20
    paddle2.sety(y)


#to have window react to keyboard
window.listen()

#up and down keys for left player
window.onkeypress(paddle1_up, "q") # for left player easy keys for up and down on keyboard
window.onkeypress(paddle1_down, "a")

#up and down keys for right player
window.onkeypress(paddle2_up, "o") # for right player easy keys for up and down on keyboard
window.onkeypress(paddle2_down, "l")

#Game loop
while True:
    window.update()
    # Moving the ball on window
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor()+ ball.dy)

    # Border bounce off window size in coordinates :
    # y [350, -350]
    # and x [450, - 450]

    if ball.ycor() > 340: # TOP bounce off
        ball.sety(340)
        ball.dy *= -1
        score_one += 1
        header.clear()
        header.write(("Player 1: {}    Player 2: {}".format(score_one, score_two)), font=("Arial", 16), align="center")

    if ball.ycor() < -340: # BOTTOM bounce off
        ball.sety(-340)
        ball.dy *= -1
        score_two += 1
        header.clear()
        header.write(("Player 1: {}    Player 2: {}".format(score_one, score_two)), font=("Arial", 16), align="center")

    if ball.xcor() > 440: #RIGHT (when losing)
        ball.goto(0 ,0)
        ball.dx *= -1

    if ball.xcor() < -440: #LEFT (when losing)
        ball.goto(0, 0)
        ball.dx *= -1


    #Collisions of paddle and ball
    if ball.xcor() > 390 and (ball.xcor() < 400) and (ball.ycor() < paddle2.ycor() + 40 and ball.ycor() > paddle2.ycor -40):
        ball.setx(390)
        ball.dx *= -1

    if ball.xcor() < -390 and (ball.xcor() > -400) and (ball.ycor() < paddle2.ycor() + 40 and ball.ycor() > paddle2.ycor -40):
        ball.setx(-390)
        ball.dx *= -1



