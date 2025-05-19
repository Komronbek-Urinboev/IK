import turtle
import math

# Настройка экрана и черепахи
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("skyblue")  # голубое небо

t = turtle.Turtle()
t.speed(0)  # Максимальная скорость для быстрой отрисовки
t.hideturtle()


# Функция для рисования травы (фон внизу)
def draw_grass():
    t.penup()
    t.goto(-400, -400)  # Начальная точка для травы немного изменена для охвата экрана 800x600
    t.pendown()
    t.color("lightgreen")
    t.begin_fill()
    for _ in range(2):
        t.forward(1200)  # Ширина травы соответствует ширине экрана
        t.left(90)
        t.forward(300)  # Высота травы (от -200 до 0 по y)
        t.left(90)
    t.end_fill()


def draw_sun(x, y, radius):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.color("yellow")
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

    # Лучи солнца
    for angle in range(0, 360, 40):
        t.penup()
        # Центр маленького круга-луча
        ray_center_x = x + (radius + 15) * math.cos(math.radians(angle))  # Уменьшил расстояние лучей от солнца
        ray_center_y = y + (radius + 15) * math.sin(math.radians(angle))
        # Перемещаемся к нижней точке маленького круга-луча для t.circle()
        t.goto(ray_center_x, ray_center_y - 8)  # 8 - радиус луча
        t.pendown()
        t.begin_fill()
        t.circle(8)
        t.end_fill()


# Функция для рисования домика
def draw_house(x, y):
    body_width = 150
    body_height = 100

    # Тело домика
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("lightgrey")
    t.begin_fill()
    for _ in range(2):
        t.forward(body_width)
        t.left(90)
        t.forward(body_height)
        t.left(90)
    t.end_fill()

    # Крыша (красный равнобедренный треугольник)
    roof_height = body_width * 0.6  # Высота крыши
    t.penup()
    t.goto(x, y + body_height)
    t.pendown()
    t.color("red")
    t.begin_fill()
    t.goto(x + body_width / 2, y + body_height + roof_height)  # Вершина крыши
    t.goto(x + body_width, y + body_height)  # Правый край крыши
    t.goto(x, y + body_height)  # Левый край крыши (замыкаем)
    t.end_fill()

    # Синее круглое окно (в центре крыши)
    window_roof_radius = 15
    roof_center_x = x + body_width / 2
    roof_peak_y = y + body_height + roof_height
    # Расположим окно чуть ниже вершины крыши
    window_center_y = y + body_height + roof_height * 0.5

    t.penup()
    t.goto(roof_center_x, window_center_y - window_roof_radius)  # Переходим к нижней точке окна
    t.pendown()
    t.color("blue")
    t.begin_fill()
    t.circle(window_roof_radius)
    t.end_fill()

    # Квадратное окно (расположено левее на теле дома)
    square_window_size = 35
    square_x = x + body_width * 0.15  # Сдвинуто немного для лучшего вида
    square_y = y + body_height * 0.2  # Немного ниже для центровки по высоте

    t.penup()
    t.goto(square_x, square_y)
    t.pendown()
    t.color("yellow")  # Заливка окна
    t.begin_fill()
    for _ in range(4):
        t.forward(square_window_size)
        t.left(90)
    t.end_fill()

    # Рисуем перекрёстие окна (рамы)
    t.color("white")  # Цвет рам
    t.pensize(2)  # Толщина рам
    # Горизонтальная линия
    t.penup()
    t.goto(square_x, square_y + square_window_size / 2)
    t.pendown()
    t.forward(square_window_size)
    # Вертикальная линия
    t.penup()
    t.goto(square_x + square_window_size / 2, square_y)
    t.pendown()
    t.setheading(90)
    t.forward(square_window_size)
    t.setheading(0)  # Возвращаем стандартное направление
    t.pensize(1)  # Возвращаем стандартную толщину пера

    # Дверь (коричневый прямоугольник, правее на теле дома)
    door_width = 35
    door_height = 60
    door_x = x + body_width * 0.9 - door_width  # Сдвинута правее
    door_y = y
    t.penup()
    t.goto(door_x, door_y)
    t.pendown()
    t.color("brown")
    t.begin_fill()
    for _ in range(2):
        t.forward(door_width)
        t.left(90)
        t.forward(door_height)
        t.left(90)
    t.end_fill()


