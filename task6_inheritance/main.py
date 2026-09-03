class Figure:
    def __init__(self, coords, width, color):
        self.coords = coords
        self.width = width
        self.color = color


class Line(Figure):
    def __init__(self, coords, width, color, length):
        super().__init__(coords, width, color)
        self.length = length


class Rect(Figure):
    def __init__(self, coords, width, color, height):
        super().__init__(coords, width, color)
        self.height = height


class Ellipse(Figure):
    def __init__(self, coords, width, color, radius):
        super().__init__(coords, width, color)
        self.radius = radius


line = Line((0, 0), 2, "синий", 15)
rect = Rect((10, 10), 4, "зелёный", 8)
ellipse = Ellipse((5, 5), 3, "жёлтый", 6)

print("Линия:", vars(line))
print("Прямоугольник:", vars(rect))
print("Эллипс:", vars(ellipse))
