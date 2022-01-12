from turtle import Screen
import time
from Snake import Snake
import food
import scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

user_name = screen.textinput(title="User data", prompt="Enter your name: ")

food = food.Food()
snake = Snake()
scoreboard = scoreboard.Scoreboard(user_name)


def play_game():
    is_game_on = True
    while is_game_on:
        screen.update()
        time.sleep(0.1)
        scoreboard.update_scoreboard()
        snake.move()

        # detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        # detect collision with wall
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            scoreboard.reset()
            snake.reset()

        # detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.reset()
                snake.reset()


scoreboard.start_game()
screen.listen()
screen.onkey(play_game, "space")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

screen.exitonclick()
