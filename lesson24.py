class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__(self, name: str, number_of_floors: int):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')


h1 = House("hightower", 10)
print(House.houses_history)
h2 = House("warehouse", 5)
print(House.houses_history)
h3 = House("building", 20)
print(House.houses_history)


del h2 # удаление
del h3

print(House.houses_history)