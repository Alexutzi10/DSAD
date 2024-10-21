class Animal():
    def __init__(self, name, age):     #self = this in C++ / practic atribui campuri odata cu constructorul
        self.name = name
        self.age = age
    
    def speak(self):
        print("I am an animal")

class Dog (Animal):
    def speak(self):
        print("Ham ham")

    def moves(self):
        print("Runs")


animal1 = Animal("Rex", 5)
# print(animal1.name)

dog1 = Dog("Buddy", 3, "Golden Retriever")
print(dog1.speak())