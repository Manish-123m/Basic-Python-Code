import math
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area_of_circle(self):
        return math.pi*(self.radius)**2
    def parameter_of_circle(self):
        return 2*math.pi*self.radius
radius=float(input("Enter the radius: "))
circle=Circle(radius)
area=circle.area_of_circle()
parameter=circle.parameter_of_circle()
print(area)
print(parameter)


#######  Using Cunstroctor intro  ------------==================

class Person:
    def __init__(self,name,age,Work):
        self.name=name
        self.age=age
        self.Work=Work
    def intro(self):
        print("i am",self.name,"i am",self.age,"year old and my work is",self.Work,)
person1=Person("manish",25,"Study")
person1.intro()


### make car model using cunstrocture--------------

class Car_model:
    def __init__(self,car,model,power,price,year):
        self.car=car
        self.model=model
        self.power=power
        self.price=price
        self.year=year
    def display_info(self):
        print("This vechical brand ",self.car,"and it's version",self.model,"it's very fast using",self.power,"Power  and this car price is",self.price," and this is",self.year,"year old ")
my_car=Car_model("Bugati","letest","Super fast",20000000,2)
my_car.display_info()

##### Create a recatangle and find area and parameter-----------======================
class Rectangle:
    def __init__(self,length,height):
        self.length=length
        self.height=height
    def area(self):
        print("area of rectangele:",self.length*self.height)
    def parameter(self):
        print("Parameter of rectangle:",2*(self.length+self.height))
rect=Rectangle(5,8)
rect.area()
rect.parameter()


### In account deposit and withdrawal and calculate amount

class Account_Statement:
    def __init__(self,account_holder_name,account_number,Balance):
        self.account_number=account_number
        self.account_holder_name=account_holder_name
        self.Balance=Balance
    def Deposit(self,amount):
        self.Balance+=amount
        print("After Deposit amount is",self.Balance,"and deposit amount is",amount)
    def withdraw(self,amount):
        if amount<=self.Balance:
            self.Balance-=amount
            print("After Withdraw amount is ",self.Balance,"and withdraw amount is",amount)
        else:
            print("Insuffcient Balance",self.Balance)
    def display_balance(self):
        print("Balance: ",self.Balance)
account_holder_name=input("Enter the Account Holder Name As Par PAN")
account_number=int(input("Enter the Account Number :"))
Balance=float(input("Enter the Minimum Amount For active Account:"))

account=Account_Statement(account_holder_name,account_number,Balance)
Diposit_Amount=float(input("Enter the Diposit amount:"))
Withdrwa_Amount=float(input("Enter the Withdrawal ammount:"))
account.Deposit(Diposit_Amount)
account.withdraw(Withdrwa_Amount)
account.display_balance()
print("Account Holder Nmae:",account_holder_name)
print("Account_number:",account.account_number)



class Student_Marks:
    def __init__(self,name,marks):
        self.name=name
        self.mark1=marks

    def calculate_avg(self):
        avg=sum(self.marks)/len(self.marks)
        return avg
    




class Student_Marks:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def calculate_avg(self):
        total=0
        for i in self.marks:
            total+=i
        avg=total/len(self.marks)
        return avg
    def print_avg(self):
        total=self.calculate_avg()
        print("student Name:",self.name)
        print("avg marks ",total)
student1=Student_Marks("manish",[1,2,3])
student1.print_avg()


class Myclass:
    @staticmethod

    def add(a,b):
        return a+b
print(Myclass.add(5,8))



class Myclass:
    @staticmethod
    def welcome(a):
        return a
print(Myclass.welcome("Welcome this static method"))



###### Example of Encapsulation
class Bank:
    def __init__(self,account,password):
        self.account=account
        self.__password=password
b1=Bank(123654,123)
print(b1.account)
print(b1.password)


class Bank:
    def __init__(self,account,password):
        self.account=account
        self.__password=password
    def reset_pass(self):
        print(self.__password)
b1=Bank(123654,123)
print(b1.account)
# print(b1.password)
b1.reset_pass()

