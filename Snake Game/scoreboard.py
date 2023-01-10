from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', '15', 'normal')


class Scoreboard(Turtle): 

    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        with open(r'Snake Game\High_score') as data:
            self.highscore = int(data.read())
        self.goto(0,270)
        self.color("white")
        self.hideturtle()
        self.write_score()

    def update_score(self):
        self.score +=1
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    # def game_over(self): 
    #     self.goto(0,0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
    
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open(r'Snake Game\High_score', mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.write_score()