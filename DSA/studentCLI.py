
#student profilr command line interface
student_id=""
name=""
age=""
course=""
while True:
    print("Student profile menu")
    print("1. Add student")
    print("2.View student")
    print("3.Update student")
    print("4.Delete student")
    choice=input("Enter the choice:")
    if choice=='1':
        student_id=input("Enter student id: ")
        name=input("Enter name: ")
        age=int(input("Enter age: "))
        course=input("Enter course: ")
        print("Student added successfully")
    
    elif choice=='2':
        if student_id=="":
            print("No data found")
        else:
            print("Student details")
            print("id ",student_id)
            print("name ",name)
            print("age ",age)
            print("course ",course)
    elif choice=='3':
        if student_id=="":
            print("No data found")
        else:
            student_id=input("Enter student id: ")
            name=input("Enter name: ")
            age=int(input("Enter age: "))
            course=input("Enter course: ")
            print("Student updated successfully")
    elif choice=='4':
        if student_id=="":
            print("No data found")
        else:
            student_id=""
            name=""
            age=""
            course=""
            print("Student deleted")
    elif choice=='5':
        print("program exit")
        break
    else:
        print("invalid choice")
            
