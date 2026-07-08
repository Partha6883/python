students =[]
while True :
    print("""
    1.Add students
    2.View students
    3.Seach students
    4.Exit
    """)
    choice=input("Enter Option:")
    if choice == "1":
        Name=input("name")
        age=input("age")
        course=input("course:")

        student={
            "name":Name,
            "age":age,
            "course":course
        }

        students.append(student)
        print("student added successfully")

    elif choice =="2":
        for student in students:
            print(student)
    elif choice == "3":
        search = input("enter name:")
        for student in students:
            if student["name"]==search:
                print(student)
            else :
                print("Student doesnt Exists")
    elif choice == "4":
        print("Exiting.......")
        break
    else :
        print ("Wrong option")


