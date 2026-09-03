class Figure:
    def __init__(self, coords, width, color):
        self.coords = coords
        self.width = width
        self.color = color


figure = Figure((10, 20), 3, "красный")

print(f"Координаты: {figure.coords}")
print(f"Ширина: {figure.width}")
print(f"Цвет: {figure.color}")
