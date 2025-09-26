from tkinter.font import names


# ✅ What is a Class?
#
# A class is a blueprint for creating objects (instances).
# It defines attributes (variables) and methods (functions).
#When is self used?
# Inside class methods
#     To access or modify attributes and methods of the current object

class Person():
    def __init__(self, name, age):     # constructor
        self.name = name
        self.age = age

    def greet(self):   # Method
        print(f"Hello world, Welcome to Python classes world {self.name} and my age is {self.age}")


p1 = Person('Jitendra', '35')
p1.greet()


# ✅ What is an Object?
#
# An object is an instance of a class.
#
# p1 = Person("Alice", 25)
# p1.greet()
# # Output: Hello, I'm Alice and I'm 25 years old.
# What is __init__?
#it’s the constructor method in Python.
# It runs automatically when you create a new object and is used to initialize attributes.


# 🔹 Inheritance & Polymorphism
# Inheritance lets you create a new class (child) that reuses code from an existing class (parent).
# This means:
#
# - Less repetition
# - Better code organization
# - Easy extensions to functionality

class Animal():
    def __init__(self, name):
        self.name =name

    def speak(self):
        print(f'{self.name} is speaking as Animal sound')


class Dog(Animal): # Inheritane to Animal class
    def speak(self):
        print(f"{self.name} says Woof!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says meow!")


d = Dog('Puppy')
c = Cat('Pussy')
d.speak()
c.speak()



# What is Polymorphism?
#Polymorphism means different objects can use the same method name, but behave differently.

# In the example above, Dog and Cat both have a speak() method, but each produces a different output.


class Character:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def attack(self):
        print(f"{self.name} attacks with a basic strike.")

class Warrior(Character):
    def attack(self):
        print(f"{self.name} swings a sword with strength level {self.level}!")

class Mage(Character):
    def attack(self):
        print(f"{self.name} casts a fireball with power level {self.level}!")

# Usage
c1 = Warrior("Thor", 5)
c2 = Mage("Merlin", 7)

c1.attack()  # Thor swings a sword with strength level 5!
c2.attack()



# Dunder (Magic) Methods in Python

# Let’s dive into the world of Python’s dunder methods — the ones surrounded by double underscores (_like_this_)!
#
# 🔍 What are Dunder Methods?
# Dunder (Double UNDERscore) methods are special methods in Python that let you define how objects behave with built-in functions and operators.
#
# ✨ Examples:
# - _init_() → Object initialization
# - _str_() → String representation
# - _len_() → Length using len()
# - _add_() → + operator behavior
# - _eq_() → == comparison

# 🧠 Why Use Them?
# They make your class behave like built-in types (e.g., str, list, etc.)


class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"{self.title} has {self.pages} pages"

    def __len__(self):
        return self.pages

book1 = Book("Python Basics", 300)
print(book1.title)        # Python Basics has 300 pages
print(len(book1))       # 300





