from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0) # this is used to turn off (in this case) Turtle animation

# paddles, tuples below
r_paddle = Paddle((350,0)) # demonstrates how important classes are for concise and effective coding
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen() # tells pc to pay attention to keyboard inputs
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect if ball misses paddle
    if ball.distance(r_paddle) > 45 and ball.xcor() > 380 or ball.distance(r_paddle) > 45 and ball.xcor() < -380:
        ball.goto(0,0)
        ball.resetMove()
    
    if ball.distance(r_paddle) > 45 and ball.xcor() > 370:
        scoreboard.l_point()
    
    if ball.distance(l_paddle) > 45 and ball.xcor() < -370:
        scoreboard.r_point()
    
        
screen.exitonclick()
