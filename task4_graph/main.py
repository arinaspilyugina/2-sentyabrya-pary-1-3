class Graph:
    def __init__(self, x=0, y=0, scale=1):
        self._x = x
        self._y = y
        self._scale = scale

    def move(self, dx, dy):
        self._x += dx
        self._y += dy

    def change_scale(self, factor):
        if factor > 0:
            self._scale *= factor
        else:
            print("Масштаб должен изменяться на положительное число.")

    def show_state(self):
        print(f"x = {self._x}, y = {self._y}, scale = {self._scale}")


graph1 = Graph()
graph2 = Graph(10, 5, 1)
graph3 = Graph(-3, 7, 2)

graph1.move(4, -2)
graph2.change_scale(1.5)

print("Первый график:")
graph1.show_state()

print("Второй график:")
graph2.show_state()

print("Третий график:")
graph3.show_state()
