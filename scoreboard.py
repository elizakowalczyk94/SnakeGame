import turtle

ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")


class Scoreboard(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=260)
        self.color("white")
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"Score: {self.score}",
                   move=False,
                   align=ALIGNMENT,
                   font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
