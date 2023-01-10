"""
Ways to improve game: 

- add high score feature
"""

from turtle import Screen

from scoreboard import Scoreboard
from snake import Snake
from food import Food
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")

game_on = True
while game_on: 
    snake.move()
    screen.update()
    time.sleep(0.1)

    #Detect snake coming into contact with food
    if snake.turtles[0].distance(food) < 18: 
        food.refresh()
        snake.extend()
        scoreboard.update_score()

    #Detect collision with wall 
    if snake.turtles[0].xcor() > 290 or snake.turtles[0].xcor() <-290 or snake.turtles[0].ycor() > 290 or snake.turtles[0].ycor() < -290:
        scoreboard.reset()
        snake.reset()
        

    #Detect collision with tail
    for turtles in snake.turtles[1:]:
        if snake.turtles[0].distance(turtles) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()