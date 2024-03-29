from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard 

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    ## detect the distance between food and snake
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_segment()
        scoreboard.increase_score()

    if snake.head.xcor() > 295 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    ## Detect if head collied with tail, trigger game over 
    for segment in snake.segments[1:]:           ## Slicing removing the first index 0                                                
        if snake.head.distance(segment) < 10:    ####if segment == snake.head: removed using slicing 
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()