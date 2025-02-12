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

    






