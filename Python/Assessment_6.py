#write a function if number is prime or not

def find_prime_number():
     num=int(input("Enter your number : "))  
     if num <=1:
          print("Number is not Prime!")       
     else:
          for i in range(2,num):
           if num%i==0:
                print("number is not prime")
                break    
          else:
                print("Number is Prime!")
find_prime_number()

#function for reverse a string

def reverse_string():
    string=input("Enter Your String:-")
    print(string[::-1])
reverse_string()    

# #function to find a factorial

def factorial():
    factorial=1
    num=int(input("Enter Your Number:-"))
    for i in range(1,num+1):
        factorial*=i
    return factorial     

x=factorial()
print("Factorial Is:-",x)

# #write a function for simple intrest calculate

def intrest():
    Principle=int(input("Enter Principle Amount:-"))
    Rate=int(input("Enter Intrest:-"))
    Time=int(input("Enter Duration in:-"))
    #main logic 
    simple_intrest=Principle*Rate*Time/100
    return simple_intrest
x=intrest()
print(x)
    
# #write a function cheak if word is palindrome

def paliandrome():
    word=str(input("Enter Your Word:-"))
    if word==word[::-1]:
        print('Word is Paliandrome')
    else:
        print('word is not paliandeome')
paliandrome()       

#write a function to count vowels in string

def count_vowels(string):
    count=0
    vowels=("A","E","I","O","U","a","e","i","o","u")
    for i in string:
        if i in vowels:
            count+=1
    return count
x=count_vowels("parth")
print(x)

#write a function to merge to list

def merge_list(list_1,list_2):
     marge_l=list_1+list_2
     return marge_l
x=merge_list([1,2,3,5],[34,23,24,23,67]) 
print(x)   

#write a function for find GCD For two number 

def GCD_finder():
    num_1=int(input("Enter a Number:-"))
    num_2=int(input("Enter a Number:-"))
    divisor_1=set()
    divisor_2=set()
    for i in range(1,num_1+1):
       if  num_1%i==0:
           divisor_1.add(i)
    for i in range(1,num_2):
        if num_2%i==0:
            divisor_2.add(i)
    result=divisor_1.intersection(divisor_2)   
    GCD=max(result)
    return GCD
x=GCD_finder()
print(x)
    
#FIND THE AREA OF RECTANGLE

def area_rectangle():
    hight=int(input("Enter Hight Of Rectangle:-"))
    width=int(input("Enter width of Rectangle:-"))

    area=hight*width
    return area
x=area_rectangle()
print(x)

#write a function cheak if number is armstrong or not

def armstrong_number():
    num=input("Enter Number:-")
    count=0
    sum=0
    for i in num:
        count+=1
    for i in num:
       m=int(i)**int(count)
       sum+=m
    if sum == int(num):
        print("Number is Armstrong!")
    else:
        print("Number is not Armstrong!")
armstrong_number()
