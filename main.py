import time
from turtle import Screen,Turtle
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
screen = Screen()
screen.setup(width= 600, height= 600)
screen.bgcolor("black")
screen.title("my snake game ")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = ScoreBoard()



screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left , "Left")
screen.onkey(snake.right , "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance (food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
       scoreboard.reset()
       snake.reset()
    for segments in snake.segment:
        if segments == snake.head:
            pass
        elif snake.head.distance(segments) < 10:
           scoreboard.reset()
           snake.reset()


























screen.exitonclick()