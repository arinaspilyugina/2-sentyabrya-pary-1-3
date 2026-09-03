class Car:
    def __init__(self):
        self._engine_temperature = 20

    def start_engine(self):
        self._engine_temperature = 90
        print("Двигатель прогрет")

    def drive(self):
        if self._engine_temperature >= 90:
            print("Поехали!")
        else:
            print("Нельзя ехать: двигатель ещё не прогрет.")


car = Car()

print("Попытка узнать температуру напрямую:")
print(car._engine_temperature)

print("\nПопытка поехать без прогрева:")
car.drive()

print("\nПрогрев двигателя:")
car.start_engine()

print("\nПопытка поехать после прогрева:")
car.drive()
