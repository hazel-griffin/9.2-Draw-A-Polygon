from turtle import*

def regular_polygon(turtle,sides):
    turtle.begin_fill()
    for i in range(sides):
        turtle.forward(200)
        turtle.left(360/sides)
    turtle.end_fill()

def unknown(turtle):
    turtle.clear()
    turtle.begin_fill()
    turtle.goto(0,75)
    turtle.goto(30,60)
    turtle.goto(10,-20)
    turtle.goto(0,0)
    turtle.end_fill()

def trapezoid(turtle):
    turtle.clear()
    turtle.begin_fill()
    turtle.forward(100)
    turtle.goto(75,25)
    turtle.setheading(180)
    turtle.forward(50)
    turtle.goto(0,0)
    turtle.end_fill()

def rectangle(turtle):
    turtle.clear()
    turtle.begin_fill()
    turtle.goto(100,0)
    turtle.goto(100,50)
    turtle.goto(0,50)
    turtle.goto(0,0)
    turtle.end_fill()

def parallelogram(turtle):
    turtle.clear()
    pass




screen = Screen()
screen.title("polygons")
screen.bgcolor("violet")
screen.setup(width = 800, height = 600)

pen = Turtle()
pen.hideturtle()
pen.speed(0)

polygon = {3: "Triangle", 4: "Quadrilateral", 5: "Pentagon", 6: "hexagon"}
quad = {}
while True:
    sides = int(input("Enter the number of sides that the polygon has: "))
    pen.clear()
    if sides<3:
        pen.write("polygons must have at least 3 sides")
    else:
        regular_polygon(pen,sides)
        if sides in polygon:
            print(polygon[sides])
            if polygon[sides] == "Quadrilateral":
                parallel = input("How many sides of the shape are parallel?")
                if parallel == "4":
                    four = input(("Do all sides have the same length"))
                    if four == "Yes":
                        print("Square")
                    else:
                        rectang = input("Do all angles have the same measure ")
                        if rectang == "Yes":
                            print("Rectangle")
                            rectangle(pen)
                        else:
                            print("Parallelogram")
                elif parallel == "2":
                    print("trapezoid")
                    trapezoid(pen)
                else:
                    print("unknown quadrilateral")
                    unknown(pen)
            else:
                pass
        else:
            print("unknown")



screen.exitonclick()