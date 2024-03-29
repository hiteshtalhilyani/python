from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score =0
        self.color("white")
        self.hideturtle()
        self.l_score =0
        self.r_score =0
        self.penup()
        self.update_scoreboard()
        

    def update_scoreboard(self):
        self.clear()
        self.goto(-100,200)
        self.write(f"{self.l_score}",align="center",font =("Courier",40,"normal"))
        self.goto(100,200)
        self.write(f"{self.r_score}",align="center",font =("Courier",40,"normal"))
    
    def l_point(self):
        self.l_score +=1
        self.update_scoreboard()

    def r_point(self):
        self.r_score +=1
        self.update_scoreboard()

        
        