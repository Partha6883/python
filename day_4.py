# class student:
#     name = "penga"
#     def study(self):
#         print("penga is studying")
# s1=student()
# print(s1.name)
# s1.study()


# class student:
#     def details(self):
#         print("had breakfast")
# s1=student()
# s1.details()            #1
# student.details(s1)     #2

# class student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# e1 = student("Haaland",21)
# e2 = student("Messi",21)
# e3 = student("Ronaldo",21)
# print(e1.name)
# print(e1.age)
# print(e2.name)
# print(e2.age)
# print(e3.name)
# print(e3.age)

# class student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# e1 = student("Odheykeran",21)
# e2 = student("ArgentMessi",21)
# e3 = student("Naroda",21)
# print(e1.name,e1.age,
#       e2.name,e2.age,
#       e3.name,e3.age )

# class bank:
#     def __init__(self,balance):
#         self.balance = balance

#     def check_balance(self):
#         print(self.balance)

# acc=bank(5000)
# acc.check_balance()

# class user:
#     def __init__(self,name):
#         self.name = name
#     def login(self):
#         print(self.name,'logged in')

# u1=user("kabaddi Player")
# u2=user("Kirmada")
# u3=user("Susmitha")
# u1.login()
# u2.login()
# u3.login()

# class user:
#     def __init__(self,name):
#         self.name = name
#     def login(self):
#         print(self.name,'logged in')

# u1=user("Madhumita")
# u2=user("Thusmita")
# u3=user("Sushmitha")
# u1.login()
# u2.login()
# u3.login()

# class dad:
#     print("Daddy is coming.....")

# class son(dad):
#     print(")));  My son")

# class class son2(son):
#     print(".......Run to home")

# class appa:
#     def house(self):
#         print("Father has bike")

# class magga(appa):
#     def bike(self):
#         print("Magga too has bike")
# m=magga()
# m.house()
# m.bike()
        
# class grandpa:
#     def land(self):
#         print("Grandpa's land")

# class Daddy(grandpa):
#     def house(self):
#         print("Daddy's home")

# class son(Daddy):
#     def bike(self):
#         print("Son has a bike")

# obj=son()
# obj.land()
# obj.house()
# obj.bike()

# class dad:
#     def house(self):
#         print("Dad")
# class mom:
#     def home(self):
#         print("Mom")
# class son(dad,mom):
#     def shelter(self):
#         print("Dad and mom")

# o=son()
# o.house()
# o.home()
# o.shelter()

# class college:
#     def classA(self):
#         print("ISE Main Branch")

# class son(college):
#     def classB(self):
#         print("ISE 2")

# class daughter(college):
#     def classC(self):
#         print("ISE 3")

# d=daughter()
# d.classA()
# e=son()
# e.classA()

# class student:
#     def __init__(self,name):
#         self.name = name

#     def __str__(self):
#         return self.name

# s=student("Raja Rani")
# print(s)

# import calsc

# from calsc import add

# print(add(10,20))

# import calsc as cl
# print(cl.add(6,6))

# import math
# print(math.sqrt(512))

# import random
# n=random.randint(1,1000000000000)
# print(n)

# def login(func):
#     def wrapper():
#         print("Checking login")
#         func()
#     return wrapper
# @login
# def dashboard():
#     print("Dashboard page")
# dashboard()

def message(func):
    def wrapper():
        print("function started")
        func()
        print("function ended")
    return wrapper

# def hi():
#     print("Let's code")

# def code():
#     print("what's next")
    
# @message
# def hello():
#     print("Hello python")
#     hi()
#     code()

# hello()

# import json
# student={
#     "Name" : "KonKa",
#     "Age" : 100
# }
# data=json.dumps(student)
# print(data)

# import json

# data='{"Name": "KonKa", "Age": 123}'
# result = json.loads(data)
# print(result["Name"])
# print(result["Age"])

# import requests
# response = requests.get(
#     "https://api.github.com/users/python"
#     )
# data=response.json()
# print(data)

# import requests

# response = requests.get("https://api.github.com/users/python")

# print(response)
# print(response.status_code)
# print(response.json())





