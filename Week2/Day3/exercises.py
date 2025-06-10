# 🌟 Exercise 1 : What are you learning ?
# Instructions
# Write a function called display_message() that prints one sentence telling everyone what you are learning in this course.
# Call the function, and make sure the message displays correctly.

def display_message():
    print(f"heyy")
display_message()

# 🌟 Exercise 2: What’s your favorite book ?
# Instructions
# Write a function called favorite_book() that accepts one parameter called title.
# The function should print a message, such as "One of my favorite books is <title>".
# For example: “One of my favorite books is Alice in Wonderland”
# Call the function, make sure to include a book title as an argument when calling the function.

def favorite_book(title):
    print(f"I love to read {title}")

favorite_book("Harry Potter")

# 🌟 Exercise 3 : Some Geography
# Instructions
# Write a function called describe_city() that accepts the name of a city and its country as parameters.
# The function should print a simple sentence, such as "<city> is in <country>".
# For example “Reykjavik is in Iceland”
# Give the country parameter a default value.
# Call your function.

def describe_city(city, country="Israel"):
    print(f"{city} is in {country}")

describe_city("Kaunas", "Lithuania")
describe_city("Tel Aviv")

# Exercise 4 : Random
# Instructions
# Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100. Use the random module.
# Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers.

import random
def dif_num(user_num):
    if 1<= user_num <= 100:
        random_num = random.randint(1, 100)
        if user_num == random_num:
            print("Congrats!! You guessed the number!")
        else:
            print(f"Sorry... Your number: {user_num}, random number: {random_num}")
    else:
        print("You need to enter number between 1 and 100")

user_input = int(input("Enter a number between 1 and 100 "))

dif_num(user_input)

# 🌟 Exercise 5 : Let’s create some personalized shirts !
# Instructions
# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
# The function should print a sentence summarizing the size of the shirt and the message printed on it, such as "The size of the shirt is <size> and the text is <text>"
# Call the function make_shirt().

# Modify the make_shirt() function so that shirts are large by default with a message that reads “I love Python” by default.
# Call the function, in order to make a large shirt with the default message
# Make medium shirt with the default message
# Make a shirt of any size with a different message.

# Bonus: Call the function make_shirt() using keyword arguments.


def make_shirt(size = "M", text = "Shalom"):
    print(f"The size of the shirt is {size} and the text is {text} ")

make_shirt("S", "Hello")
make_shirt("L")
make_shirt()
make_shirt(text="Crazy code", size="XXS")

# 🌟 Exercise 6 : Magicians …
# Instructions
# Using this list of magician’s names

# magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

# Create a function called show_magicians(), which prints the name of each magician in the list.
# Write a function called make_great() that modifies the original list of magicians by adding the phrase "the Great" to each magician’s name.
# Call the function make_great().
# Call the function show_magicians() to see that the list has actually been modified.

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians(magician_names):
    for magician in magician_names:
        print(f"Hello magicians {magician} ")

def make_great(magician_names):
    for i in range(len(magician_names)):
        magician_names[i] = magician_names[i] + " the Great"

make_great(magician_names)

show_magicians(magician_names)


# 🌟 Exercise 7 : Temperature Advice
# Instructions
# Create a function called get_random_temp().
# This function should return an integer between -10 and 40 degrees (Celsius), selected at random.
# Test your function to make sure it generates expected results.

# Create a function called main().
# Inside this function, call get_random_temp() to get a temperature, and store its value in a variable.
# Inform the user of the temperature in a friendly message, eg. “The temperature right now is 32 degrees Celsius.”

# Let’s add more functionality to the main() function. Write some friendly advice relating to the temperature:
# below zero (eg. “Brrr, that’s freezing! Wear some extra layers today”)
# between zero and 16 (eg. “Quite chilly! Don’t forget your coat”)
# between 16 and 23
# between 24 and 32
# between 32 and 40

