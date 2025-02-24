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





# Write a program to store 10 country names entered by the user in a list and print them in reverse order.
# Create an empty list to store country names
countries = []

for i in range(10):
    country = input(f"Enter country name {i+1}: ")
    countries.append(country)

print("\nCountries in reverse order:")
for country in reversed(countries):  
    print(country)

# Take a list of numbers from the user and remove duplicate elements from it.
numbers =list(map(int, input("Enter the numbers separated by commas: ").split(",")))
unique_numbers = list(set(numbers))
print("list after removing duplicate numbers :",unique_numbers)

# Create a tuple of 5 numbers, take an input from the user, and check whether the number exists in the tuple or not.
numbers = (20,30,80,89,55,65)
user_input = (int(input("enter the number to check:")))

if user_input in numbers:
    print("number is exists in the tuple")
else:
    print("number is not exist in the list")

# Write a program to swap the first and last elements of a given list
numbers = list(map(int, input("Enter the numbers separated by commas: ").split(',')))
if len(numbers) >= 2:
    numbers[0], numbers[-1] = numbers[-1], numbers[0]

print("List after swapping first and last numbers:", numbers)

# Create a tuple (10, 20, 30, 40, 50), and try changing the second value. Observe the error.
numbers = (10, 20, 30, 40, 50)
numbers[2] = 9

# Write a program to create a dictionary of 5 student names as keys and their marks as values. Then print the student with the highest marks.
student = {
    "Abhishek" : 21,
    "mohan" : 98,
    "Ronit" : 90,
    "Anurag" : 89,
    "himanshu" : 87
}
for name ,marks in student.items():
    if marks == max(student.values()):
        print(name,"has the highest marks :",marks)

# Create a dictionary where keys are numbers from 1 to 10 and values are their squares.
squares = {
    1 : 1**2,
    2 : 2**2,
    3 : 3**2,
    4 : 4**2,
    5 : 5**2,
    6 : 6**2,
    7 : 7**2,
    8 : 8**2,
    9 : 9**2,
    10:10**2
}
print(squares)

# Write a program to take input of a word from the user and translate it into another language using a dictionary.
translations = {
    "hello": "नमस्ते",
    "thank you": "धन्यवाद",
    "please": "कृपया",
    "yes": "हाँ",
    "no": "नहीं",
    "goodbye": "अलविदा",
    "love": "प्यार",
    "food": "खाना",
    "water": "पानी",
    "friend": "मित्र"
}
word = input("enter an english word to translate into hindi :").lower()
if word in translations:
    print("hindi translation of this word is :",translations[word])
else:
    print("translation is not available")

# Modify the dictionary you created in Question 6 and update the marks of one student.
student = {
    "Abhishek" : 21,
    "mohan" : 98,
    "Ronit" : 90,
    "Anurag" : 89,
    "himanshu" : 87
}
student["Abhishek"] = 89
student["Anjali"] = 87
del student["himanshu"]
print(student)

# Take a sentence as input and count the frequency of each word using a dictionary.
sentence = input("enter the sentnece :")
words = sentence.split()
word_frequency ={}
for word in words:
    word_frequency[word]= word_frequency.get(word, 0) + 1
print(word_frequency)

# Create a program that takes 10 numbers from the user and stores only unique numbers in a set.
unique_numbers = set()
for i in range (10):
  num =int(input(f"enter the numbers {i+1}:"))
  unique_numbers.add(num)
print("unique_numbers",unique_numbers) 

# Write a program to check whether two sets {1, 2, 3, 4} and {3, 4, 5, 6} have any common elements
set1 = {1,2,3,4}
set2 = {3,4,5,6}

common_elements = set1 & set2
if common_elements:
    print("common elements :",common_elements)
else:
    print("no common elements")

# Given a set {5, 10, 15, 20, 25}, remove an element entered by the user.
set = {5,10,15,20,25}
num_to_remove = int(input("enter the number :"))

if num_to_remove in set:
    set.remove(num_to_remove)
    print("updated set :",set)
else :
    print("number not found in the set")

# Create a set containing both integers and strings and print its length.
set1 = {1,3,45,"Abhishek","Abhi","abhaa","Chhabra"}
print("length of the set :",len(set1))

# Write a program to find the union and intersection of two sets.
set1 = {1,2,3,4,5,6,7}
set2 ={9,8,7,6,5,4,3}

union = set1 | set2  #combine the unique elements
intersection = set1 & set2 #common elements
print("union of set1 and set2 :",union)
print("intersection of set1 and set2 :",intersection)

# Take a number from the user and check whether it is even or odd.
number = int(input("enter the number :"))
if number%2 ==0:
    print("number is even")
else:
    print("number is odd")

# Write a Python program that takes a percentage from the user and assigns a grade based on the following conditions:
# 90-100: A+
# 80-89: A
# 70-79: B
# 60-69: C
# 50-59: D
# <50: Fail
marks = int(input("enter the number :"))
if (marks <=100 and marks > 90):
     print(" Grade : A+")
elif (marks <= 89 and marks> 80):
    print("Grade : A")
elif (marks <= 79 and marks> 70):
    print("Grade : B")
elif (marks <= 69 and marks> 60):
    print("Grade : C")
elif (marks <= 59 and marks > 50):
    print("Grade :D")
else :
    print("Failed")

# Write a program to check if a given year is a leap year or not.
year = int(input("enter the year :"))
if (year % 4 == 0 and year % 100 != 0)or (year %400 == 0):
    print("this year is leap year")
else:
    print("this year is not a leap year")

# Write a program that takes three sides of a triangle as input and checks whether the triangle is valid or not
a = int(input("enter the first side:"))
b = int(input("enter the second side:"))
c = int(input("enter the third side:"))

if (a + b > c) and (a + c > b) and (b + c > a):
    print("the given sides forms a valid triangle")
else :
    print("the sides forms an invalid triangle")

# Write a program to check whether a given string is a palindrome (same when reversed).
word = (input("enter the word to check:"))
if word == word[::-1]:
    print("its a palindrome")
else:
    print("its not a palindrome")

# Print the multiplication table of a number using a for loop
num = int(input("enter the number :"))
print("multiplication table of :",num)
for i in range (11):
    print(f"{num} * {i} = {num * i}")

# Print all prime numbers between 1 to 50 using a loop.
for num in range(2,51):
  for i in range(2,num):
    if num % i == 0:
       break
  else:
    print(num, end=" ")

# Write a program to find the sum of digits of a number
n = int(input("Enter the number: "))
sum_of_digits = 0
while n > 0:
    sum_of_digits += n % 10
    n //= 10
print("sum of digits :",sum_of_digits)

# Take an input n and print a right-angled triangle pattern using *
n = int(input("enter the number of rows:"))
for i in range(n+1):
    print("*" *i)

# Print the Fibonacci series up to n terms using a while loop.
n = int(input("enter the number of terms:"))  # Ask the user for the number of terms
a,b = 0,1  # Initialize the first two Fibonacci numbers (0 and 1)
count = 0  # Initialize a counter to keep track of how many terms have been printed
while count < n:  # Loop will continue until we print 'n' terms
    print(a , end = " ") # Print the current value of 'a' (Fibonacci number)
    a,b = b,a +b   # Update 'a' and 'b' for the next Fibonacci numbers
    count += 1  #increase the counter by 1 to track printed terms.

