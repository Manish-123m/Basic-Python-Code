# a='manish'
# b='kumar'
# c='fdf'
# print(a)
# print(b)
# print(c)


# b=[1,2,3,4,5,6,7,8,9]
# print(b)
# print(type(b))


# c = {"Manish": 1, "avi": 2}
# print(c)
# print(c["manish"])


# a=10
# b=880
# print(a-b)
# print(a+b)
# print(b-a)
# print(b+a)


# x="mansi"
# y=3
# print(x*4)
# print(y*"man")
# print(x*y)


# # Basic variables
# a = 20
# b = 10

# # Print basic arithmetic results
# print("a =", a)
# print("b =", b)

# print("Addition:", a + b)        # Output: 30
# print("Subtraction:", a - b)     # Output: 10
# print("Multiplication:", a * b)   # Output: 200
# print("Division:", a / b)         # Output: 2.0

# # Working with strings
# name = "Alice"
# greeting = "Hello"
# print("Greeting:", greeting + ", " + name + "!")  # Output: Hello, Alice!

# # Working with lists
# numbers = [1, 2, 3, 4]
# print("Numbers List:", numbers)

# # List operations
# numbers.append(5)                 # Adding an element
# print("After appending 5:", numbers)  # Output: [1, 2, 3, 4, 5]

# # Working with tuples
# point = (3, 4)
# print("Point Tuple:", point)      # Output: (3, 4)

# # Accessing tuple elements
# print("X coordinate:", point[0])  # Output: 3
# print("Y coordinate:", point[1])  # Output: 4

# # Working with sets
# unique_numbers = {1, 2, 2, 3}
# print("Unique Numbers Set:", unique_numbers)  # Output: {1, 2, 3}

# # Set operations
# unique_numbers.add(4)             # Adding an element
# print("After adding 4:", unique_numbers)  # Output: {1, 2, 3, 4}

# # Checking membership
# print("Is 2 in the set?", 2 in unique_numbers)  # Output: True
# print("Is 5 in the set?", 5 in unique_numbers)  # Output: False
# print(a%b)

# print(15%3)


#######  Question 


# Side_length=float(input("Enter the length of a side of the square: "))
# area=Side_length**2
# parameter=4*Side_length
# print("area of square",area)
# print("parameter of square:",parameter)

# ####Rectangle

# a=float(input("Enter the widht of rectanglr:"))
# b=float(input("Enter the height of rectangle:"))
# area=a*b
# parameter=2*(a+b)
# print("area of rectangle:",area)
# print("parameter of rectangle:",parameter)



##--------------------------Function-----------------------------------

# x=abs(-8)
# print(x)

# x=abs(-8.54)
# print(x) 

# x=abs(-8.54+5j)
# print(x) 

# x=bin(13)
# print(x)

# x=bytes(78)
# print(x)

# c=chr(97)
# print(c)
# c=chr(91)
# print(c)

# x=float(input("enter your lab_1 score :"))
# y=float(input("enter your lab 2 score :"))
# z=float(input("enter your lab 3 score :"))
# a=float(input("enter your lab 4 score :"))
# b=float(input("enter your lab 5 score :"))
# sum=x+y+z+a+b
# print("avg lab result:",sum/5)


# i=20
# if (i>=20):
#     print("i is greater than 15")
# else:
#     print("check")


# attendence=int(input("enter the attendence:"))
# if attendence>=80:
#     print("Green marks")
# if attendence>=50 and attendence<80:
#     print("yellow")
# if attendence>=0 and attendence<50:
#     print("red")



# age=int(input("Enter the age : "))
# if age>=18:
#     print("You are eligible")
# else:
#     print("You are not eligible")

# a=int(input("Enter your score :"))
# if a>=90 and a<=100:
#     print("A Grade")
# elif a>70 and a<90:
#     print("B Grade")
# elif a>=50 and a<70:
#     print("C Grade")
# elif a<50:
#     print(" Fail")
# else:
#     print("Wrong input")


####  Calculate the area of circle

# pai=3.14
# radius=5
# area= pai*(radius**2)
# print("Area of circle:",area)


# ####  Calculate the parameter of circle
# pai=3.14
# radius=5
# parameter=2*(pai*radius)
# print("Parameter of circle:",parameter)