# Change the get_random_temp() function:
# Add a parameter to the function, named ‘season’.
# Inside the function, instead of simply generating a random number between -10 and 40, set lower and upper limits based on the season, eg. if season is ‘winter’, temperatures should only fall between -10 and 16.
# Now that we’ve changed get_random_temp(), let’s change the main() function:
# Before calling get_random_temp(), we will need to decide on a season, so that we can call the function correctly. Ask the user to type in a season - ‘summer’, ‘autumn’ (you can use ‘fall’ if you prefer), ‘winter’, or ‘spring’.
# Use the season as an argument when calling get_random_temp().

# Bonus: Give the temperature as a floating-point number instead of an integer.
# Bonus: Instead of asking for the season, ask the user for the number of the month (1 = January, 12 = December). Determine the season according to the month.

import random

def get_random_temp(season):
    if season == 'winter':
        lower, upper = -10, 16
    elif season == 'spring':
        lower, upper = 0, 20
    elif season == 'summer':
        lower, upper = 16, 32
    elif season == 'autumn':
        lower, upper = 5, 20
    else:
        return "There is no such season"
    
    return round(random.uniform(lower, upper), 2)

def temp_advice(temp):
    if temp < 0:
        print("Super cold!!! Wear a winter coat and a hat!")
    elif 0 <= temp <= 16:
        print("Chilly temp! Wear a coat!")
    elif 16 < temp <+ 23:
        print("Really nice weather! Might need a sweather though!")
    elif 24 <= temp <= 32:
        print("Wow! Completely summer vibes! Wear only summer clothes and don't forget sunscreen!")
    elif 32 < temp <= 40:
        print("Super HOT! Better stay inside!")

def main():
    month = int(input("Enter the month number (1 = Jan, 12 = Dec): "))
    if 3 <= month <= 5:
        season = 'spring'
    elif 6 <= month <= 8:
        season = 'summer'
    elif 9 <= month <= 11:
        season = 'autumn'
    else:
        season = 'winter'

    temp = get_random_temp(season)

    print(f"Temp now is {temp} degrees C ")
    temp_advice(temp)

main()


# 🌟 Exercise 8 : Star Wars Quiz
# Instructions
# This project allows users to take a quiz to test their Star Wars knowledge.
# The number of correct/incorrect answers are tracked and the user receives different messages depending on how well they did on the quiz.

# Create a function that asks the questions to the user, and check his answers. Track the number of correct, incorrect answers. Create a list of wrong_answers
# Create a function that informs the user of his number of correct/incorrect answers.
# Bonus : display to the user the questions he answered wrong, his answer, and the correct answer.
# If he had more then 3 wrong answers, ask him to play again.


data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]

def ask_function():
    correct_count = 0
    incorrect_count = 0
    wrong_answers = []

    for item in data:
        question = item["question"]
        correct_answer = item["answer"]

        user_answer = input(f"{question} ")

        if user_answer.lower() == correct_answer.lower():
            correct_count += 1
        else:
            incorrect_count += 1
            wrong_answers.append({
                "question": question,
                "user_answer": user_answer,
                "correct_answer": correct_answer
            })
    
    return correct_count, incorrect_count, wrong_answers

def show_results(correct_count, incorrect_count, wrong_answers):
    print(f"\nYou got {correct_count} correct answers and {incorrect_count} incorrect answers.")
    
    if incorrect_count > 0:
        print("\nYou answered the following questions incorrectly:")
        for answer in wrong_answers:
            print(f"Question: {answer['question']}")
            print(f"Your answer: {answer['user_answer']}")
            print(f"Correct answer: {answer['correct_answer']}")
            print("-" * 50)

def play_quiz():
    correct_count, incorrect_count, wrong_answers = ask_function()
    show_results(correct_count, incorrect_count, wrong_answers)

    if incorrect_count > 3:
        print("\nYou got more than 3 wrong answers. Let's try again!")
        play_quiz()

play_quiz()