print("Courses Available Python \n Java \n Flutter \n C++ \n Html and Css")
coursename=input("enter your coursename")
f=open("course.txt","r")
for i in f:
    if(i.split(" ")[0]==coursename):
        print("courses is available")
        print("coursetype:",i.split(" ")[1])
        print("courseduration:",i.split(" ")[2])
        print("coursefees",i.split(" ")[3])
else:
    print("invalid course")
f.close()