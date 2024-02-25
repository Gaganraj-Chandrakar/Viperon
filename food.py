from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5, 1)
        self.color("blue")
        self.speed(0)
        self.refresh()

    def refresh(self):
        rand_xcor = random.randint(-485, 485)
        rand_ycor = random.randint(-360, 360)
        self.goto(rand_xcor, rand_ycor)
