# Assignment 1: Superhero Class with Inheritance
class Superhero:
    def __init__(self, name, power, energy_level=100):
        self.__name = name  
        self.__power = power
        self.__energy_level = energy_level

    def use_power(self):
        if self.__energy_level >= 10:
            self.__energy_level -= 10
            return f"{self.__name} uses {self.__power}! Energy level: {self.__energy_level}%"
        return f"{self.__name} is too tired to use {self.__power}."

    def rest(self):
        self.__energy_level = min(100, self.__energy_level + 20)
        return f"{self.__name} rests. Energy level restored to {self.__energy_level}%."

    def get_name(self):
        return self.__name

    def get_energy_level(self):
        return self.__energy_level

class FlyingSuperhero(Superhero):
    def __init__(self, name, power, max_altitude, energy_level=100):
        super().__init__(name, power, energy_level)
        self.__max_altitude = max_altitude  

    def fly(self):
        if self.get_energy_level() >= 15:
            self._Superhero__energy_level -= 15  
            return f"{self.get_name()} soars to {self.__max_altitude} feet!"
        return f"{self.get_name()} is too tired  to fly."
class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        return f"{self.name} is moving."

class Dog(Animal):
    def move(self):
        return f"{self.name} is running on four legs! 🐶"

class Bird(Animal):
    def move(self):
        return f"{self.name} is flying in the sky! 🐦"


if __name__ == "__main__":
    
    print("=== Assignment 1: Superhero ===")
    hero = Superhero("Captain Thunder", "Lightning Strike")
    print(hero.use_power())  
    print(hero.rest())    
    flying_hero = FlyingSuperhero("Sky Blazer", "Wind Blast", 10000)
    print(flying_hero.use_power())  
    print(flying_hero.fly())        

    
    print("\n=== Activity 2: Polymorphism Challenge ===")
    dog = Dog("Rex")
    bird = Bird("Tweety")
    animals = [dog, bird]
    for animal in animals:
        print(animal.move()) 