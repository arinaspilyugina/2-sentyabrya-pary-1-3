class Cat:
    def __init__(self, breed, name, age):
        self.breed = breed
        self.name = name
        self.age = age

    def draw(self):
        print(f"На экране рисуется кот {self.name}, порода {self.breed}.")


cat1 = Cat("Бурма", "Васька", 3)
cat2 = Cat("Саванна", "Красик", 5)
cat3 = Cat("Русская рыжая", "Рыжик", 2)

cat1.draw()
cat2.draw()
cat3.draw()
