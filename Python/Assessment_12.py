#------------------------------Loop---------------------------------------------#

#TASK 1------------------------------------------------------------------
#PRINT NUMBER FROM 1 TO 10.

for i in range(1,11):
    print(i)

#TASK 2-----------------------------------------------------------------
#Display multiplication table of a given number.

Number=int(input("Enter Your number:-"))
for i in range(1,11):
    table=Number*i
    print(f"{Number}*{i}={table}")

#TASK 3------------------------------------------------------------------
# Find factorial of number

Number=int(input("Enter Your Number for factorial:-"))
factorial=1
for i in range(1,Number+1):
    factorial=factorial*i
print(factorial)    

#TASK 4------------------------------------------------------------------
#Generate the frist N febonacci number.
num=int(input("Enter Your number:-"))
a=0
b=1
for i in range(num):
    print(a, end=" ")
    next_num = a + b
    a = b
    b = next_num

# #TASK 5-----------------------------------------------------------------
#Cheak if number is prime or not.
num=int(input("Enter Your Number :-"))
prime=True
for i in range(2,num):
    if num % i==0:
        prime=False
        break
if prime:
    print("Number Is Prime!")
else:
    print("Number Is Not Prime!")  

# #TASK 6-----------------------------------------------------------------
# #Reverse a number.
num = int(input("Enter Your Number:- "))

revers = 0

while num > 0:
    last_digit = num % 10
    revers = revers * 10 + last_digit
    num = num // 10

print("Reverse Number is:-", revers)

#TASK 7-------------------------------------------------------------------------
#count digit in number.
num=input("Enter Your Number :-")
num=str(num)
count=0
for i in num:
    count+=1
print(count)

# #TASK 8-----------------------------------------------------------------------
#find a sum of even Number from  1 to 100.
sum=0
for i in range(1,101):
    if i%2==0:
        sum+=i
print(sum)

# #TASK 9----------------------------------------------------------------------
#Print pyramid pattren
n = 5
for row in range(1, n + 1):
    for space in range(n - row):
        print(" ", end="")

    for star in range(2 * row - 1):
        print("*", end="")

    print()
    
#TASK 10------------------------------------------------------------------------------
#find all divisor of number
Num=int(input("Enter Your Number:-"))
divisor=[]

for i in range(1,Num+1):
    if Num%i==0:
        divisor.append(i)
print(divisor)        
