#calculate the remainder of two number 

a=23
b=5
remainder=a%b
print(remainder)

#cheak if number is even or odd

number=23
if number%2==0:
    print('number is positive!')
else:
    print("number is negative!")

#compare two number and print larger one

number_1=23
number_2=12
if number_1 > number_2:
    print(number_1)
else:
    print(number_2)

#write a program to find a square and cubs of number

number=int(input("Enter Your Number:-"))
square=number**2
cubs=number**3
print("square is:-",square)
print("cubs is:-",cubs)

#write a program given two number is qual

number_1=50
number_2=50
equal=number_1==number_2
if equal==False:
    print("Your Numbers Are Not Equal!")
else:
    print("Your Numbers Are Equal!")

#write a program to take two number and print true if both are positive else false

number_1=int(input("Please Enter Number:-"))    
number_2=int(input("Please Enter Number:-"))   
if number_1 and number_2>0:
    print("True")
else:
    print("False")

#write a program tp convert float into intiger

number=float(input("Enter A Float Number:-"))
intiger_number=int(number) #convert into intiger
print(intiger_number)
print(type(intiger_number))

#take a number as a string and convert into intiger and multiply by 10

number=str(input("enter number :-"))
print(type(number))
intiger=int(number)*10 #convert into intiger and multiply by 10
print(intiger)

#write a program that use of and & or opertors to cheaks multiple conditions
#write a condition for number is positve or even but also grater then 500

number=int(input('enter your number:-'))
if number>0 or number%2==0 and number>500: 
    print("This Number Is valid!")
else:
    print("This Number Is Not Valid!")

#write a function to find quoienit and remainder
number_one=int(input("Enter Your Number For Division:-"))
number_two=int(input("Enter Number:-"))
division= int(number_one/number_two)
remainder=number_one%number_two
print(f"Quoienit Is ,{division}")
print(f"Remainder Is,{remainder}")