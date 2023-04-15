from turtle import Turtle

class Paddle(Turtle):

    # __init__(self) is used to initialize a new paddle object from the Paddle class
    # super().__init__() follows b/c super class (Turtle) must initialize itself, as well

    def __init__(self, position): # position determines where the paddle goes to
        super().__init__()
        self.shape("square") # self class is same as Paddle class which is akin to Turtle calss w/ additional attributes
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)