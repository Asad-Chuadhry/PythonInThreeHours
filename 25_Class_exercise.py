class Person:
    def __init__(self, name=""):
        self.name = name

    def talk(self):
        print(f"Hi i am {self.name} .")


person = Person("Asad")
print(person.name)
person.talk()