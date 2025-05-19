import turtle

screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(15)

t.begin_fill()
t.up()
t.goto(-170,-90)
t.fillcolor("green")
for i in range(2):
    t.forward(400)
    t.left(90)
    t.forward(200)
    t.left(90)
t.end_fill()

t.begin_fill()
t.up()
t.goto(-170,-90)
t.fillcolor("#305CDE")
t.left(90)
t.forward(200)
t.left(90)
t.forward(200)
t.left(135)
t.forward(300)
t.end_fill()


t.begin_fill()
t.up()
t.goto(230,-90)
t.fillcolor("#305CDE")
t.left(135)
t.forward(200)
t.right(90)
t.forward(200)
t.right(135)
t.forward(283)
t.end_fill()

t.begin_fill()
t.up()
t.goto(60,50)
t.fillcolor("yellow")
t.circle(70)
t.end_fill()


t.begin_fill()
t.up()
t.goto( -120,50)
t.fillcolor("yellow")
t.circle(70)
t.end_fill()


t.begin_fill()
t.up()
t.goto( -170,110)
t.fillcolor("red")
t.right(135)
for i in range(2):
    t.forward(200)
    t.right(90)
    t.forward(160)
    t.right(90)
t.end_fill()


t.begin_fill()
t.up()
t.goto( 50,110)
t.fillcolor("red")
for i in range(2):
    t.forward(100)
    t.right(90)
    t.forward(150)
    t.right(90)
t.end_fill()

t.begin_fill()
t.up()
t.goto( 100,210)
t.fillcolor("yellow")
for i in range(2):
    t.forward(150)
    t.right(90)
    t.forward(50)
    t.right(90)
t.end_fill()



t.begin_fill()
t.up()
t.goto( 10,310)
t.fillcolor("yellow")
t.circle(100, 180)
t.left(90)
t.forward(200)
t.end_fill()


turtle.done()