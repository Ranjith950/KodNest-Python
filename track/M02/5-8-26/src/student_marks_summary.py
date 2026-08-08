student_count=int(input("enter the number of students:"))
total_marks=0
passed_count=0
failed_count=0
for i in range(student_count):
    marks=int(input("enter the marks:"))
    total_marks+=marks
    if marks>=40:
        passed_count+=1
    else:
        failed_count+=1
print("total marks",total_marks)
print("passed count",passed_count)
print("failed count",failed_count)
if failed_count==0:
    print("Batch Result: All passed")
else:
    print("Batch Result: Needs Improvement")
