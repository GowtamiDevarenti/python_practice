# -*- coding: utf-8 -*-
"""Untitled82.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1F0Yek4Db_APPbXgVGYaKA8uEmIdvhaVK

## Class Variables
In Python, class variables are variables that are shared by all instances of a class. They are defined within the class, but outside of any methods or constructors. Class variables are associated with the class itself rather than with specific instances of the class.

## Class Methods
In Python, a class method is a special type of method that is bound to the class rather than an instance of the class. It is defined using the @classmethod decorator, followed by a function definition within the class. Class methods have access to the class itself as the first parameter, conventionally named cls, instead of the instance (self) that is used in regular methods.
"""

class MyClass:
    class_variable = 10

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

# Accessing class variables
print(MyClass.class_variable)  # Output: 10

# Creating instances of the class
obj1 = MyClass(20)
obj2 = MyClass(30)

# Accessing instance variables
print(obj1.instance_variable)  # Output: 20
print(obj2.instance_variable)  # Output: 30

# Modifying class variable
MyClass.class_variable = 15

# Class variable is shared by all instances
print(obj1.class_variable)  # Output: 15
print(obj2.class_variable)  # Output: 15

"""## Static Methods
In Python, a static method is a method that belongs to a class but doesn't have access to the class itself (via self) or its instances. Static methods are defined using the @staticmethod decorator and are typically used when a method doesn't require access to instance-specific data or class-specific data.

Static methods are often used when you have a utility function or a method that doesn't depend on the state of a specific instance or the class itself. They are self-contained and don't have access to instance variables or class variables unless they are explicitly passed as arguments.

It's important to note that static methods don't have the ability to modify the state of the instance or the class. They are independent of any specific instance and can be called without creating an instance of the class.


"""

class MyClass:
    class_variable = 10

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    @staticmethod
    def static_method():
        print("This is a static method.")

# Calling the static method
MyClass.static_method()

class MathUtils:
    @staticmethod
    def multiply(x, y):
        return x * y

result = MathUtils.multiply(5, 3)
print(result)  # Output: 15

class Employee:
  company_name="iNeuron" ##class variable

  def __init__(self,first_name,last_name):
    self.firstname=first_name #instance variables
    self.lastname=last_name

  ## class method
  @classmethod
  def change_company(cls,company_name):
    cls.company_name=company_name

person1=Employee("Krish","Naik")

person1.company_name

Employee.change_company("PWSKILLS")

person1.company_name

Employee.company_name

class Car:
  base_price=100000 ##class variable ## 2023 ##global access to all the instance variables

  def __init__(self,model,brand):
    self.model=model
    self.brand=brand

  def display_price(self):
    print(f"The base price is {self.base_price}")

  @classmethod
  def update_base_price(cls,inflation):
    cls.base_price=cls.base_price+ (cls.base_price *(inflation/100))

car1=Car("BMW","EV")
car1.display_price()

## 2024

Car.base_price

Car.update_base_price(10)

Car.base_price

car1.base_price

class BMW:
  base_price=100000

  def __init__(self,model):
    self.model=model

  def total_price(self):
    if self.model=="EV":
      ##functionality to calculate the price of the car

      pass

  @classmethod
  def update_base_price(cls):
    ##update thie base price

    pass

class Car:
  base_price=100000 ##class variable ## 2023 ##global access to all the instance variables

  def __init__(self,model,brand):
    self.model=model
    self.brand=brand

  def display_price(self):
    print(f"The base price is {self.base_price}")

  @classmethod
  def update_base_price(cls,inflation):
    cls.base_price=cls.base_price+ (cls.base_price *(inflation/100))

  #utility method
  @staticmethod
  def display_base_price():
    print(Car.base_price)

Car.display_base_price()







