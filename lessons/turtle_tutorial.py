from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()
leo.penup()
leo.goto(-150, 55)
leo.pendown()
leo.speed(10)
leo.hideturtle()
leo.begin_fill()  
leo.color(99, 204, 250)  

i = 0
while i < 3:
    leo.forward(300)
    leo.left(120)
    i += 1

leo.end_fill()  

