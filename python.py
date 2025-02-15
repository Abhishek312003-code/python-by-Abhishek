# write a program to store seven fruits in a list entered by user
fruits = []
f1 = input("enter the fruits name :")
fruits.append(f1)
f2 = input("enter the fruits name :")
fruits.append(f2)
f3 = input("enter the fruits name :")
fruits.append(f3)
f4 = input("enter the fruits name :")
fruits.append(f4)
f5 = input("enter the fruits name :")
fruits.append(f5)
f6 = input("enter the fruits name :")
fruits.append(f6)
f7 = input("enter the fruits name :")
fruits.append(f7)
print(fruits)

# write a program to accept marks of 6 students and display them in a sorted way
marks = []
m1 = int(input("enter the marks:"))
marks.append(m1)
m2 = int(input("enter the marks:"))
marks.append(m2)
m3 = int(input("enter the marks:"))
marks.append(m3)
m4 = int(input("enter the marks:"))
marks.append(m4)
m5 = int(input("enter the marks:"))
marks.append(m5)
m6 = int(input("enter the marks:"))
marks.append(m6)
marks.sort()
print(marks)

# check that tuple type cannot be changed in python
tuple = (2,6,9,"Abhishek")
tuple[2] = "Abhi"
print(tuple)
print(type(tuple))

# write a program to sum a list of 4 numbers
list = [1,89,76,98]
print(sum(list))

# write a program to count the number of zeroesin the following tuple:
tup = (1,3,4,0,4,0,0,8,0,6,0,4)
print(tup.count(0))

# write a program in to create a dictionary of hindi words as their english translation
# provide user with an option to look it up
words ={
    "madad" : "help",
    "kutta" : "dog",
    "class" : "kaksha"
}

word = input("enter the word you want meaning of :")
print(words[word])

# write a program to input eight numbers from the user and siplay all the unique numbers(once)
s = set()
n = input("Enter number: ")
s.add(int(n))  
n = input("Enter number: ")
s.add(int(n))  
n = input("Enter number: ")
s.add(int(n))  
n = input("Enter number: ")
s.add(int(n))  
n = input("Enter number: ")
s.add(int(n))  
n = input("Enter number: ")
s.add(int(n))  
n = input("Enter number: ")
s.add(int(n))  
n = input("Enter number: ")
s.add(int(n))  

print(s)

# can we have a set with 18(int)
# and "18" (str) as a value in it?
s = set()
s.add(18)
s.add("18")
print(s)

# what will be the length of following set s:
s = set()
s.add(20)
s.add(20.0)
s.add('20') #length of s after these operations
print(len(s))

# what is the type of 's'
s ={}
print(type(s))
# output : <class 'dict'>

# create an empty dictionary. allow 4 friends to enter their favorite language
# as value and use key as their names.assume that the names are unique
d = {}

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})


print(d)

#if the names of 2 friends are same what will happen to the program in problem 6?
# The values entered later will be updated
# if languages of two friends are same; what will happen to the program in problem 6?
# Nothing will happen. The values can be same

# can you change the values inside a list which contained in set S?
s = {8,7,12,"Abhishek",[1,2]}
s[4][0] = 9
# it will give a error we cannot include list in a set and list is unhashable


# CONDITIONAL EXPRESSIONS
# write a program to print yes hwn the age entered by the user is greater than or equal to 18
age = int(input("enter the age :"))

if age >= 18:
    print("yes")
else:
    print("No") 
print("End of Program")

# write a program to find the greatest of four numbers entered ny user
a1 = int(input("enter the number 1:"))
a2 = int(input("enter the number 2:"))
a3 = int(input("enter the number 3:"))
a4 = int(input("enter the number 4:"))

if (a1>a2 and a1>a3 and a1>a4):
   print("greatest number is a1", a1)


elif (a2>a1 and a2>a3 and a2>a4):
   print("greatest number is a2", a2)


elif (a3>a1 and a3>a2 and a3>a4):
   print("greatest number is a3", a3)


elif (a4>a1 and a4>a2 and a4>a3):
   print("greatest number is a4", a4)

# write a program to find out whether a student has passed or failed if it required a total of  40%
# and at least 33% in each subject to pass.Assume 3 subjects and take marks as an input from the user
marks1 = int(input("Enter Marks 1: "))
marks2 = int(input("Enter Marks 2: "))
marks3 = int(input("Enter Marks 3: "))

# Check for total percentage
total_percentage = (100*(marks1 + marks2 + marks3))/300

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("You are passed:", total_percentage)

else:
    print("You failed, try again next year:", total_percentage)

