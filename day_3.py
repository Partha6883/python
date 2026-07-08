# # students = ("Ram","Sai","Nitu")
# # print(students[-1])

# # num =(10,20,30,40)
# # print(num[-3])

# # data =(1,2,3)
# # print(data[2])

# # Arr=["Sita","Aita","Mita"]
# # print(Arr)
# # for Arr[0] in range(10) :
# #     print(Arr)


# # null = input("*,*,*,*,*,*,*,*,*,* ")
# # for i in null():
# #     for j in null():
# #         i=j
# #         null+=1
# #         null=[0]
# #         print(" ")
# # x= (1,2,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,null)
# # print(x.count(null))

# # A = ("R","A","M","R")
# # print(A.count("R"))

# # num  =(10,20,30,40,50)
# # print(num[1:4]) 

# # x= {1,2,3,5,5,}
# # print(x)

# # data= {1,2,3}
# # data.add(4)
# # print(data)

# a = {1,2,3}
# b= {3,4,5}
# print(a&b)

# def sagar():
#     print("Sagar is a Student")
#     sagar()

# def d(*n):
#     print(n)
# d(10,20,30,40,50,60)

# def add(*n):
#     total = 0
#     for i in n:
#         total+= i
#     print(total)
# add(10,20,30,40,50,60,70,80,90,100)

# def student(**deatails):
#     print("name:",deatails["name"])
# student(
#     name="Jony"
# )

# math= 25 ** 0.5
# print(math)

# def sq(x):
#     return x*x
# print(sq(6))

# sq = lambda x:x*x
# print(sq(100))

# add = lambda a,b:a+b
# print(add(10,20))

# thima = lambda x:"even" if x%2 ==0 else "odd"
# print(thima(18))
# print(thima(2))

# n="Keerthan"
# print(n.upper())
# print(n.lower())

# file=open("student.txt","w")
# file.write("Annoooo sak annoooo.....")
# file.close()

# print("Done")

# file=open("student.txt","r")
# data = file.read()
# print(data)
# file.close()

# file=open("student.txt","a")
# file.write("Annoooo sak annoooo.....")
# file.close()

# print("Done")


# file=open("student.txt","r")
# print(file.read())
# file.close()

# try:
#     a=10
#     b=0
#     print(a/b)
# except:
#     print("Naa bro..learn basics")          

# try:
#     n=int(input("enter n:"))
#     print(n)
# except ValueError:
#     print("only number allowed!"

# try:
#     a=int(input("Enter a:"))
#     b=int(input("Enter b:"))
#     print(a/b)
# except ValueError:
#     print("******")
# except ZeroDivisionError:
#     print("only nos")

# try:
#     file=open("student.txt")
#     print(file.read())
# except:
#     print("file error")
# finally:
#     print("Program completed")