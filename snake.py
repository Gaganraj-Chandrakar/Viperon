from turtle import Turtle

MOVE_DISTANCE = 20


class Snake:
    turtle_list = []

    position = 0
    i = 1

    def make_turtle(self):
        new_turtle = Turtle(shape="square")
        new_turtle.color("white")
        new_turtle.penup()
        self.turtle_list.append(new_turtle)
        new_turtle.teleport(x=self.turtle_list[self.i - 1].xcor() + self.position)
        self.position -= 20
        self.i += 1

    def move(self):
        for turtle_num in range(len(self.turtle_list) - 1, 0, -1):
            new_x = self.turtle_list[turtle_num - 1].xcor()
            new_y = self.turtle_list[turtle_num - 1].ycor()
            self.turtle_list[turtle_num].goto(new_x, new_y)

        self.turtle_list[0].forward(MOVE_DISTANCE)

    def add_body(self, position):
        new_body = Turtle("square")
        new_body.color("white")
        new_body.penup()
        new_body.goto(position)
        self.turtle_list.append(new_body)

    def extend(self):
        self.add_body(self.turtle_list[-1].position())

    def up(self):
        if self.turtle_list[0].heading() != 270:
            self.turtle_list[0].setheading(90)

    def down(self):
        if self.turtle_list[0].heading() != 90:
            self.turtle_list[0].setheading(270)

    def left(self):
        if self.turtle_list[0].heading() != 0:
            self.turtle_list[0].setheading(180)

    def right(self):
        if self.turtle_list[0].heading() != 180:
            self.turtle_list[0].setheading(0)

