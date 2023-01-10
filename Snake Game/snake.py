from turtle import Turtle
import turtle

#CONSTANTS
UP = 90
DOWN = 270 
RIGHT = 0
LEFT = 180

class Snake:
    global turtles

    def __init__(self) -> None:
        self.turtles = []
        self.create_snake()
    
    def create_snake(self): 
        for i in range(3):
            new_turtle = Turtle(shape="square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.goto(x=i*-20, y=0)
            self.turtles.append(new_turtle)

    def move(self): 
        for turtle_index in range(len(self.turtles) - 1,0,-1):
            nxt_x = self.turtles[turtle_index-1].xcor()
            nxt_y = self.turtles[turtle_index-1].ycor()
            self.turtles[turtle_index].goto(nxt_x,nxt_y)
        self.turtles[0].forward(20)
    

    def up(self): 
        turtle = self.turtles[0]
        if turtle.heading() != DOWN: 
            turtle.setheading(90)


    def down(self): 
        turtle = self.turtles[0]
        if turtle.heading() != UP: 
            turtle.setheading(270)


    def right(self): 
        turtle = self.turtles[0]
        if turtle.heading() != LEFT: 
            turtle.setheading(0)


    def left(self): 
        turtle = self.turtles[0]
        if turtle.heading() != RIGHT: 
            turtle.setheading(180)

    
    def extend(self): 
        #add new segment to snake
        self.add_segment(self.turtles[-1].position())

    def add_segment(self, position):
        new_turtle = Turtle(shape="square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        self.turtles.append(new_turtle)
    
    def reset(self):
        for snake in self.turtles:
            snake.goto(1000,1000)
        self.turtles.clear()
        self.create_snake()