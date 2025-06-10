# Exercise 1: Hello World
# Print the following output in one line of code:
# Hello world
# Hello world
# Hello world
# Hello world

print("Hello world\nHello world\nHello world\nHello world")

# Exercise 2: Some Math
# Write code that calculates the result of: (99^3)*8

print(99**3 * 8)

# Exercise 3: What is the output?
# Predict the output of the following:
# 5 < 3
# 3 == 3
# 3 == "3"
# "3" > 3
# "Hello" == "hello"

print(5<3)
print(3==3)
print(3=="3")
#print("3">3) #TypeError: '>' not supported between instances of 'str' and 'int'
print("Hello" == "hello")

# Exercise 4: Your computer brand
# Create a variable called computer_brand and print a sentence about it.

computer_brand = "Asus"
print(f"I have {computer_brand} computer.")

# Exercise 5: Your information
# Create variables for name, age, shoe_size, and info sentence.

name = "Saule"
age = 25
shoe_size = 38
info = f"My name is {name}, I am {age} years old and my shoe size is {shoe_size}."
print(info)

# Exercise 6: A & B
# Compare two numbers and print "Hello World" if a is greater than b.

a = 20
b = 7

if a > b:
    print("Hello World") 

# Exercise 7: Odd or Even
# Ask the user for a number and determine if it's odd or even.

number = int(input("Choose number:"))
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")   

# Exercise 8: What's your name?
# Ask the user for their name and compare it to yours.

user_name = input("Enter your name: ")

if user_name.lower() == name.lower():
    print("YEY! We Match! Your name is prettiest!")
else:
    print(f"Sadly you're not Saule, but still nice to meet you {user_name}!")

# Exercise 9: Tall enough to ride a roller coaster
# Ask for the user's height and check if they can ride.

height = int(input("What's your height in cm? "))

if height > 145:
    print("Good Job! You're tall enough to ride!")
else:
    print("Sorry, you are too small to ride, come back when you are taller.")    