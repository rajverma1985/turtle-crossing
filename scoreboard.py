from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(140, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", font=FONT)

    def keep_score(self):
        self.score += 10 + self.score * 0.5
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, font=FONT, align="center")

    def restart(self):
        self.goto(-220, 280)
        self.write(f"RESTART GAME", False, font=FONT, align="center")

    def exit(self):
        self.goto(250, 280)
        self.write(f"EXIT", False, font=FONT, align="center")


class LevelUp(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()
        self.goto(-280, 270)
        self.update_level()

    def update_level(self):
        self.goto(-280, 270)
        self.write(f"Level: {self.level}", font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.update_level()
