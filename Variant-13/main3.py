import turtle

screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(15)


t.begin_fill()
t.up()
t.goto(-200, 0)
t.fillcolor("grey")
for i in range(2):
    t.backward(100)
    t.right(270)
    t.backward(200)
    t.right(270)

t.end_fill()


t.begin_fill()
t.up()
t.fillcolor("black")
t.backward(120)
t.right(320)
t.forward(100)
t.right(85)
t.forward(90)
t.end_fill()


t.begin_fill()
t.up()
t.goto(-265, -50)
t.fillcolor("green")
t.circle(25)
t.end_fill()


t.begin_fill()
t.up()
t.goto(-265, -105)
t.fillcolor("yellow")
t.circle(25)
t.end_fill()


t.begin_fill()
t.up()
t.goto(-265, -160)
t.fillcolor("red")
t.circle(25)
t.end_fill()





t.begin_fill()
t.up()
t.goto(0, 0)
t.fillcolor("purple")
t.left(45)
for i in range(4):
    t.forward(200)
    t.right(90)


t.end_fill()



t.begin_fill()
t.up()
t.goto(-20, 0)
t.fillcolor("light blue")
t.forward(240)
t.left(140)
t.forward(140)
t.left(75)
t.forward(160)

t.end_fill()



t.begin_fill()
t.up()
t.goto(135, -60)
t.down()
t.fillcolor("white")
t.right(35)
for i in range(4):
    t.forward(70)
    t.left(90)
t.end_fill()

t.begin_fill()
t.up()
t.goto(135, -60)
t.down()
t.fillcolor("white")
t.forward(35)
t.left(90)
t.forward(70)
t.left(90)
t.forward(35)
t.left(90)
t.forward(35)
t.left(90)
t.forward(70)
t.end_fill()


t.begin_fill()
t.up()
t.goto(20, 28)
t.fillcolor("light green")
t.right(75)
t.forward(70)
t.right(90)
t.forward(30)
t.right(90)
t.forward(70)
t.right(90)
t.forward(30)
t.end_fill()





turtle.done()