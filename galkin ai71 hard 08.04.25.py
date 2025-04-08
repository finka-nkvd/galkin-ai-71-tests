from abc import ABC, abstractmethod
# 1 задача
class Animal:
    @staticmethod
    def make_sound():
        print(f'Животное издает звук')


class Dog(Animal):
    @staticmethod
    def make_sound():
        print(f'Собака издает звук')


class Cat(Animal):
    @staticmethod
    def make_sound():
        print(f'Кот издает звук')


# 2 задача
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, value):
        if value > 0:
            self.__balance = value

    def withdraw(self, value):
        if value <= self.__balance:
            self.__balance -= value

    def get_balance(self):
        print(self.__balance)


# 3 задача
class Shape:
    @abstractmethod
    def area(self):
        pass
    

class Rect(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
