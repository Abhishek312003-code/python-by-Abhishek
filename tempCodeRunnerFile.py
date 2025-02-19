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
