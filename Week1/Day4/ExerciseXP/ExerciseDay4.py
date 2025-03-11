# Exercise 1: Favorite Numbers

#Create a set called my_fav_numbers with all your favorites numbers.
#Add two new numbers to the set.
#Remove the last number.
#Create a set called friend_fav_numbers with your friend’s favorites numbers.
#Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.

my_fav_num = {2, 5, 7}
my_fav_num.add(22)
my_fav_num.add(30)
my_fav_num.remove(22)

friend_fav_num = {7, 11, 12}
our_num = my_fav_num.union (friend_fav_num)
print(our_num)

# Exercise 2: Tuple

#Given a tuple which value is integers, is it possible to add more integers to the tuple?

#not possible to add more, because tuple content cannot be changed

# Exercise 3: List

#Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];
#Remove “Banana” from the list.
#Remove “Blueberries” from the list.
#Add “Kiwi” to the end of the list.
#Add “Apples” to the beginning of the list.
#Count how many apples are in the basket.
#Empty the basket.
#Print(basket)

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")
apple_count = basket.count("Apples")
basket.clear()
print(basket)

# Exercise 4: Floats
# Recap – What is a float? What is the difference between an integer and a float?
# Create a list containing the following sequence of floats and integers (it should be a list with mixed types): 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).
# Can you think of another way to generate a sequence of floats?

float_list = [x * 0.5 for x in range (3, 11)]
print(float_list)

# Exercise 5: For Loop
# Use a for loop to print all numbers from 1 to 20, inclusive.
# Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.

for num in range(1, 21):
    print(num)

for num in range (1, 21, 2):
    print(num)

# Exercise 6: While Loop
# Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.

my_name = "Saule"
while True:
    user_name = input("Enter your name: ")
    if user_name == my_name: 
        break

# Exercise 7: Favorite fruits
# Ask the user to input their favorite fruit(s) (one or several fruits).
# Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
# Store the favorite fruit(s) in a list (convert the string of words into a list of words).
# Now that we have a list of fruits, ask the user to input a name of any fruit.
# If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
# If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.

fav_fruits = input("Enter your fav fruits and seperate it by space: ").split()
fruit_choice = input("Enter name of fruit: ")
if fruit_choice in fav_fruits:
    print("You chose fav fruit!!")
else:
    print("You chose different fruit, maybe you will like it.")

# Exercise 8: Pizza toppings
# Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
# As they enter each topping, print a message saying you’ll add that topping to their pizza.
# Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).

toppings = []
while True:
    topping = input("Enter pizza topping (or type 'stop' to finish): ")
    if topping.lower() == "stop":
        break
    toppings.append(topping)
    print(f"Adding {topping} on pizza!")
total_price = 10 + 2.5 * len(toppings)
print(f"You chose: {toppings}")
print(f"Total price ${total_price}")

# Exercise 9: Cinemax
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.

# Ask a family the age of each person who wants a ticket.

# Store the total cost of all the family’s tickets and print it out.

# A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
#Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
# At the end, print the final list.

ages = list(map(int, input("Enter family members and separate ages by SPACE: ").split()))
total_cost = sum(0 if age < 3 else 10 if age <= 12 else 15 for age in ages)
print(f"Total cost: ${total_cost}")
teenagers = ["Saule", "Ieva", "Arik", "Totti"]
allowed_teens = []
for teen in teenagers:
    age = int(input(f"Enter age of {teen}: "))
    if not (16 <= age <= 21):
        allowed_teens.append(teen)
print(f"Final list of allowed teens: {allowed_teens}")

# Exercise 10: Sandwich Orders
# sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
# The deli has run out of pastrami, use a while loop to remove all occurrences of “Pastrami sandwich” from sandwich_orders.
# We need to prepare the orders of the clients:
#Create an empty list called finished_sandwiches.
# One by one, remove each sandwich from the sandwich_orders while adding them to the finished_sandwiches list.
# After all the sandwiches have been made, print a message listing each sandwich that was made, such as:
# I made your tuna sandwich
# I made your avocado sandwich
# I made your egg sandwich
# I made your chicken sandwich

sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

finished_sandwitches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    finished_sandwitches.append(sandwich)
    print(f"Here is your {sandwich}")