#Python Conditional Statement's

#cheak if person is eligible for vote(age>=18)
age=19
if age>= 18:
    print("yes,You Are Eligible for Vote!")
else:
    print("sorry,You Are Not Eligible for Vote!")

#grade calculator based on marks 90+ =A,80+ =B ,else C
mark=97
if mark >= 90:
    print("A")
elif mark >=80:
    print("B")
else:
    print("C")

#simulate trafic light red=stop ,yellow=wait, green=go
light_color=str(input("Enter one Trafic Light Colour:-"))
if light_color =="red":
    print("Stop!")
elif light_color=="yellow":
    print("Wait!")
elif light_color=="green":
    print("Go!")
else:
    print("Invalid Color!!!")

#ATM withdrawal cheak sufficient balance or not    
balance=15000
withdrawal_amount=int(input("Enter Withdrawal amount:-"))
if withdrawal_amount <= balance:
    print("Withdrawal Successful!")
else:
    print("Please Cheak Balance!")

#cheak if number is positive negative or zero
num=int(input("Enter Your Number:-"))
if num==0:
    print("Number Is Zero!")
elif num>0:
    print("Number Is Positive!")
elif num<0:
    print("Number Is Negative!")
else:
    print("Enter valid Number")

#cheak if number is lies with a given range
num=int(input("Enter Your Number:-"))
if num in range(1,999):
    print("Number In Range!")
else:
    print("Number Is Out Of Range!")

#username & password varification

UserName="parth@123"
password=1234
User_name=input("Enter UserName:-")
Password=int(input("Enter Password:-"))

if User_name==UserName and Password==password:
          print("Login Sucessefully")
else:
    print("Enter Valid UserName and Password!")

#electricity bil calculator based on units consumed

Unit=int(input("Enter Consumed Units:-"))
if Unit in range(0,50):
      electricity_bil=Unit*3.05
      print(electricity_bil)
elif Unit in range(51,100):
      electricity_bil=Unit*3.50
      print(electricity_bil)   
elif Unit in range(101,250):
      electricity_bil=Unit*4.15
      print(electricity_bil)
elif Unit > 250:
     electricity_bil=Unit*5.20   
     print(electricity_bil)
else:
     print("Cheak Your Unit!")

#simple calculator(add,multiply,divide,subtraction)

num_1=int(input("Enter Your Number For Calculation:-"))
num_2=int(input("Enter Sec Number For Calculation:-"))
opration=input("Enter Your Opration:-")

if opration=="+":
     add=num_1+num_2
     print(add)
elif opration=="-":
     subtrct=num_1+num_2
     print(subtrct)
elif opration=="*":
     mltiply=num_1+num_2
     print(mltiply)     
elif opration=="/":
     divide=num_1/num_2
     print(divide)     
else:
     print("cheak your data Enter by You!!")

#cheak Type of triangle(Equilateral triangle,Isosceles triangle,Scalene triangle)

side_1=int(input("Enter triangle  one side value:-"))
side_2=int(input("Enter triangle  sec side value:-"))
side_3=int(input("Enter triangle  third side value:-"))
if side_1==side_2==side_3:
     print("Equilateral!")
elif side_1==side_2 or side_1==side_3 or side_2==side_3:
     print("Isosceles!")
elif side_1==side_2 and side_1==side_3 and side_2==side_3:
     print("Scalene!")
else:
     print("Cheak Your Data!!")
         

