#write a program to print your name age and city in one line
print("My name is Parth",'I Am 20 year old',"My City Name is Navsari")

#take a input two number and print their sum
number1=int(input('enter  frist number:-'))
number2=int(input('enter sec number:-'))
print(number1+number2)

#write a program to convert teamprature in to celcius to fehranhiet
celcius=int(input('enter temprature in celcius:-'))
fehranhiet=celcius*9/5+32
print(fehranhiet)

#store your name in variable and convert into a uppercase
student_name="parth patel"
print(student_name.upper())

#ask user thier brithday year and find their currnet age
brithday_year=int(input('enter your brithday year:-'))
current_year=2026
age=current_year-brithday_year
print(age)

#write a program swap to variable
frist_name="patel"
last_name="parth"
print(frist_name,last_name)
frist_name,last_name= last_name , frist_name
print(frist_name,last_name) #after swaping variables

#create a program find area of regtangle user input
length=int(input("enter length of rectangle:-"))
width=int(input('enter width of rectangle:-'))
area_of_rectangle=length*width
print(area_of_rectangle)

# write a program to cheak if number is positive or negative
num=23
if num > 0:
    print("this number is positive")
else:
    print("this number is negative")

#ask for a two number and print their average
num1=int(input("enter one number:-"))
num2=int(input("enter sec number:-"))
avg=num1+num2/2
print(avg)


