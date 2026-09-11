#---------------------------------Error handling-----------------------------------------------------------#

#TASK 1
#write a program to handle division by zero error.

num1=int(input("enter your frist number:-"))
num2=int(input("enter your second number:-"))
try:
    div=num1/num2
    print(div)
except ZeroDivisionError:
    print("cheak your sec number!")

#TASK 2
#write a program to handle invalid intger input

num1=input("enter your frist number:-")
num2=input("enter your second number:-")
try:
    div=int(num1)/int(num2)
    print(div)
except ValueError :
    print("enter only int value!")

#TASK 3
#write a program open a file and handle file not found error

try: 
    f=open("se.txt","r")
    print(f)
    
except FileNotFoundError:
    print("file not found!")

#TASK 4
# write a program to show multiple error handling 

num1=input("enter your frist number:-")
num2=input("enter your sec number:-")
try:
    num1=int(num1)
    num2=int(num2)
    result=num1/num2
    with open("frist_file.txt","r+") as f2:
     f2.seek(0,2)
     f2.write(str(result))
except ZeroDivisionError:
    print("can't divide by zero!")
except FileNotFoundError:
    print("opps! file not found")
except ValueError:
    print("enter only int value!")

#TASK 5
#write a program use finally for the resource cleaning.

num1=input("Enter your frist number:-")
num2=input("Enter Your sec number:-")
f=None
try:
    num1=int(num1)
    num2=int(num2)

    div=num1/num2
    f=open("sec_file.txt","r+")
    f.seek(0,2)
    f.write(str(div))
except ZeroDivisionError:
   print("can't division by zero!")
except ValueError:
     print('int value only')
except FileNotFoundError:
    print("file not found!")
finally:
     if f is not None:
      f.close()
     

#TASK 6
#write a program to custum exception invalid age (<18)

class invalidageerror(Exception):
     pass
age=input("enter your age:-")
try:
    age=int(age)
    if age < 18:
         raise invalidageerror("age must be 18 or above")
except ValueError:
     print("enter only int value!")
except invalidageerror:
     print("you are not eligible!")

#TASK 7
#write a program to handle index error while accessing a list.

car=["BMW","HUNDAI","MAHINDRA","MARUTI"]
try:
    access_element=input("Enter Your Index Number:-")
    print(car[int(access_element)])
except IndexError:
    print("opps! index is out of range")
except ValueError:
    print("enter only int value!")

#TASK 8
#write program for the take two number and handle all posible error.

NUM1=input("Enter your frist number:-")
NUM2=input("Enter Your sec number:-")
class lengthError(Exception):
        pass       
try:
    if len(NUM1)>1:
     raise lengthError("if length more then 1")
    NUM1=int(NUM1)
    NUM2=int(NUM2)
    print("number one is:-",NUM1)
    print("number two is:-",NUM2)   
except ValueError:
    print("Enter Only Int Value!")
except lengthError:
     print("length of number is only 1.")

#TASK 9
#write a program to log error instend of printing them.
 
import logging
num1=input("enter your frist number:-")
num2=input("enter your sec number:-")
try:
    num1=int(num1)
    num2=int(num2)
    div=num1/num2
    print(div)
except ValueError:
    logging.error("int value only!")
except ZeroDivisionError:
    logging.error("can't division by zero!")

#TASK 10
#write a program that validate email format and raise an exception for invaild once.

email=input("Enter your Email:-")
class invalidemail(Exception):
    pass
try:
    email=str(email)
    if "@" not in email or "." not in email:
        raise invalidemail("if @ or . not in email.")
    print("you enter valid email!")
except invalidemail:
    print("invalid email")
        
    
