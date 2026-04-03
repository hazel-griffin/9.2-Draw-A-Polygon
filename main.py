from turtle import*

def regular_polygon(turtle,sides):
    turtle.begin_fill()
    for i in range(sides):
        turtle.forward(200)
        turtle.left(360/sides)
    turtle.end_fill()

screen = Screen()
screen.title("polygons")
screen.bgcolor("violet")
screen.setup(width = 800, height = 600)

pen = Turtle()
pen.hideturtle()
pen.speed(0)


while True:
    sides = int(input("Enter the number of sides that the polygon has: "))
    pen.clear()
    if sides<3:
        pen.write("polygons must have at least 3 sides")
    else:
        regular_polygon(pen,sides)


screen.exitonclick()