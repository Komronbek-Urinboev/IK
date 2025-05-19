import turtle
import math

def draw_filled_rectangle(x, y, width, height, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()

    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)

    t.end_fill()


# Настройка экрана
screen = turtle.Screen()
screen.bgcolor("lightblue")  # Задний цвет светло-голубой

# Создание черепахи
t = turtle.Turtle()
t.speed(0)

# Рисуем залитый прямоугольник
draw_filled_rectangle(x=100, y=200, width=300, height=350, color="lightyellow")
draw_filled_rectangle(x=140, y=160, width=70, height=70, color="lightblue")
draw_filled_rectangle(x=290, y=160, width=70, height=70, color="lightblue")
draw_filled_rectangle(x=220, y=1, width=70, height=150, color="green")
draw_filled_rectangle(x=-40, y=-40, width=20, height=100, color="brown")
draw_filled_rectangle(x=-202, y=-70, width=2, height=100, color="black")

def draw_isosceles_triangle(x, y, base, height, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()

    # Вычисляем координаты вершины
    top_x = x
    top_y = y + height

    left_x = x - base / 2
    left_y = y

    right_x = x + base / 2
    right_y = y

    # Рисуем треугольник
    t.goto(left_x, left_y)
    t.goto(top_x, top_y)
    t.goto(right_x, right_y)
    t.goto(left_x, left_y)

    t.end_fill()

# Рисуем равнобедренный треугольник с параметрами
draw_isosceles_triangle(x=250, y=200, base=300, height=80, color="yellow")
draw_isosceles_triangle(x=-30, y=-40, base=70, height=120, color="#66ff00")


def draw_circle(x, y, radius, color):
    """Рисует залитый круг."""
    t.penup()
    t.goto(x, y - radius)  # Смещаем вниз, чтобы центр был правильным
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()


def draw_petal(x, y, width, height, angle, color):
    """Рисует один лепесток в виде овала."""
    t.penup()
    t.goto(x, y)
    t.setheading(angle)  # Поворачиваем черепаху
    t.pendown()
    t.color(color)
    t.begin_fill()

    # Рисуем овал (имитируем с помощью растянутой окружности)
    t.circle(width, 90)
    t.circle(height, 90)
    t.circle(width, 90)
    t.circle(height, 90)

    t.end_fill()


circle_x = -200
circle_y = -50
radius = 10
draw_circle(circle_x, circle_y, radius, "white")

circle_x_s = -150
circle_y_s = 250
radius_s = 40
draw_circle(circle_x_s, circle_y_s, radius_s, "black")

draw_circle(circle_x_s, circle_y_s, radius_s - 1, "yellow")  # Чуть меньший радиус, чтобы граница была видна

num_petals = 10
petal_width = 10
petal_height = -2 # Доработано, чтобы лепестки были заметнее
petal_color = "yellow"

for i in range(num_petals):
    angle = i * (360 / num_petals)
    x_offset = math.cos(math.radians(angle)) * (radius_s + petal_height / 2)
    y_offset = math.sin(math.radians(angle)) * (radius_s + petal_height / 2)
    draw_petal(circle_x_s + x_offset, circle_y_s + y_offset, petal_width + 1, petal_height + 1, angle, "black")
    draw_petal(circle_x_s + x_offset, circle_y_s + y_offset, petal_width, petal_height, angle, petal_color)


num_petals = 8
petal_width = 30
petal_height = 0
petal_color = "yellow"

for i in range(num_petals):
    angle = i * (360 / num_petals)
    x_offset = math.cos(math.radians(angle)) * (radius + petal_height / 2)
    y_offset = math.sin(math.radians(angle)) * (radius + petal_height / 2)
    draw_petal(circle_x + x_offset, circle_y + y_offset, petal_width, petal_height, angle, petal_color)


def draw_oval(x, y, width, height, color):
    t.penup()
    t.goto(x, y - height / 2)  # Смещаем вниз, чтобы центр был правильным
    t.pendown()
    t.color(color)
    t.begin_fill()

    for _ in range(2):
        t.circle(width / 2, 100)
        t.circle(height / 2, 100)

    t.end_fill()
draw_oval(x=-201, y=-130, width=40, height=3, color="#66ff00")
draw_oval(x=-207, y=-133, width=40, height=3, color="#66ff00")
# Завершаем рисование
turtle.done()
