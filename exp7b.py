print("251A018 , 9/2/26")
Student={ }
n=int(input("Enter no.of students :"))
for i in range(1,n+1) :
     Name=input("Enter Name :")
     Attendance=input("Enter the Attendance (%):")
     Student[i]={"Name": Name , "Attendance" : Attendance}
print(Student)
