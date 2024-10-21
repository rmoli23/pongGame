from turtle import *
from pong_class import Pong
from ball_class import Ball
from scoreboard_class import Scoreboard
import time


    


screen = Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


r_paddle=Pong((350,0))
l_paddle=Pong((-350,0))
ball =Ball()
scoreboard=Scoreboard()


screen.listen()
screen.onkeypress(l_paddle.go_up,"w")
screen.onkeypress(l_paddle.go_down,"s")
screen.onkeypress(r_paddle.go_up,"Up")
screen.onkeypress(r_paddle.go_down,"Down")

game_is_on=True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor()>290 or ball.ycor()<-290:
        ball.bounce_y()
    if ball.distance(r_paddle)<50 and ball.xcor()>330 or ball.distance(l_paddle)<50 and ball.xcor()<-330:
        ball.bounce_x()
        
        
    if ball.xcor()>360:
        scoreboard.l_point()
        ball.restart()
        
        
       
    if ball.xcor()<-360:
        scoreboard.r_point()
        ball.restart()
        
        
        
        
       
            
    
        
   

    





screen.exitonclick()