Key Principles of Encapsulation:
Private Variables: Variables that should not be accessed directly from outside the class.
Public Methods: Methods that provide controlled access to the private variables, typically through "getter" and "setter" methods.


class Car:
    def __init__(self):
        self.start=False
        self.brek=False
        self.clutch=False
    def engine_start(self):
        if not self.start:
            self.start=True
            print("Engine is started")
        else:
            print("Engine is already started")
    def engine_stop(self):
        if self.start:
            self.start=False
            print("Engine is stopped")
        else:
            print("Car is already stopped")
    def press_clutch(self):
        if not self.clutch:
            self.clutch=True
            print("Clutch is pressed")
        else:
            print("Clutch is already pressed")
    def release_clutch(self):
        if self.clutch:
            self.clutch=False
            print("Clutch os released")
        else:
            print("Clutch is already released")
    def car_status(self):
        engine_status="on"if self.start else "off"
        Clutch_status="Pressed" if self.clutch else "Released"


        print("Car status: Engine:"+ engine_status +","+"Clutch:"+ Clutch_status)
my_car=Car()
my_car.engine_start()
my_car.press_clutch()
my_car.car_status()
my_car.release_clutch()
my_car.engine_stop()
my_car.car_status()




###----------Inheritance ============================
class Car:
    color="Black"
    @staticmethod
    def start():
        print("Car started")
    @staticmethod
    def stop():
        print("Car is stopped")
class maruti(Car):
    def __init__(self,name):
        self.name=name
m1=maruti("swift")
m1.start()
m1.stop()

##########----   Multiple Inheryance-----------

class A:
    vara="Hello from A"
class B:
    varb="Hello from  B"
class C(A,B):
    varc="Hello from C"
obj=C()
print(obj.vara)
print(obj.varb)
print(obj.varc)


###########     use super()---------------

class Car:
    def __init__(self,type):
        self.type=type
    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def stopped():
        print("Car stopped")
class Maruti(Car):
    def __init__(self,name,type):
        self.name=name
        super().__init__(type)
s1=Maruti("Swift","Diesel")
print(s1.name)
print(s1.type)
s1.start()
s1.stopped()



class Car:
    name="Arun"
    def __init__(self,name):
        self.name=name
c1=Car("Rahul")
print(c1.name)
print(Car.name)


class Car:
    name="Arun"
    def __init__(self,name):
        self.__class__name=name
        # Car.name=name
c1=Car("Rahul")
print(c1.name)
print(Car.name)


class Car:
    name="Arun"
    def __init__(self,name):
        Car.name=name
        # Car.name=name
c1=Car("Rahul")
print(c1.name)
print(Car.name)

class Car:
    name="Arun"
    def __init__(self,name):
        self.name=name
    @classmethod
    def changename(self,new_name):
        self.name=new_name
c1=Car("Rahul")
print(c1.name)
print(Car.name)
Car.changename("Manish")
print(Car.name)
print(c1.name)


class ClassName:
    def __init__(self,name1,name2):
        self.atr1=name1
        self.atr2=name2
s1=ClassName("manish","Kumar")
print(s1.atr1)
print(s1.atr2)



class check:
    def __init__(self):
        print("check id",id(self))
obj=check()
print("Address of class object=",id(obj))



###########------------  Polymorphism  -------------------

class animal:
    def speak(self):
        print("Animal make a sound ")
class Dog(animal):
    def speak(self):
        print("Dog barks")
class Cat(animal):
    def speak(self):
        print("CAt Mews")
dog=Dog()
cat=Cat()
animals=[dog,cat]
for animal in animals:
    animal.speak()


class Printer:
    def print_msg(self,msg="Hello ,World !"):
        print(msg)
printer=Printer()
printer.print_msg()
printer.print_msg("custom msg")


class Printer:
    def __init__(self,msg="hello"):
        print(msg)
    def print_msg(self,new="Wold"):
        print(new)
printer=Printer()
printer.print_msg("manish")

 ############   -----   Overriding -------------------

class A:

    def man(self,name):
        return name
    def mn(self,name,age):
        return name,age
class B(A):
    def ee(self,name,marks,number):
        return name,marks,number
s=A()
result=s.man("manish")
print(result)
