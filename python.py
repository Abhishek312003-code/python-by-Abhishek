# #i am learning a python language
# #basic code of python
# print("hello world")
# # write a program to print twinkle twinkle little star poem in python
# # here we use double triple double cot and we use triple single cot to print multilines
# print("""Song Lyrics
# # Twinkle twinkle little star.
# # How I wonder what you are.
# # Up above the world so high.
# # Like a diamond in the sky.
# # Twinkle twinkle little star.
# # How I wonder what you are.""")

# # Write a Python program to print the contents of a directory using the OS module. Search online for the function that does that.
# import os   
# # Specify the directory path
# directory_path = '/'

# # List all entries in the specified directory
# contents = os.listdir(directory_path)

# # Print the entries
# for item in contents:
#      print(item)

# # some practice questions on variables datatypes
# #  1st wap on add two numbers
# a = int(input("enter first number :"))
# b = int(input("enter second number :"))
# sum = a + b
# print(sum)

# # 2nd Write a Python program to find remainder when
# # a number is divided by z
# a = 66
# b = 5
# print("the remainder is :", a % b)

# # 3rd Check the type of the variable assigned using input () function
# a = input("enter the value of a :")
# print(type(a))

# # 4th use Comparison operators to find out whether a given Variable 'a' is greater than 'b' or not. Take a = 34 and b=80
# a = 34
# b = 80 
# print(a > b)

# # 5th Write a python program to find average of two
# # numbers entered by the user
# a = int(input("enter the first number :"))
# b = int(input("enter the second number :"))
# print(" the average of two number is :" ,(a + b) / 2)

# # 6th Write a python program to calculate the square of the number entered by the user 
# a = int(input("enter your number :"))
# print("the sqaure of the number :" , a ** 2)

# a = "nfwhfwnjnwmicjwojciwjiwkj"
# print (a [1 : 9]) 
# print(a [1 : 9 : 4])

# # escape sequence characters 
# a = "Abhishek is a student \n also he is 21 years \"old\" \t better "
# print(a)

# # Write a Python program to display a user entered name followed by Good Afternoon using 
# # input function
# name = input("enter the name :")
# print("Good Afternoon" , name)

# # Write a program to fill in a letter template given below with
# # name and date.
# letter = '''Dear <|NAME|>
#  You are selected!
#  <|Date|> '''
# print(letter.replace("<|NAME|>", "Abhishek").replace("<|Date|>", "08 February 2025"))

# #write a program to detect double spaces in a string 
# #replace the double space from problem 3 with single spaces
# name = "Abhishek is a  good boy"
# print(name.find("  "))
# print(name.replace("  "," "))

# # white a progrom to format the following letter using escape sequence characters.
# letter = "Dear Harry,\n\tThis Python Course is nice.\n Thanks!"
# print(letter)
#  loop code given by friend 
name = "Abhishek"
A = int(input("enter the number :"))
for i in range (A):
    print(name) 
    






