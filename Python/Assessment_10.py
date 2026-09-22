#---------------------------OOP Advance-----------------------------------#

#TASK 1
#create a base class animal and sub class dog clss and cat class.

class Animal:
    def __init__(self):
        pass
class dog(Animal):
        print("my dog  name  is lio!")
class cat(Animal):
        print("my cat name is meow!")
obj_1=Animal()  

#TASK 2
#create a class hirechy for  vehicle----car---electric class

class Vehicle:
    def __init__(self,brand,speed):
        self.brand=brand
        self.speed=speed
class Car(Vehicle):
    def __init__(self, brand, speed,doors):
        super().__init__(brand, speed)
        self.doors=doors 
class Electric_car(Car):  
     def __init__(self, brand, speed, doors,capacity):
         super().__init__(brand, speed, doors)
         self.capacity=capacity 
         print("Car Brand is:-",brand)
         print("Top Speed Is:-",speed)
         print("Number of doors:-",doors)
         print("Battryn Capacity:-",capacity)
Electric_car_obj= Electric_car("mahidra",340,5,670)

#TASK 3
#Impliment method overriding base class and drived class

class Vehicle:
    def start(self):
          print("Car is start!")
        
class Car(Vehicle):
    def start(self):
         print("car is start with key!") 
     
car_obj=Car()
car_obj.start()

#TASK 4
#Demonstarte multiple inheritance with the two parent class.

class Xuv_3xo:  # First parent class
    def __init__(self, prise, **kwargs):
        self.prise = prise
        super().__init__(**kwargs)

    def details(self):
        print("This Is Type is Hatchback Xuv")
        print("This car prise is:-", self.prise)


class Xuv_700:  # Second parent class
    def __init__(self, cost, **kwargs):
        self.cost = cost
        super().__init__(**kwargs)

    def Details(self):
        print("This Is Type is Xuv")
        print("This car prise is:-", self.cost)


class Car(Xuv_3xo, Xuv_700):  # Multiple inheritance
    def __init__(self, prise, cost, **kwargs):
        super().__init__(prise=prise, cost=cost)

    def impformation(self):
        print("-----Car's-----")
        print("XUV 3xo cost is", self.prise)
        print("XUV 700 cost is", self.cost)

car_obj = Car(3, 3333)
car_obj.impformation()

#TASK 5
#create polymorpfic function for that wrok with diffrent shapse

class square:
    def __init__(self,r):
         self.r=r
    def area(self):
         a=self.r*self.r
         print("Area of square:-",a)
class circle:
     def __init__(self,R):
          self.R=R
     def area(self):
          a=3.14*self.R**2
          print("Area of Circle:-",a)
class regtangle:
     def __init__(self,l,w):
          self.l=l
          self.w=w
     def area(self):
          a=self.l*self.w
          print("Area of Regtangle:-",a)
def calculate_area(shape):
     shape.area()                   
square_obj=square(5)
circle_obj=circle(4)
regtangle_obj=regtangle(4,6)
calculate_area(square_obj)
calculate_area(circle_obj)
calculate_area(regtangle_obj)

 #TASK 6
 # Create a bank system with current acount class and saveing account class.

class BankAccount:
    def __init__(self,holder,balance):
        self.holder=holder
        self.balance=balance
class Saving_account(BankAccount):
    def deposite(self):
        d_m=input("Enter Deposite Money:-")
        self.balance+=int(d_m)
        print("Your New Balance :-",self.balance)
class Current_account(BankAccount):
    def withdraw(self):
        w_m=input("Enter Your Withdraw Amount:-")
        self.balance-=int(w_m)
        print("Successfully withdraw!")
        print("Your Balance Now:-",self.balance)


Saving_ac_obj=Saving_account("parth",10000)
Current_ac_obj=Current_account("parth",10000)  
Current_ac_obj.withdraw()
Saving_ac_obj.deposite()

#TASK 7
#Create a class with private attribute with getter/setter method.

class Bank_Account:
    def __init__(self,id):
        self.__id=id
    def get_id(self):
         return self.__id
    def set_id(self,new_id):
        self.__id=new_id
id=input("Enter Your id:-")    
Account_obj= Bank_Account(id)
print("OLD iD:-",Account_obj.get_id())
new_id=input("Enter Your New Id:-")
Account_obj.set_id(new_id)
print("NEW ID:-",Account_obj.get_id())

#TASK 8
#create a teacher and student class to show inheritance.

class Teacher:
    def __init__(self,class_name,class_capacity):
        self.class_name=class_name
        self.class_capacity=class_capacity       
class Student(Teacher): 
      def __init__(self, class_name, class_capacity,floor):
           super().__init__(class_name, class_capacity)
           self.floor=floor
      def display(self):
           print("Class name is:-",self.class_name)
           print("Class capacity:-",self.class_capacity)
           print("clss floor Number:-",self.floor) 
student=Student("9-C",56,5)    
student.display()   

#TASK 9
# Create Music Player Class And sub Class spotify to override a method play.

class Music_player:
    def __init__(self):
        pass
    def play(self):
        print("PLAY MUSIC")
class spotify(Music_player): 
    def play(self):
        print("STOP MUSIC")

MUSIC=Music_player()
SPOTIY=spotify()
SPOTIY.play()

#TASK 10
#Demonstarte use of super in inheritance.

class Laptop:
    def __init__(self,name,ram,storage):
        self.name=name
        self.ram=ram
        self.storage=storage
class Display(Laptop):
    def __init__(self, name, ram, storage,color):
        super().__init__(name, ram, storage)  
        self.color=color 
    def INFO(self):
        print("laptop name is:-",self.name)
        print("Ram is:-",self.ram)
        print("Storage is :-",self.storage)
        print("Color is:-",self.color)        

lapy=Laptop("HP-Pavalion",12,512)
display=Display("HP-Pavalion",12,512,"black")    
display.INFO()    