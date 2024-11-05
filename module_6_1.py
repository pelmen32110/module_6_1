# Животные
class Animal:
    alive = True
    fed = False

    def eat(self, food):  # food - это параметр, принимающий объекты классов растений.
        if food.edible:
            print(f'{self.name} съел {food.name}')
            Animal.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            Animal.alive = False

class Mammal(Animal):

    def __init__(self,name):
        self.name = name

class Predator(Animal):

    def __init__(self,name):
        self.name = name


# Растения
class Plant:
    edible = False

class Flower(Plant):

    def __init__(self, name):
        self.name = name

class Fruit(Plant):
    edible = True

    def __init__(self, name):
        self.name = name



a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')


print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)