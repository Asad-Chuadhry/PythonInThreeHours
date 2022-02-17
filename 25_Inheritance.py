class Mammal: # parent class
    def walk(self):
        print("Walk...")


class Dog(Mammal): # child class 1
    pass # pass keyword is used to pass or ignore a statement bloc


class Cat(Mammal): # child class 2
    def Meow(self):
        print("Meoww..")


dog1 = Dog()
dog1.walk()
cat1 = Cat()
cat1.Meow()
cat1.walk()