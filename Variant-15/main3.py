import turtle

screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(15)

#Ухо1
t.begin_fill()
t.fillcolor('yellow')
t.up()
t.goto(200,130)
t.circle(40)
t.end_fill()

#Ухо2
t.begin_fill()
t.fillcolor('yellow')
t.up()
t.goto(-200,130)
t.circle(40)
t.end_fill()

# лицо
t.begin_fill()
t.fillcolor('yellow')
t.up()
t.goto(0,-100)
t.down()
t.circle(200)
t.end_fill()


#Глаз1
t.begin_fill()
t.fillcolor('white')
t.up()
t.goto(-100,130)
t.down()
t.circle(40)
t.end_fill()

#зрачок1
t.begin_fill()
t.fillcolor('black')
t.up()
t.goto(-100,160)
t.circle(10)
t.end_fill()

#Глаз2
t.begin_fill()
t.fillcolor('white')
t.up()
t.goto(100,130)
t.down()
t.circle(40)
t.end_fill()

#зрачок2
t.begin_fill()
t.fillcolor('black')
t.up()
t.goto(100,160)
t.circle(10)
t.end_fill()

#Рот
t.begin_fill()
t.fillcolor('red')
t.up()
t.goto(-100,10)
t.down()
t.right(5)
t.forward(200)
t.left(85)
t.forward(20)
t.left(95)
t.forward(200)
t.left(85)
t.forward(20)
t.end_fill()

# нос
t.begin_fill()
t.fillcolor('white')
t.up()
t.goto(-20,110)
t.down()
t.right(25)
for _ in range(2):
    t.circle(40, 90)
    t.circle(20, 90)

t.end_fill()

#Бровь1
t.begin_fill()
t.fillcolor('black')
t.up()
t.goto(-120,250)
t.left(85)
t.forward(100)
t.left(85)
t.forward(20)
t.left(90)
t.forward(100)
t.left(90)
t.forward(29)
t.end_fill()


t.begin_fill()
t.fillcolor('black')
t.up()
t.goto(120,250)
t.left(-10)
t.forward(100)
t.left(270)
t.forward(20)
t.right(90)
t.forward(95)
t.right(78)
t.forward(20)
t.end_fill()





























turtle.done()