###  calculate the area of triangle 
# height=10
# base=25
# hipotanus=50
# area=1/2*(base*height)
# parameter=height+base+hipotanus
# print("area of triangle :",area)
# print("parameter of triangle:",parameter)



###########Using input function take two number and then swap the number
# a=5
# b=9
# a,b=b,a
# print(a)
# print(b)


# units=int(input("Enter the number of units used:"))
# bill=0
# if units<=100:
#     bill=0
# elif units<=200:
#     bill=(units-100)*5
# else:
#     bill=(100*5)+((units-200)*10)
# print("Total bill amount : Rs",bill)



# amt = 0
# number = int(input("Enter the number of electric units: "))

# if number <= 100:
#     amt = 0
# elif 100 < number <= 200:
#     amt = (number - 100) * 5
# else:
#     amt = 500 + (number - 200) * 10

# print("Amount you have to pay is:", amt)

# amt=0

# number=int(input("enter the number of electric unit ")) 
# if number<=100: 
#     amt=0 
# if number>100 and number<=200: 
#     amt=(number-100)*5

# if number>200:

#     amt=500+(number-200)*10

# print("amout you have to pay are", amt,)


# i=1
# n=10
# while i<=10:
#     print(i)
#     i+=1


# i=1
# a=int(input("Enter the number"))
# while i<=10:
#     print(f"Table of {a}*{i}:{i*a}")
#     i+=1

# name = "manish"
# count=0
# while count<=5:
#     print(name)
#     count+=1

# i=1
# while i<6:
#     print("Manish kumar")
#     i+=1

# i=1
# while i<=11:
#     print(i**3)
#     i+=1


# x=["manish","avanish","nik"]
# for i in x:
#     print(i)


# for a in "manishkumar":
#     print(a)


# a=[]
# for i in range(1,15):
#     a.append(i**2)
# print(a)



# b=["Manish","Avanish","Rahul"]
# for i in b:
#     b.append("nik")
# print(b)


###    Write a  Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included).
# a=[]
# for x in range(1500,2700):
#     if x%7==0 and x%5==0:
#         a.append(x)
# print(a)




###     Write a  Python program to construct the following pattern, using a nested for loop.


# n=5
# for i in range(n):
#     for j in range(i):
#         print(" *",end="")
#     print()
# for i  in range(n,0,-1):
#     for j in range(i):
#         print(" *",end="")
#     print()


# n=int(input("Enter the number for ...:"))
# for i in range(n):
#     for j in range(i):
#         print(" *",end="")
#     print()

# for i in range(n,0,-1):
#     for j in range(i):
#         print(" *",end="")
#     print()

#   # Number of rows

# for i in range(n):
#     # Print spaces for alignment
#     print(" " * (n - i - 1) + "*" * (i + 1))






# for i in range(n):
#     print(" "*(n-i-1)+" *"*(i+1))

# for i in range(n):
#     print(" "*(n-i-1)+"*",end="")
# print()



# n = int(input("Enter the number of rows for the Squre: "))  # Rows for Square
# # m = int(input("Enter the number of columns for the rectangle: "))  # Columns for rectangle

# # Inverted Triangle
# for i in range(n, 0, -1):
#     # for i in range(n):
#         print("  *"*n)

# Rectangle Pattern
# for i in range(n):
#     print("* " * m)


# n=6
# for i in range(0,n+1):
#     print(" *"*i)


# n=6
# for i in range(n):
#     for j in range(i):
#         print(" *",end="")
#     print()



# a=[1,2,3,4,5,6,9,8,7,4,1,74,1,212,3,66,4,5,89,45,5555,55,5,4,7,7,8,8,8,8,89,9,9,9,9,6,6,5,5,5,741,69,2,2,2,2,2]
# even=[]
# odd=[]
# for i in(a):
#     if i%2==0:
#         even.append(i)
        
#     elif i%2!=0:
#         odd.append(i)
# print("odd number:",odd)
# print("even number:",even)


# a=[1,-2,7,-27,8,-7,-6,4]
# posi=[]
# neg=[]
# for i in a:
#     if i>=0:
#         posi.append(i)
#     else:
#         neg.append(i)
# print("positive number:",posi)
# print("negative number:",neg)



