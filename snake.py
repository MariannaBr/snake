from turtle import Turtle

positions = [(0, 0), (-20, 0), (-40, 0)]
UP = 90.0
DOWN = 270.0
RIGHT = 0.0
LEFT = 180.0

class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for position in positions:
            self.add_tile(position)

    def add_tile(self, position):
        new_tile = Turtle()
        new_tile.shape("square")
        new_tile.color("white")
        new_tile.penup()
        new_tile.goto(position)
        self.snake.append(new_tile)

    def extend(self):
        self.add_tile(self.snake[-1].position())

    def move(self):
        for i in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[i - 1].xcor()
            new_y = self.snake[i - 1].ycor()
            self.snake[i].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)