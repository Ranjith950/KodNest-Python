marks=int(input("enter the marks:"))
attendance=int(input("enter the attendance:"))
project_status=(input("enter the project_status:"))
if marks>=60 and attendance>=75:
    if project_status=="yes":
        print("eligible")
    else:
        print("not eligible")
else:
    print("not eligible")