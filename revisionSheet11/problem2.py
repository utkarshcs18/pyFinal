class Animal:
    def show(self):
        print("This is Animal.. Class")

class Pets(Animal):
    def show(self):
        print("This is Pets.. Class")

class Dog(Pets):
    def bark(self):
        print("Dog is Barking... WOOF ")


a = Dog()
a.show()
a.bark()