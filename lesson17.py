class Animal(object):
    def run(self):
        print('Animal is running!')


class Dog(Animal):
    def run(self):
        print('Dog is running!')

    def eat(self):
        print('Eating meat...')
    pass


class Cat(Animal):
    pass


dog = Dog()
dog.run()
dog.eat()

print(isinstance(dog, Dog))


def run_twice(animal):
    animal.run()
    animal.run()


run_twice(dog)

print(dir(dog))