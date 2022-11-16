import turtle

t=turtle.Turtle()
s = turtle.Screen()

s.bgcolor('black')
t.hideturtle()
t.goto(0,-10)

t.pensize(3)
t.color('red')
t.begin_fill()
t.left(140)
t.forward(180)
t.circle(-90,200)
t.setheading(60)
t.circle(-90,200)
t.forward(178)
t.end_fill()

t.penup()
t.goto(-100,130)
t.pendown() 
t.color('white')
# t.write("te amo esterzinha",font = ("Verdana",15,"bold"))
t.write("Te amo Esterzinha",font = ("Verdana",15,"bold"))

t.penup()
t.goto(-180,-130)
t.pendown() 
t.color('white')
# t.write("te amo esterzinha",font = ("Verdana",15,"bold"))
t.write("Bernardo te ama Esterzinha S2",font = ("Verdana",15,"bold"))


turtle.done()