# Функция для рисования дерева
def draw_tree(x, y):
    trunk_width = 20
    trunk_height = 70  # Уменьшил высоту ствола для пропорций
    # Ствол дерева
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("saddlebrown")
    t.begin_fill()
    for _ in range(2):
        t.forward(trunk_width)
        t.left(90)
        t.forward(trunk_height)
        t.left(90)
    t.end_fill()

    # Крона дерева (несколько кругов для объёма)
    crown_radius = 30
    t.color("forestgreen")  # Более темный зеленый для крон

    # Центральный круг кроны
    t.penup()
    t.goto(x + trunk_width / 2, y + trunk_height + crown_radius * 0.8)  # Центр первого круга
    t.pendown()
    t.begin_fill()
    t.circle(crown_radius)
    t.end_fill()

    # Левый круг кроны
    t.penup()
    t.goto(x + trunk_width / 2 - crown_radius * 0.7, y + trunk_height + crown_radius * 0.4)
    t.pendown()
    t.begin_fill()
    t.circle(crown_radius * 0.9)  # Чуть меньше
    t.end_fill()

    # Правый круг кроны
    t.penup()
    t.goto(x + trunk_width / 2 + crown_radius * 0.7, y + trunk_height + crown_radius * 0.4)
    t.pendown()
    t.begin_fill()
    t.circle(crown_radius * 0.9)  # Чуть меньше
    t.end_fill()


# Функция для рисования эллиптического пруда
def draw_oval(x_center, y_center, semi_major_axis, semi_minor_axis):
    t.penup()
    t.goto(x_center + semi_major_axis, y_center)  # Начальная точка на правом краю эллипса
    t.pendown()
    t.color("blue")
    t.begin_fill()
    original_speed = t.speed()
    if original_speed != "fastest": t.speed(0)  # Рисуем эллипс быстро

    for angle_deg in range(361):  # от 0 до 360 градусов для полного эллипса
        rad = math.radians(angle_deg)
        x_offset = semi_major_axis * math.cos(rad)
        y_offset = semi_minor_axis * math.sin(rad)
        t.goto(x_center + x_offset, y_center + y_offset)
    t.end_fill()
    if original_speed != "fastest": t.speed(original_speed)


def draw_pond(x, y, width_radius,
              height_radius):  # width_radius - горизонтальный полурадиус, height_radius - вертикальный
    draw_oval(x, y, width_radius, height_radius)


# ОБНОВЛЕННАЯ ФУНКЦИЯ ДЛЯ РИСОВАНИЯ УТКИ
def draw_duck(x_body_center, y_body_center):
    # Тело утки (желтый круг)
    body_radius = 12
    t.penup()
    t.goto(x_body_center, y_body_center - body_radius)  # Переходим к нижней точке тела для рисования круга
    t.pendown()
    t.color("yellow")
    t.begin_fill()
    t.circle(body_radius)
    t.end_fill()

    # Голова утки (меньший желтый круг)
    head_radius = 7
    # Центр головы смещен относительно центра тела
    head_center_x = x_body_center + body_radius * 0.2  # Голова чуть правее центра тела
    head_center_y = y_body_center + body_radius * 0.7  # Голова выше тела, немного перекрывая его

    t.penup()
    t.goto(head_center_x, head_center_y - head_radius)  # Переходим к нижней точке головы
    t.pendown()
    # t.color("yellow") # Цвет уже желтый
    t.begin_fill()
    t.circle(head_radius)
    t.end_fill()

    # Клюв (маленький оранжевый треугольник)
    beak_size = 6  # Размер клюва
    t.penup()
    # Начало клюва - на правой стороне головы
    beak_start_x = head_center_x + head_radius * 0.9
    beak_start_y = head_center_y + head_radius * 0.1  # Чуть выше центра головы по Y

    t.goto(beak_start_x, beak_start_y)
    t.pendown()
    t.color("orange")
    t.begin_fill()
    t.setheading(10)  # Направляем клюв немного вправо и вверх
    for _ in range(3):  # Рисуем равносторонний треугольник
        t.forward(beak_size)
        t.left(120)
    t.end_fill()
    t.setheading(0)  # Возвращаем стандартное направление

    # Глаз (маленькая черная точка на голове)
    eye_dot_size = 2.5
    # Позиция глаза на голове, ближе к клюву
    eye_x = head_center_x + head_radius * 0.4
    eye_y = head_center_y + head_radius * 0.3

    t.penup()
    t.goto(eye_x, eye_y)
    t.pendown()
    t.color("black")
    t.dot(eye_dot_size)


# ----- Основной участок рисования -----

draw_grass()
draw_sun(-280, 200, 40)  # Солнце левее и выше

draw_house(-250, -150)  # Домик левее и ниже

# Рисуем три дерева
draw_tree(80, -130)
draw_tree(150, -140)  # Деревья разной высоты для естественности
draw_tree(220, -130)

# Рисуем пруд с утками
# Пруд: центр (x=50, y=-180), горизонтальный полурадиус 130, вертикальный полурадиус 30
draw_pond(50, -230, 120, 40)  # Пруд чуть ниже и другой формы
# Утки (координаты x, y - это центр тела утки)
draw_duck(20, -225)  # Первая утка
draw_duck(70, -235)  # Вторая утка, чуть правее и ниже

screen.mainloop()  # Используем mainloop() для корректного завершения в некоторых средах