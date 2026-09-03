class Figure:
    def __init__(self, coords, width, color):
        self.coords = coords
        self.width = width
        self.color = color

    def draw(self):
        print("Рисуется фигура.")


class Line(Figure):
    def __init__(self, coords, width, color, length):
        super().__init__(coords, width, color)
        self.length = length

    def draw(self):
        print(
            f"Рисуется линия: длина {self.length}, "
            f"цвет {self.color}, координаты {self.coords}."
        )


class Rect(Figure):
    def __init__(self, coords, width, color, height):
        super().__init__(coords, width, color)
        self.height = height

    def draw(self):
        print(
            f"Рисуется прямоугольник: ширина {self.width}, "
            f"высота {self.height}, цвет {self.color}."
        )


class Ellipse(Figure):
    def __init__(self, coords, width, color, radius):
        super().__init__(coords, width, color)
        self.radius = radius

    def draw(self):
        print(
            f"Рисуется эллипс: радиус {self.radius}, "
            f"цвет {self.color}, координаты {self.coords}."
        )


figures = [
    Line((0, 0), 2, "синий", 15),
    Rect((10, 10), 4, "зелёный", 8),
    Ellipse((5, 5), 3, "жёлтый", 6)
]

for figure in figures:
    figure.draw()
