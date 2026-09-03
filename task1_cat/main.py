class Cat:
    def __init__(self, breed, name, age):
        self.breed = breed
        self.name = name
        self.age = age

    def info(self):
        print(f"Кот: {self.name}")
        print(f"Порода: {self.breed}")
        print(f"Возраст: {self.age} лет")
        print("-" * 25)


cat1 = Cat("Бурма", "Васька", 3)
cat2 = Cat("Саванна", "Красик", 5)
cat3 = Cat("Русская рыжая", "Рыжик", 2)

cat1.info()
cat2.info()
cat3.info()
