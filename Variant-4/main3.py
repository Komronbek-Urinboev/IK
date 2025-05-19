import turtle

screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(15)

t.begin_fill()
t.up()
t.goto(-150,0)
t.fillcolor("orange")
t.right(45)
for _ in range(2):
    t.circle(250, 90)
    t.circle(100, 90)
t.end_fill()

t.begin_fill()
t.up()
t.goto(-120,90)
t.fillcolor("black")
t.circle(20)
t.end_fill()

t.begin_fill()
t.up()
t.goto(-240,110)
t.fillcolor("green")
t.left(15)
t.forward(80)
t.right(120)
t.forward(80)
t.right(120)
t.forward(80)
t.end_fill()

t.begin_fill()
t.up()
t.goto(-230,180)
t.fillcolor("#A1C935")
t.circle(20)
t.end_fill()

t.begin_fill()
t.up()
t.goto(-180,290)
t.fillcolor("#A1C935")
t.circle(20)
t.end_fill()

t.begin_fill()
t.up()
t.goto(-180,290)
t.fillcolor("#A1C935")
t.circle(20)
t.end_fill()

t.begin_fill()
t.up()
t.goto(120,200 )
t.down()
t.fillcolor("#CA9BF7")

t.forward(100)
t.left(120)
t.forward(200)
t.left(150)
t.forward(173)
t.end_fill()


t.begin_fill()
t.up()
t.goto(-56,-60 )
t.down()
t.fillcolor("#CA9BF7")
t.forward(176)
t.right(90)
t.forward(100)
t.right(119)
t.forward(202)

t.end_fill()


t.begin_fill()
t.up()
t.goto( -200,-400)
t.fillcolor("orange")
t.right(62)
t.circle(100, 180)
t.left(90)
t.forward(200)
t.end_fill()


t.begin_fill()
t.up()
t.goto( 400,-400)
t.fillcolor("red")
t.left(90)
t.circle(120, 180)
t.left(90)
t.forward(240)
t.end_fill()


t.begin_fill()
t.up()
t.goto( 310,120)
t.fillcolor("blue")
t.right(90)
t.forward(90)
t.right(120)
t.forward(90)
t.right(120)
t.forward(90)
t.end_fill()



turtle.done()