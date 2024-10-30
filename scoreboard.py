# from turtle import Turtle

# class Scoreboard(Turtle):
#     def __init__ (self):
#         super().__init__()
#         self.score = 0
#         self.color = "pink"
#         self.write(f"score : {self.score}", align="center", font=("Arial", 24, "normal"))
#         self.hideturtle()


from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()  # Hide the turtle cursor
        self.goto(0, 260)  # Position scoreboard at the top of the screen
        self.update_score()  # Display the initial score

    def update_score(self):
        self.clear()  # Clear previous score before updating
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))
