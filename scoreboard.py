import turtle

ALIGNMENT = "center"
FONT = ("Courier", 10, "normal")


class Scoreboard(turtle.Turtle):

    def __init__(self, user_name):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=260)
        self.color("white")
        self.score = 0
        self.user_name = user_name
        with open("best_player.txt", "r") as txt_file:
            data = txt_file.read().split(",")
            self.high_score = int(data[0])
            self.best_player = data[1]
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} Player: {self.user_name}\n"
                       f"High score {self.high_score} Player: {self.best_player}",
                   move=False,
                   align=ALIGNMENT,
                   font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.best_player = self.user_name
            with open("best_player.txt", "w") as txt_file:
                txt_file.write(f"{self.high_score},{self.best_player}")
        self.score = 0
        self.update_scoreboard()
