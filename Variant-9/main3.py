import turtle as tur

screen = tur.Screen()
screen.bgcolor("white")

t = tur.Turtle()
t.speed(15)

t.begin_fill()
t.up()
t.goto(-400,-270)
t.fillcolor("brown")
for i in range(2):
    t.forward(800)
    t.right(90)
    t.forward(50)
    t.right(90)
t.end_fill()



t.begin_fill()
t.up()
t.goto(-300,-267)
t.fillcolor("black")
t.circle(45)
t.end_fill()


t.begin_fill()
t.up()
t.goto(-150,-267)
t.fillcolor("black")
t.circle(45)
t.end_fill()

t.begin_fill()
t.up()
t.goto(200,-267)
t.fillcolor("black")
t.circle(45)
t.end_fill()


t.begin_fill()
t.up()
t.goto(-90,-220)
t.fillcolor("orange")
for i in range(2):
    t.forward(220)
    t.left(90)
    t.forward(500)
    t.left(90)
t.end_fill()

t.begin_fill()
t.up()
t.goto(130,-170)
t.fillcolor("yellow")
for i in range(2):
    t.forward(200)
    t.left(90)
    t.forward(300)
    t.left(90)
t.end_fill()


t.begin_fill()
t.up()
t.goto(-90,-170)
t.fillcolor("#2a9df4")
for i in range(2):
    t.backward(300)
    t.right(90)
    t.backward(400)
    t.right(90)
t.end_fill()

t.begin_fill()
t.up()
t.goto(-40,130)
t.fillcolor("#ADDFFF")
for i in range(4):
    t.forward(120)
    t.left(90)
t.end_fill()

t.begin_fill()
t.up()
t.goto( -120,230)
t.left(90)
t.fillcolor("yellow")
t.circle(120, 180)
t.left(90)
t.forward(240)
t.end_fill()
tur.done()