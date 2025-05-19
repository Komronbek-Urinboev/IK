import turtle

screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(16)

#тело
t.begin_fill()
t.up()
t.goto(150,-170)
t.down()
t.fillcolor('yellow')
t.circle(150)
t.end_fill()

#голова
t.begin_fill()
t.up()
t.goto(-29,50)
t.down()
t.fillcolor('yellow')
t.circle(90)
t.end_fill()

#глаза
t.begin_fill()
t.up()
t.goto(-49,130)
t.down()
t.fillcolor('black')
t.circle(20)
t.end_fill()

#рот
t.begin_fill()
t.up()
t.goto(-119,160)
t.down()
t.fillcolor('red')
t.right(90)
t.forward(70)
t.right(135)
t.forward(70)
t.right(90)
t.forward(70)
t.right(135)
t.forward(29)
t.end_fill()

#крыло
t.begin_fill()
t.up()
t.goto(90,20)
t.down()
t.fillcolor('yellow')
t.right(25)
t.forward(60)
t.left(95)
t.forward(150)
t.left(135)
t.forward(190)
t.left(129)
t.forward(80)
t.end_fill()


#Нога1
t.begin_fill()
t.up()
t.goto(90,-160)
t.down()
t.fillcolor('red')
t.forward(100)
t.right(65)
t.forward(120)
t.right(150)
t.forward(187)
t.end_fill()

#Нога2
t.begin_fill()
t.up()
t.goto(180,-160)
t.down()
t.right(135)
t.forward(100)
t.right(65)
t.forward(120)
t.right(151)
t.forward(187)

t.end_fill()



#
t.begin_fill()
t.up()
t.goto(260,90)
t.down()
t.fillcolor('yellow')
t.right(90)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.end_fill()





turtle.done()

                         