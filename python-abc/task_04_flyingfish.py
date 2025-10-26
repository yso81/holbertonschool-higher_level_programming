#!/usr/bin/python3
class Fish:
    """
    Represents a fish with methods for swimming and defining its habitat
    """
    def swim(self):
        """
        Prints a message indicating the fish is swimming
        """
        print("The fish is swimming")

    def habitat(self):
        """
        Prints a message defining the fish's habitat
        """
        print("The fish lives in water")

class Bird:
    """
    Represents a bird with methods for flying and defining its habitat
    """
    def fly(self):
        """
        Prints a message indicating the bird is flying
        """
        print("The bird is flying")

    def habitat(self):
        """
        Prints a message defining the bird's habitat
        """
        print("The bird lives in the sky")

class FlyingFish(Fish, Bird):
    """
    Represents a magical flying fish, inheriting from both Fish and Bird
    This class demonstrates multiple inheritance and method overriding
    """
    def fly(self):
        """
        Overrides the fly method to describe the flying fish's unique flight
        """
        print("The flying fish is soaring!")

    def swim(self):
        """
        Overrides the swim method to describe the flying fish's unique swimming
        """
        print("The flying fish is swimming!")

    def habitat(self):
        """
        Overrides the habitat method to describe the flying fish's dual habitat
        """
        print("The flying fish lives both in water and the sky!")


if __name__ == "__main__":
    flying_fish = FlyingFish()

    flying_fish.swim()
    flying_fish.fly()
    flying_fish.habitat()

    print("MRO method:", FlyingFish.mro())
    print("MRO using __mro__ attribute:", FlyingFish.__mro__)
