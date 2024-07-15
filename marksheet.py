a=input("Enter the name  of the student::")
b=input("Enter the name  of the college::")
c=input("Enter the Roll NO::")
sub1=input("Enter the sub1::")
m1=int(input("Enter the mark1::"))
sub2=input("Enter the sub2::")
m2=int(input("Enter the mark2::"))
sub3=input("Enter the sub3::")
m3=int(input("Enter the mark3::"))
sub4=input("Enter the sub4::")
m4=int(input("Enter the mark4::"))
sub5=input("Enter the sub5::")
m5=int(input("Enter the mark5::"))

total=m1+m2+m3+m4+m5
per=total/5
          
print("-----------------MARKSHEET-----------------")
print("student's Name::",a)
print("College Name::",b)
print("Roll No::",c)
print("--------------------------------------------")
print("subjects\t\t\tmarks")
print(sub1,"\t\t\t\t",m1)
print(sub2,"\t\t\t\t",m2)
print(sub3,"\t\t\t\t",m3)
print(sub4,"\t\t\t\t",m4)
print(sub5,"\t\t\t\t",m5)
print("--------------------------------------------")
print("Total",total)
print("percantage",per)
if(per>=35 and per<55):
    print("Grade C")
elif(per>=55 and per<75):
    print("Grade B")
elif(per>=75 and per<99):
    print("Grade A")
else:
    print("Grade F")  



