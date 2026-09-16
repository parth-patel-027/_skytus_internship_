#------------------------------OOP BASIC---------------------------------------------------------#

#TASK 1
#create a class with attribute like brand,model and speed and method to accelerate and break.

class Car:
     def __init__(self,name,model,speed):
          self.name=name
          self.model=model
          self.speed=speed
     def accelerate(self):
           print('your speed is:-',self.speed)  
           acceleration=int(input("Accelerate Your Speed:-"))  
           self.speed+=acceleration      
           print("your Speed now:-",self.speed) 
     def break_car(self):
      break_speed=int(input("enter your speed to break your car:-"))
      print("your car speed is :-",self.speed-break_speed)     
obj_1=Car("Bmw","m5",100) #create a object
obj_1.accelerate()#function call
obj_1.break_car()

#TASK 2
#create a bank account class with deposite and withdraw mwthod.

class BankAccount:
    def __init__(self,total):
        self.total=total
    def deposite_cash(self):
        D_cash=int(input("enter your deposite amount:-"))
        self.total+= D_cash
        print( "your balance is:-",self.total)
    def withdraw(self):
        w_d_cash=int(input("Enter Your Withdraw Amount:-"))
        if w_d_cash < self.total:
             print("Cash Withdraw successfully!")
             balance=self.total-w_d_cash
             print("Your Balance is:-",balance)
        else:
            print("please cheak your balance!!")
obj_2=BankAccount(10000)     
obj_2.deposite_cash() 
obj_2.withdraw()     


#TASK 3
#create a student class with avrge mark calculate method.

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def calculate_average(self):
        total=0
        count=0
        for x in self.marks:
            total+=x
            count+=1
        avg=total/count      
        print("your marks avrage is:-",avg)
obj_3=Student("parth",[20,30,39])
obj_3.calculate_average()       

#TASK 4
#create regtangle class with method to find area and perimiter

class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def calculate_area(self):
         area=self.length*self.width
         print("Area of  Rectangle is :-",area)
    def calculate_perimeter(self):
         perimeter=2 * (self.length + self.width)
         print("Perimiter Of Rectangle:-", perimeter)
obj_4=Rectangle(5,3)
obj_4.calculate_area()  
obj_4.calculate_perimeter()       

#TASK 5
#create a employee  class that display salary salary details.

class Employee:
     def __init__(self,name,salary):
          self.name=name
          self.salary=salary
     def display_data(self):
          print("-------Employee Data-------")
          print("Employee Name:-",self.name)
          print("Salary:-",self.salary)
obj_5=Employee("Nelson Patel",100000)   
obj_5.display_data()       

#TASK 6
#create book class that stores title,author,and prize and display details.

class book:
    def __init__(self,title,author,prize):
        self.title=title
        self.author=author
        self.prize=prize
    def display_book_details(self):
        print("-------Book Details-------")
        print("Book Title:-",self.title)
        print("Author:-",self.author)
        print("prize:-",self.prize)
obj_6=book("THE ALMANACK OF NAVAL RAVIKANT","Eric Jorgenson",469)
obj_6.display_book_details()

#TASK 7
# create circle class that find area and circumfierence.

class Circle:
    def __init__(self,radius):
        self.radius=radius
    def calculate_area(self):
        area=3.14*self.radius**2
        print("Area of circle:-",area)
    def calculate_circumference(self):
        circumference=2*3.14*self.radius
        print("Circumfierence is:-",f"{circumference:.1f}") #use F-string formating formate specifier (:.1f)
obj_7=Circle(5)
obj_7.calculate_area()
obj_7.calculate_circumference()        

#TASK 8
#create a laptop class with the method to apply discount on prize.

class laptop:
    def __init__(self,prize,discount):
        self.prize=prize
        self.discount=discount
    def calculate_discount(self):
        discount_prize=self.prize*self.discount/100
        print("-------Discount Calculator-------")
        print("M.R.P:-",self.prize)
        print("Discount:-",self.discount)
        print("Discount Prize:-")
obj_8=laptop(75000,28)
obj_8.calculate_discount()

#TASK 9
# create flight class with seat booking functionality.

class Flight:
     def __init__(self):
            pass
     def flight_data(self):
        print("------indiGo Airbus A320------")
        print(" Route:- Surat To Mumbai")
        print('[1A, 2B, 3C]  [4D ,5E ,6F]\n'
              "[7A ,8B ,9C]   [10D,11E,12F]\n"
              "[13A,14B,15C]  [16D,17E,18F]\n"
              "[19A,20B,21C]  [22D,23E,24F]\n"
              "[25A,26B,27C]  [28D,29E,30F]\n"
              )
        print("A/F:window  [prize:-9800]\n" "B/E:middle  [prize:-9500]\n"  "C/D:Aisle   [prize:-9600]\n ")
     def seat_booking(self):
         window=["1A","7A","13A","19A","25A","6F","12F","18F","24F","30F"]
         Middle=["2B","8B","14B","20B","26B","5E","11E","17E","23E","29E"]
         aisle=["3C",'9C',"15C","21C","27C","4D","10D","16D","22D","28D"]
         date=input("Enter Your date:-")
         seat=input("Enter Your seat Number:-")
         prize=0
         if seat in window:
              prize+=9800
         elif seat in Middle:
              prize+=9500
         elif seat in aisle:
              prize+=9600
         else :
            print("oops ! seat not found")     

         print("\n----Your Tikit Data----")     
         print("flight name:-indiGo Airbus A320") 
         print("Route:-Surat to Mumbai")
         print("Date:-",date)
         print("total cost:-",prize)           
obj_9=Flight()
obj_9.flight_data()
obj_9.seat_booking()

#TASK 10
#Create a shop class with a method to add and list products.

class Shop:
    def __init__(self,*product):
        self.product=list(product)
        print(product)
obj_10=Shop("dove","lifeboy","detol","fiyama")
