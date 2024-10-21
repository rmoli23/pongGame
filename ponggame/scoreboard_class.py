from turtle import *

ALIGNMENT="center"
FONT=("Courier",16,"bold")
FONT_GAME_OVER=("Arial",24,"bold")

class Scoreboard(Turtle):
    
   
    
    def __init__(self):
        super().__init__()
        self.l_score=0
        self.r_score=0
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.color("White")
        self.update_score()
        
        
    def update_score (self):
        
        self.clear()
        self.write(f"Score: {self.l_score} - {self.r_score}",False,ALIGNMENT,FONT)
        
    def r_point(self):
        self.r_score+=1
        self.update_score()
    def l_point(self):
        self.l_score+=1
        self.update_score()
    
    def game_over(self):
        
        self.goto(0,0)
        self.write(f"GAME OVER",False,ALIGNMENT,FONT)