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
