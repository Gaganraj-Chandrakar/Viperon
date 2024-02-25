from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(1000, 750, starty=0)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

for index in range(3):
    snake.make_turtle()
head = snake.turtle_list[0]
screen.listen()
screen.onkeypress(snake.up, "w")
screen.onkeypress(snake.down, "s")
screen.onkeypress(snake.left, "a")
screen.onkeypress(snake.right, "d")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.08)
    snake.move()

    # Detect collision with the food
    if head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # Detect collision with wall
    if head.xcor() > 480 or head.xcor() < -480 or head.ycor() > 355 or head.ycor() < -355:
        game_is_on = False
        scoreboard.game_over()

    # Detect Collision with the body
    for turtle in snake.turtle_list[3:]:
        if head.distance(turtle) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
