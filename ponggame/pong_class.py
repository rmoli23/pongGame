from turtle import *

class Pong(Turtle):
    
    
    def __init__(self,pos):
        super().__init__()
       
       
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(5,1)

        self.goto(pos)
                



    def go_up(self):
        new_y=self.ycor() + 20
        self.goto(self.xcor(),new_y)
        
    def go_down(self):
        new_y=self.ycor() - 20
        self.goto(self.xcor(),new_y)

    
    