# for i in range(5):
#     if i==4:
#         break
#     print(i)

# for i in range(9):
#     if i==4:
#         continue
#     print(i)




##############---------------------=====================================================----------------------------------------

# def demo():
#     print("this is my first function demo")
# demo()
# demo()


# def address():
#     print("Anudip Fundation")
#     print("Kolakata")
#     print("9616463523")
#     for i in range(5):
#         a=input("Enter your name:")
#         b=input("Enter your marks:")
# address()

# def demo(name):  # name is a parameter
#     print(name)

# demo("manish")  # "manish" is the argument


# a=5
# b=3
# a,b=b,a
# print("After swapping:")
# print("a =", a)
# print("b =", b)




# a=5
# b=3
# a=a+b
# b=a-b
# a=a-b
# print(a)


# ch=input("Enter the word")[0]
# print(ch)


# def find(v):
    
#     if v<=100:
#         print(v*5)
#     elif v>=100 and v<=200:
#         print(v*10)
#     elif v>=200 and v<=500:
#         print(v*20)
#     else:
#         print(v*30)
# valu=float(input("Enter the value of meter uses"))
# find(valu)

# def demo(first_name,last_name):
#     print(first_name +" " + last_name)
# demo(first_name="manish", last_name="kumar")



###############---  slicing -----======================
# str="hello manish kumar hoe are you ?"
# print(str[7:10])  #### 7 is included 
# print(str[:10])   ###  [start: end: skip]
# print(str[0:15:2])
# print(str[0:15:1])
# print(str[2::3])
# print(str[::1])
# print(str[::-1])


# str="how are you ?"
# words=str.split()
# arrenge=" ".join([words[2],words[1],words[0]])
# print(arrenge)
# str = "how are you?"

# Replace "how" with "who"
# modified_str = str.replace("how", "who")

# # Print the modified string
# print(modified_str)
# print(str.find("z"))
# if ("are" in str):
    # print("yes it's present in str")


# str1="my name is manish"
# str2="i am feeling well"
# print(str1+","+str2)
# print(str1+" and "+str2)

# list=[1,21,3,6,5,4,7,8,9,8]
# list.remove(21)
# print(list)
# l1=["manish","avanish","panku","nik"]
# l2=[1,2,3,6,5,4,7,8,9]
# l3=l1+l2
# print(l3)
# l3.reverse()
# print(l3)

# l=[2,7,9,1,4,12]
# result=sum(l)
# print(result)


# l=[2,7,9,1,4,12]
# total=0
# for i in l:
#     total+=i
# print(total)


# l=[2,7,9,1,4,12]
# total=1
# for i in l:
#     total*=i
# print(total)

# l=[2,7,9,1,4,12]
# l[0],l[-1]=l[-1],l[0]
# print(l)
# l=[2,7,9,1,4,12]
# print(max(l))

# l=[2,7,9,1,4,12]
# k=[]
# lis=len(l)
# for i in range (1,7):
#     j=-i #
#     k.append(l[j])
# print(k)

# l = [2, 7, 9, 1, 4, 12]

# # Convert the list to a space-separated string
# str_list = " ".join(map(str, l))  # map(str, l) converts each element to a string

# # Now use split() on the string (this would split the string back to a list)
# w = str_list.split()

# # Print the new list after split
# print(type(str_list))

# l=[2,7,9,1,4,12]
# i=l[-1]
# j = " ".join(map(str, l))
# w = j.split()
# print( len(w))
# print(w)





# l = [1, 2, 3, 6, 9, 8, 7, 4, 5, 5, 7, 8]

# max_value = l[0]  # Initialize with the first element
# max_index = 0  # Initialize the index of the max value to 0
# length = len(l)

# # Iterate through the list to find the max value and its index
# for i in range(1, length):  # Start from the second element
#     if l[i] > max_value:
#         max_value = l[i]
#         max_index = i  # Update the index when a new max is found

# print("Index of max value:", max_index)


############-------tuple---------------------
# tp=()
# print(tp)
# print(type(tp))


# tp=("manish")
# print(tp)
# print(type(tp))