#.a spam comment is defined as a text containing following keywords:
# "make alot of money","buy now", "subscribe this","click this".write a program
# to detect these spams
p1 = "Make a lot of money"
p2 = "buy now"  
p3 = "subscribe this"  
p4 = "click this"

message = input("Enter your comment: ")

if((p1 in message) or (p2 in message )or (p3 in message) or (p4 in message)):
    print("This comment is a spam")

else:
    print("This comment is not a spam")
 
# write a program to find whether a given username contains less than 10 characters or not?
username = input("Enter username: ")

if(len(username)<10):
    print("Your username contains less than 10 characters")
else:
    print("Your username contains more than or equal to 10 characters")

# write a program to finds out whether a given name is present in a list or not
l = ["Abhishek", "Rohan", "Shubham", "Divya"]

name = input("Enter your name: ")

if(name in l):
    print("Your name is in the list")
else:
    print("Your name is not in the list")

# write a program to calculate the grade of a student from his marks from the following scheme:
# 90 - 100 => Ex
# 80 - 90 => A
# 70 - 80 => B
# 60 - 70 => C
# 50 - 60 => D
# <50 => F
marks = int(input("Enter your marks: "))

if(marks<=100 and marks>=90):
    grade = "Ex"
elif(marks<90 and marks>=80):
    grade = "A"
elif(marks<80 and marks>=70):
    grade = "B"
elif(marks<70 and marks>=60):
    grade = "C"
elif(marks<60 and marks>=50):
    grade = "D"
elif(marks<50):
    grade = "F"

print("Your grade is:", grade)

# write a program to find out whether a given post is talking about "Abhishek" or not?
post = input("Enter the post: ")

if("Abhishek" in post.lower()):
    print("This post is talking about Abhishek")


# loops in python
l = ["Abhishek" ,False,"help","case","popular","junior"]
i = 0
while (i<len(l)):
    print(l[i])
    i += 1

# write a program to print multiplication of a given number using loop
n = int(input("enter the number :"))
for i in range (1,11):
    print(f" {n} * {i} = {n*i}")

# write a program to greet all the person names stored in a list "l" and which starts with S
    # l = ["Abhishek" , "soham" , "Sachin" , "Rahul"]
l = ["Abhishek" , "Soham" , "Sachin" , "Rahul"]
for name in l:
    if(name.startswith("S")):
        print(f"Hello {name}")

# write a program of problem no. 1 using while loop
n = int(input("enter the number :"))
i = 1
while (i < 11):
    print(f" {n} * {i} = {n*i}")
    i += 1

# write a program to find whether a givem number is prime or not
n = int(input("Enter a number: "))

for i in range(2, n):
    if(n%i) == 0:
        print("Number is not prime")
        break
else:
    print("Number is prime")

# write the program to find the sum of first n natural numbers using while loop
n = int(input("Enter the number: "))
i = 1
sum = 0
while(i<=n):
    sum += i
    i+=1

print(sum)

# write a program to find the factorial of a given number using for loop
# 5! = 1 X 2 X 3 X 4 X 5
n = int(input("Enter the number: "))
product = 1
for i in range(1, n+1):
    product = product * i

print(f"The factorial of {n} is {product}")

# write the program to print the following star pattern
# *
# ***
# ***** for n = 3
n = int(input("Enter the number: "))
for i in range(1, n+1):
    print(" "* (n-i), end="")
    print("*"* (2*i-1), end="")
    print("")

#write the program to print following star pattern
# *
# **
# *** for n = 3
n = int(input("Enter the number: "))
for i in range(1, n+1): 
    print("*"* i, end="")
    print("")

# write the program to print following star pattern
'''

***
* *       for n = 3
***


'''
n = int(input("Enter the number: "))
for i in range(1, n+1): 
    if(i==1 or i==n):
        print("*"* n, end="")
    else:
        print("*", end="")
        print(" "* (n-2), end="")
        print("*", end="")
    print("")

# write a program to print multiplication table of n using for loops in reversed
n = int(input("Enter the number: "))

for i in range(1, 11):
    print(f"{n} X {11 -i} = {n*(11-i)}")


# FUNCTIONS AND RECURSION
# write a program using function to find greatest of 3 numbers

def greatest(a,b,c):
    
    if (a>b and a>c):
        return a
    elif (b>a and b>c):
        return a
    elif (c>a and c>b):
        return c

print(greatest(12,78,98))

# write a python program using function to convert celsius into fahrenheit
def c_to_f(c):
    return (9/5) * c + 32

c = float(input("Enter the temperature in Celsius: "))
f = c_to_f(c)
print(f"{round(f, 2)}° Fahrenheit")
