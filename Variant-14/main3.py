import turtle

# Настройка экрана
screen = turtle.Screen()
screen.bgcolor("lightblue")  # Задний цвет светло-голубой

# Создание черепахи
t = turtle.Turtle()
t.speed(0)

# Рисуем желтый круг
t.penup()
t.goto(-150, 100)
t.pendown()
t.color("yellow")
t.begin_fill()
t.circle(100)
t.end_fill()

# Рисуем перевернутый красный полукруг
t.penup()
t.goto(-241, 240)  # Опускаем немного вниз
t.setheading(-114)  # Устанавливаем направление
t.pendown()
t.color("red")
t.begin_fill()
t.circle(100, -130)  # Рисуем дугу в обратном направлении
t.end_fill()


def draw_trapezoid(x, y, width_top, width_bottom, height, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()

    # Нижнее основание (меньше верхнего)
    t.goto(x + width_bottom / 2, y)
    t.goto(x + width_top / 2, y + height)
    t.goto(x - width_top / 2, y + height)
    t.goto(x - width_bottom / 2, y)

    t.end_fill()
# Рисуем трапецию с параметрами (x, y, верхнее основание, нижнее основание, высота, цвет)
draw_trapezoid(x=-145, y=-50, width_top=160, width_bottom=80, height=80, color="brown")


def draw_triangle(x, y, base, height, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)

    # Рисуем перевернутый треугольник
    t.goto(x + base / 2, y)
    t.goto(x, y - height)
    t.goto(x - base / 2, y)
    t.goto(x, y)  # Возвращаемся к начальной точке
# Рисуем два перевернутых треугольника с заданными параметрами
draw_triangle(x=-150, y=240, base=190, height=250, color="black")
draw_triangle(x=-150, y=200, base=110, height=150, color="black")

# Завершаем рисование
turtle.done()
