from turtle import Turtle, Screen
import random  as r

timmy=Turtle()


timmy.shape("classic")
timmy.pensize(2)
timmy.speed('fastest')

############"Drawing a spirograph"###############
def draw_spirograph(gap_angle):
    for _ in range(360//gap_angle):
        r1=r.random()
        g=r.random()
        b= r.random()
        timmy.pencolor((r1, g, b))
        timmy.circle(100)
        timmy.setheading(timmy.heading() + gap_angle)

draw_spirograph(5)











############"Drawing a random walk"###############
# stop=False

# while not stop:
#     r1=r.random()
#     g=r.random()
#     b= r.random()
#     direction=r.randint(1,4)*90
#     timmy.pencolor((r1, g, b))
#     timmy.right(direction)
#     timmy.forward(30)
    


############"Drawing different Polygons"###############
# for side_number in range(3,11):
#     r1=r.random()
#     g=r.random()
#     b= r.random()
#     timmy.pencolor((r1, g, b))
#     for _ in range(side_number):
#         timmy.forward(100)
#         timmy.right(360/side_number)








screen= Screen()
screen.exitonclick()
























