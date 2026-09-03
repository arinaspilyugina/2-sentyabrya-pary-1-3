from math import pi


class Figure:
    def __init__(self, coords):
        self._coords = coords

    def get_coords(self):
        return self._coords

    def set_coords(self, coords):
        self._coords = coords

    def calculate_area(self):
        raise NotImplementedError(
            "Метод calculate_area() должен быть реализован в дочернем классе."
        )


class Circle(Figure):
    def __init__(self, coords, radius):
        super().__init__(coords)
        self.radius = radius

    def calculate_area(self):
        return pi * self.radius ** 2


class Square(Figure):
    def __init__(self, coords, side):
        super().__init__(coords)
        self.side = side

    def calculate_area(self):
        return self.side ** 2


figures = [
    Circle((0, 0), 3),
    Square((2, 4), 5),
    Circle((8, 1), 2),
    Square((10, 6), 4),
    Circle((3, 7), 1)
]

figures[0].set_coords((1, 1))

total_area = 0

for figure in figures:
    area = figure.calculate_area()
    total_area += area

    print(
        f"{figure.__class__.__name__}: "
        f"координаты {figure.get_coords()}, "
        f"площадь = {area:.2f}"
    )

print(f"\nОбщая площадь всех фигур: {total_area:.2f}")