# tp=("manish","nik","manish")
# print(tp)
# print(type(tp))

# tp=(1,2,3,6,5,4,8,9,7,8)+(4,54,8,9,9,6,6,6,3,2,5)+(5,)
# print(tp[-2])
# print(tp[-2:-6])
# lst = list(tp)
# lst.append(123)
# lst.pop(2)
# lst.remove(2)
# tp=tuple(lst)
# count=tp.count(9)
# print(type(tp))
# print(tp)



# tp1=("Manish","avani","nik","pank")
# for i in tp1:
#     print(i)

# print("============= for loop with range==============")


# tp1=("Manish","avani","nik","pank")
# l=len(tp1)
# for i in range(l):
#     print(tp1[i])


# tp1=("Manish","avani","nik","pank")
# i=0
# l=len(tp1)
# while i<l:
#     print(tp1[i])
#     i+=1


# inputs=[]
# for i in range(5):
#     user=input("Enter the value:")
#     inputs.append(user)
#     tp=tuple(inputs)
#     print(tp)




# Creating a dictionary with mixed data types: int, char, list, and tuple
# my_dict = {
#     "int_key": 42,                         # Integer value
#     "char_key": "A",                       # Single character (string of length 1)
#     "list_key": [1, 2, 3, 4,["manish",5,6,8]],              # List of integers
#     "tuple_key": (10, 20, 30,(7,8,9,6)),             # Tuple with integers
# }
# print("Original dictionary:")
# print(my_dict)
# print(my_dict["int_key"])
# print(my_dict["char_key"])
# print(my_dict["list_key"])
# print(my_dict["tuple_key"])
# print(my_dict.keys())
# print(my_dict.values())
# my_dict.update({"mail_id":"manishmaurya9616@gmail.com"})
# print(my_dict)


# def print_pattern(n):
#     if n % 2 == 0:
#         print("Please enter an odd number.")
#         return

#     mid = n // 2  # The middle row index

#     for i in range(n):
#         # Calculate the number of @ symbols based on the row position
#         at_signs = "@" * (i + 1 if i <= mid else n - i)
        
#         if i == mid:
#             # Middle row with @ symbols followed by * symbols across the entire width
#             print(at_signs + "*" * n)
#         else:
#             # Other rows with @ symbols, spaces, and a single * at the end
#             print(at_signs + " " * (n - len(at_signs)) * 2 + "*")

# # Example usage:
# print_pattern(3)
# print()
# print_pattern(5)



# def print_numbers(num=1):
#     if num > 100:  # Base case to stop recursion
#         return
#     print(num)  # Print the current number
#     print_numbers(num + 1)  # Recursive call with the next number

# # Start the recursive function
# print_numbers()


# def fizz_buzz():
#     for i in range(1, 101):
#         if i % 3 == 0 and i % 5 == 0:
#             print("FizzBuzz")
#         elif i % 3 == 0:
#             print("Fizz")
#         elif i % 5 == 0:
#             print("Buzz")
#         else:
#             print(i)

# fizz_buzz()


# def find_large(nums):
#     return max(nums)
# print(find_large([1,2,3,6,9,8,7,4,5]))


# def print_numbers(num=0):
#     if num>100:
#         return
#     print(num)
#     print_numbers(num+1)
# print_numbers()

# def pattern(n):
#     for i in range(1,n+1):
#         print(" "*(n-i), end="")
#         print("*"*(2*i-1))
# pattern(5)


# def pattern(n):
#     for i in range(n,0,-1):
#         print(" "*(n-i),end="")
#         print("*"*(2*i-1))
# pattern(8)


# First part: Pyramid of "@" symbols
# n=int(input("Enter the odd number :"))
# for i in range(1,n+1,2):
#     spaces=(n-i)//2
#     print(" "*spaces+"@"*i+" "*spaces)

# Python3 implementation
# n=int(input("Enter the number:"))

# for i in range(n//2+2):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(2*i+1):
#         print("@",end="")
#     print()

