'''Encapsulation means wrapping variables and methods 
Together inside a class and controlling access of the data'''

'''Without encapsulation'''

# class bank:
#     def __init__(self):
#         self.balance=10000
# account = bank()
# account.balance=10000000
# print(account.balance)

'''With encapsulation'''

# class bank:
#     def __init__(self):
#         self.__balance = 10000
#     def deposit(self,amount):
#         self.__balance += amount
#     def show_balance(self):
#         print(self.__balance)
# account = bank()
# account.deposit(50000)
# account.show_balance()

'''gettter'''

# class employee:
#     def __init__(self,salary):
#         self.__salary = salary

#     def get_salary(self):
#         return self.__salary
    
# emp = employee(52436)
# print(emp.get_salary())

'''setter'''

# class employee:
#     def __init__(self):
#         self.__salary = 0
    
#     def set_salary(self,amount):
#         if amount > 0:
#             self.__salary = amount
#         else:
#             print("Invalid salary")

#     def get_salary(self):
#         return self.__salary

# emp = employee()
# emp.set_salary(98752)
# print(emp.get_salary())

'''Polymorsphism means the same method name can perform 
Different action depending on the object'''

# class dog:
#     def sound(self):
#         print("Dog barks")

# class cat:
#     def sound(self):
#         print("Cat meows")

# D=dog()
# C=cat()
# D.sound()
# C.sound()

# class Credit_card:
#     print("______Choose the payment______")
#     def m1(self):
#         print("Pay through Credit Card")

# class UPI:
#     def m1(self):
#         print("Pay through UPI_ID")

# class Cash:
#     def m1(self):
#         print("Pay through cash")

# A=Credit_card()
# B=UPI()
# C=Cash()
# A.m1()
# B.m1()
# C.m1()

'''Abstraction'''

'''Abstraction means hiding internal implementation and 
   showing only necessary feature to the user'''

# from abc import ABC ,abstractmethod
# class vehicle(ABC):
#     @abstractmethod
#     def start(self):
#         pass

# class car(vehicle):
#     def start(self):
#         print("Car started")

# car = car()
# car.start()

# from abc import ABC ,abstractmethod

# class Animals(ABC):
#     @abstractmethod
#     def food(self):
#         pass

# class monkey(Animals):
#     def food(self):
#         print("Monkey Eats Banana")

# class donkey(Animals):
#     def food(self):
#         print("Donkey Eats Grass")

# class cow(Animals):
#     def food(self):
#         print("Cow Eats Millets")

# m=monkey()
# d=donkey()
# c=cow()
# m.food()
# d.food()
# c.food()






