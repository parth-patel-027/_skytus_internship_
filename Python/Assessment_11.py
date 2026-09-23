#------------------------------Modules & Libraries-----------------------------------------------#

#TASK 1
#create a  custom math module and import  it into a another file.
import Custom_Math as math
#addition 
math.Addition(23,45)

#multiplication
math.Multiply(23,4)

#subtraction
math.Subtraction(1022,432)

#division
math.Division(240,2)

#----------------------------------------------------------------------------------------------------
#TASK 2
#Create a module to perform a string opration

import string_op

#length of string
string_op.length("python is popular programming language.")

#string convert into lower case
string_op.Lower("PARTH PATEL")

# convert into upper case
string_op.upper("python")

#---------------------------------------------------------------------------------------------------
#TASK 3
#use a random module to generate 5 random intigers.

import random

intiger=[]

for i in range(5):
    x=random.randint(1,10)
    intiger.append(x)
print(intiger)  

 #----------------------------------------------------------------------------------------------------  
#TASK 4
#use datetime module to display current date time.

import datetime

x= datetime.datetime.now()
print(x)

#------------------------------------------------------------------------------------------------------
#TASK 5
#use math module to find factorial of number 

import math

print(math.factorial(9))
print(math.factorial(8))

#-----------------------------------------------------------------------------------------------
#TASK 6
#Create package shapes with modules for circle and rectangle
from shapes import circle,rectangle

#to find area of circle
circle.Area_circle()

#to find area of rectangle
rectangle.Area_of_Rectangle()

#----------------------------------------------------------------------------------------------
#TASK 7 
#import multiple function from one module and use them.

from Custom_Math import Addition,Multiply,Division,Subtraction

Addition(2,4)
Multiply(120,3)
Division(120,2)
Subtraction(10,5)

#-----------------------------------------------------------------------------------------------
#TASK 8
#write a program to suffle list using random module.

import random

mylist=[1,2,3,4,5,6,7,8,9,10]
random.shuffle(mylist)
print(mylist)

#------------------------------------------------------------------------------------------------
#TASK 9
#write a program to calculate diffrance between two dates.

from datetime import datetime

date1 = input("Enter Your first date:- ")
date2 = input("Enter Your sec date:- ")

date1 = datetime.strptime(date1, "%d-%m-%Y")
date2 = datetime.strptime(date2, "%d-%m-%Y")

D = abs(date1 - date2)

print(D.days)

#---------------------------------------------------------------------------------------------------
#TASK 10
# us os Module to list file in dictionry.

import os

file=os.listdir(".")

file_dict={}

for i,file in enumerate(file,1):
    file_dict[i]=file

print(file_dict)    