"""EX05 - The Sun and the Ocean - ."""

__author__ = "730529193"

from turtle import Turtle, colormode, tracer, update, done


def draw_rectangle(a_turtle: Turtle, x: float, y: float, width: float, height: float) -> None:
    """Draws the body (rectangles) of the robot using x and y and width and height."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown()
    a_turtle.pencolor("grey")
    a_turtle.begin_fill()
    a_turtle.fillcolor("grey")
    i = 0
    while i < 4:
        a_turtle.forward(width)
        a_turtle.left(90)
        a_turtle.forward(height)
        a_turtle.left(90)
        i += 1
    a_turtle.end_fill()


def draw_triangle(b_turtle: Turtle, x: float, y: float, width: float, height: float) -> None:
    """Draws the eyes (triangles) of the robot using x and y coordinates and width and height."""
    b_turtle.penup()
    b_turtle.goto(x, y)
    b_turtle.pendown()
    b_turtle.begin_fill()
    b_turtle.fillcolor("red")
    i = 0
    while i < 3:
        b_turtle.forward(width)
        b_turtle.left(120)  
        i += 1
    b_turtle.end_fill()


def draw_line(c_turtle: Turtle, x: float, y: float, width: float, height: float) -> None:
    """Draws the antena (a line) of the robot using x and y coordinates and width and height."""
    c_turtle.penup()
    c_turtle.goto(x, y)
    c_turtle.pendown()
    c_turtle.setheading(90)
    c_turtle.begin_fill()
    c_turtle.fillcolor("black")
    c_turtle.forward(height)
    c_turtle.end_fill()


def draw_square(d_turtle: Turtle, x: float, y: float, width: float, height: float) -> None:
    """Draws the mouth and feet (squares) of the robot using x and y coordinates and width and height."""
    d_turtle.penup()
    d_turtle.goto(x, y)
    d_turtle.pendown()
    d_turtle.begin_fill()
    d_turtle.fillcolor("black")
    i = 0
    while i < 4:
        d_turtle.forward(width)
        d_turtle.left(90)
        d_turtle.forward(height)
        d_turtle.left(90)
        i += 1
    d_turtle.end_fill()


def main() -> None:
    """Calls the functions, which draws the shapes of the robot."""
    tracer(0, 0)
    colormode(255)
    a_turtle: Turtle = Turtle()
    a_turtle.speed(0)
    b_turtle: Turtle = Turtle()
    b_turtle.speed(0)
    c_turtle: Turtle = Turtle()
    c_turtle.speed(0)
    d_turtle: Turtle = Turtle()
    d_turtle.speed(0)
    draw_rectangle(a_turtle, -50, 0, 50, 200)
    draw_rectangle(a_turtle, 0, 0, 50, 200)
    draw_rectangle(a_turtle, -200, 100, 200, 50)
    draw_rectangle(a_turtle, 20, 100, 200, 50)
    draw_triangle(b_turtle, -35, 160, 30, 50)
    draw_triangle(b_turtle, 5, 160, 30, 50)
    draw_line(c_turtle, -25, 200, 10, 100)
    draw_square(d_turtle, -10, 120, 20, 20)
    draw_square(d_turtle, 50, 0, 20, 20)
    draw_square(d_turtle, -70, 0, 20, 20)
    a_turtle.hideturtle()
    b_turtle.hideturtle()
    d_turtle.hideturtle()
    
    update()
    done()


if __name__ == "__main__":
    main()