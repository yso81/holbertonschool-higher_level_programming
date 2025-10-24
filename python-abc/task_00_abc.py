#!/usr/bin/python3
import abc

class Animal(abc.ABC):
    @abc.abstractmethod
    def sound(self):
        """
        Abstract that defines the sound made by the animal
        """
        pass

class Dog(Animal):
    """
    Implementing the dog subclass with sound method
    """
    def sound(self):
        return "Bark"

class Cat(Animal):
    """
    Implementing the cat subclass with sound method
    """
    def sound(self):
        return "Meow"


if __name__ == "__main__":

    try:
        """
        Instantiating abstract class Animal will raise a TypeError
        """
        animal = Animal()
    except TypeError as e:
        print(f"ZError: {e}")


    """
    Instantiating subclasses Dog and Cat
    """
    dog = Dog()
    cat = Cat()


    """
    Printing the sound method on the instances
    """
    print(f"Dog makes: {dog.sound()}")
    print(f"Cat makes: {cat.sound()}")


    """
    Polymorphism
    """
    animals = [Dog(), Cat()]
    for animal in animals:
        print(f"Animal makes : {animal.sound()}")
