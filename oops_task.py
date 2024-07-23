'''
1) Write a Python program to create a person class. Include  attributes like name, country and date of birth. Implement a method to determine the person's age.

'''
class Person:
    def __init__(self,name,country,d_o_b):
        self.name = name
        self.country = country
        self.d_o_b = d_o_b
    def calculate_age(self,current_year):
        age = current_year - self.d_o_b
        return age

person = Person("sakthi","india",1999)
age = person.calculate_age(2024)
print(f"person name is:{person.name} \nperson country is:{person.country}\nperson d.o.b is:{person.d_o_b}\nperson age is :{age}")

#date time - module import
from datetime import  date
class Person1:
    def __init__(self,name,country,d_o_b):
        self.name = name
        self.country = country
        self.d_o_b = d_o_b

    def cal_age(self):
        today = date.today()
        age = today.year - self.d_o_b
        return  age
        #if today < date(today.year,self.d_o_b)

person1 = Person1("sakthii","indiaa",1999)
print(person1.name)
print(person1.country)
print(person1.d_o_b)
print(person1.cal_age())






"""
2) Write a Python program to create a calculator class. Include methods for basic arithmetic operations.( Addition, Subtraction, Multiplication,  Division )
"""
class Calculator:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        if b!=0:
            return a/b
        else:
            return  "Error divisible by 0"

cal =Calculator()
print(cal.add(2,5))
print(cal.sub(10,5))
print(cal.mul(2,2))
print(cal.div(10,5))

"""
3) Create a child class Bus that will inherit all of the variables and methods of the Vehicle class(Parent class)

"""
class Variables:
    def __init__(self,speed,year):
        self.s = speed
        self.y = year
class Bus(Variables):
    def __init__(self,speed,year,capacity):
        super().__init__(speed,year)
        self.c = capacity

bus = Bus(100,2016,70)
print(bus.s)
print(bus.y)
print(bus.c)

"""
4)Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.

"""
class Variables:
    def __init__(self,speed,year):
        self.s = speed
        self.y = year
class Bus(Variables):
    def seating_capacity(self,capasity=50):
        return capasity

bus = Bus(80,2020)
print(bus.s)
print(bus.y)
print(bus.seating_capacity())

"""
5)Create a Zoosystem class without any variables
 and methods

"""
class Zoosystem:
    pass

"""
6)Create a Vehicle class with max_speed and year instance attributes

"""
class Vehicle:
    def __init__(self,max_speed,year):
        self.max_speed = max_speed
        self.year = year
    def show(self):
        print(f"your vehicle speed is:{self.max_speed}, and the model of the year is:{self.year}")

vehicle = Vehicle(120,2018)
vehicle.show()


"""
7)Write a  Python class named Student with two attributes student_name, marks. Modify the attribute values of the said class and print the original and modified values of the said attributes
"""
class Student:
    def __init__(self,student_name,marks):
        self.s = student_name
        self.m = marks

student = Student("sakthi",98)
print("original values are:")
print(student.s)
print(student.m)

student.s= "spidy"
student.m = 99
print("modified values:")
print(student.s)
print(student.m)





"""
8) Define a class Person with private attributes name and age. Provide public methods to get and set the values of these attributes(Use getter and setter)

"""
class Person:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name = name

    def get_age(self):
        return self.__age
    def set_age(self,age):
        self.__age = age

person = Person("sakthi",24)
print(person.get_name())
print(person.get_age())

person.set_name("sowmi")
person.set_age(22)
print(person.get_name())
print(person.get_age())

"""
9)Create an abstract base class BankAccount with abstract methods deposit, withdraw, and get_balance. Implement these methods in a subclass SavingsAccount.

"""
from abc import ABC, abstractmethod

class Bank_Account(ABC):
    @abstractmethod
    def deposit(self,amnt):
        pass

    @abstractmethod
    def withdraw(self,amnt):
        pass
    @abstractmethod
    def get_bal(self):
        pass

class Savings_Account(Bank_Account):
    def __init__(self,bal):
        self.bal = 0

    def deposit(self,amnt):
        self.bal += amnt
        return  f"your deposit amount is: {amnt} and your balance is:{self.bal}"
    def withdraw(self,amnt):
        if self.bal >= amnt:
            self.bal -=amnt
            return  f"your withdraw amount is: {amnt} and the balance amount is: {self.bal}"
        else:
            print("Insufficient balance")

    def get_bal(self):
        return f"your bal is :{self.bal}"

savings = Savings_Account(1000)
print(savings.deposit(10000000))
print(savings.withdraw(1000))
print(savings.get_bal())

"""
10)Define an abstract base class Payment with an abstract method pay. Create two subclasses CreditCardPayment and PayPalPayment that implement the pay method.
"""
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self,amnt):
        pass

class CreditCardPayment(Payment):
    def pay(self,amnt):
        return f"paying {amnt} with credit card"
class PayPalPayment(Payment):
    def pay(self,amnt):
        return f"paying {amnt} with paypal account"
ccp = CreditCardPayment()
print(ccp.pay(1000))
ppp = PayPalPayment()
print(ppp.pay(100000))












