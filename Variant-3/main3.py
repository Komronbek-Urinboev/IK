import turtle

# Настройка экрана
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(0)

# Вспомогательная функция для рисования круга по координатам центра
def draw_circle(x, y, radius, color):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Вспомогательная функция для рисования треугольного листа
def draw_leaf(points, color):
    t.penup()
    t.goto(points[0])
    t.pendown()
    t.color(color)
    t.begin_fill()
    for point in points[1:]:
        t.goto(point)
    t.goto(points[0])
    t.end_fill()

# Рисуем лепестки
draw_circle(-70, 170, 50, "red")  # Левый верхний
draw_circle(70, 170, 50, "purple")  # Правый верхний
draw_circle(-55, 80, 50, "darkviolet")  # Левый нижний
draw_circle(60, 80, 50, "orange")  # Правый нижний
draw_circle(0, 210, 50, "mediumpurple")  # Верхний

# Рисуем центр
draw_circle(0, 130, 50, "yellow")

# Рисуем стебель
t.penup()
t.goto(0, 80)
t.setheading(-90)
t.pendown()
t.color("green")
t.pensize(15)
t.forward(300)

# Рисуем листья
draw_leaf([(-60, 40), (-10, 70), (-90, 0)], "limegreen")  # Левый лист
draw_leaf([(60, 40), (10, 70), (90, 0)], "limegreen")  # Правый лист

# Спрятать черепаху
t.hideturtle()
screen.mainloop()
