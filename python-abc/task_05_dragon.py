#!/usr/bin/python3

class SwimMixin:
    """
    A mixin class providing swimming capability
    """
    def swim(self):
        """
        Prints a message indicating the creature is swimming
        """
        print("The creature swims!")

class FlyMixin:
    """
    A mixin class providing flying capability
    """
    def fly(self):
        """
        Prints a message indicating the creature is flying
        """
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    """
    A Dragon class that inherits swimming and flying abilities from mixins
    """
    def roar(self):
        """
        Prints a message indicating the dragon is roaring
        """
        print(f"The dragon roars!")


if __name__ == "__main__":

    draco = Dragon()
    draco.swim()
    draco.fly()
    draco.roar()

    print("MRO using mro() method:", Dragon.mro())
    print("Dragon MRO attribute:", Dragon.__mro__)