# for i in range(n):
#     for j in range(n//2+1):
#         if (j>=n//2-i and j>=i-n//2):
#             print("*",end="")
#         else:
#             print(" ",end="")
#     for j in range(n):
#         if i==n//2:
#             print("@",end="")
#         else:
#             print(" ",end="")
#     for j in range(n//2+1):
#         if (j>=n//2-i and j>=i-n//2):
#             print("*",end="")
#     print()



# n = 5  # Example odd number

# if n % 2 == 0:
#     print("Please enter an odd number.")
# else:
#     mid = n // 2  # The middle row index

#     for i in range(n):
#         # Calculate the number of @ symbols based on the row position
#         if i <= mid:
#             at_signs = "@" * (i + 1)
#         else:
#             at_signs = "@" * (n - i)
        
#         # Middle row: @ symbols followed by * symbols
#         if i == mid:
#             print(at_signs + "*" * n)
#         else:
#             # Other rows: @ symbols + spaces + a single * at the end
#             spaces = " " * (n - len(at_signs) - 1)
#             print(at_signs + spaces + "*")



# n=int(input("Enter the number:"))
# if n==1:
#     print("it's not prime")
# if n>1:
#     for i in range(2,n):
#         if n%i==0:
#             print("It's not prime",n)
#             break
#     else:
#         print("Prime number",n)



# a = [2, 1, 3, 1, 4, 2, 6]
# a_set = set(a)
# print(a_set)


# a = {[2, 1, 3, 1, 4, 2, 6],[2, 1, 3, 1, 4, 2, 6]}       # it's not working due to unhashable   

# print(a)


#############3 ============          it's working only in tuple 

# a = {tuple([2, 1, 3, 1, 4, 2, 6]), tuple([2, 1, 3, 1, 4, 2, 6])}

# print(a)



# s={"a","b","c","d","e"}
# print(s)

# set = {"apple", "banana", "cherry"}
# for x in set:
#     print(x)

# s = {"apple", "banana", "cherry"}
# # b={"manish"}
# s.add("manish")  ######### it's not working due to unhashable
# # set.update(b)
# print(s)


# a={1,2,3,6,5,4,7,8,9}
# b={7,8,9,6,5,4,1,2,5,8,8,8,8,8}
# print(a.intersection(b))

# a=["manish","avni",1,21,3,6,6,6,5,4,4,4,7,8,"manish"]
# b=set(a)
# print(a)


# a = ["manish", "avni", 1, 21, 3, 6, 6, 6, 5, 4, 4, 4, 7, 8, "manish"]
# a = list(set(a))
# print(a)


# a = ["manish", "avni", 1, 21, 3, 6, 6, 6, 5, 4, 4, 4, 7, 8, "manish"]
# b={}
# for i in a:
#     if i not in b:
#         b[i] = True
#         b.update(i)
#     print(b)




# a = ["manish", "avni", 1, 21, 3, 6, 6, 6, 5, 4, 4, 4, 7, 8, "manish"]
# s=set()
# for i in a:
#     s.add(i)
# print(s)


# n=int(input("Enter the number"))
# for i in range(n):
#     print(' *' * n)


# n=int(input("Enter the number"))
# for i in range(n):
#     for j in range(n):
#         print("*", end="")
#     print()

# n=int(input("Enter the number"))
# for i in range(1,n+1):
#     print("*"*i)

# n=9
# for i in range(1,n+1):
#     for j in range(i):
#         print("*",end="")
#     print()


# n=9
# for i in range(1,n+1):
#     for j in range(n-i):    ##for spacing
#         print(" ",end="")
#     for j in range(i):
#         print("*",end="")
#     print()

# n=9
# for i in range(1,n+1):
#     for j in range(n-i):
#         print("*",end="")
#     print()


# class Student:
#     # name="manish"

#     def __init__(self) :
#         print("Hello")

#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks



# #create object
# s1=Student("manish",56)
# s2=Student("Pankaj",80)
# print(s1.name)
# print(s1.marks)
# print(s2.name)
# print(s2.marks)




class Student:
    def __init__(self,name,marks,id):
        self.name=name
        self.marks=marks
        self.id=id
    def greeting(self):
        print("Hello",self.name)
    def get_marks(self):
        return self.marks
s=Student("manish",90,12365)
print(s.name,s.marks,s.id)
s.greeting()
marks=s.get_marks()