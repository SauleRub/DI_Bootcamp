# 🌟 Exercise 1: Currencies
# Instructions
# Using the code above, implement the relevant methods and dunder methods which will output the results below.
# Hint : When adding 2 currencies which don’t share the same label you should raise an error.

# class Currency:
#     def __init__(self, currency, amount):
#         self.currency = currency
#         self.amount = amount

#     def __str__(self):
#         return f"{self.amount} {self.currency}" + ("s" if self.amount != 1 else "")

#     def __repr__(self):
#         return self.__str__()

#     def __int__(self):
#         return self.amount

#     def __add__(self, other):
#         if isinstance(other, int):
#             return self.amount + other
#         elif isinstance(other, Currency):
#             if self.currency == other.currency:
#                 return self.amount + other.amount
#             else:
#                 raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
#         else:
#             raise TypeError("Unsupported operand type for +")

#     def __iadd__(self, other):
#         if isinstance(other, int):
#             self.amount += other
#         elif isinstance(other, Currency):
#             if self.currency == other.currency:
#                 self.amount += other.amount
#             else:
#                 raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
#         else:
#             raise TypeError("Unsupported operand type for +=")
#         return self


# c1 = Currency('dollar', 5)
# c2 = Currency('dollar', 10)
# c3 = Currency('shekel', 1)
# c4 = Currency('shekel', 10)

# print(str(c1))  
# print(int(c1))  
# print(repr(c1))  

# print(c1 + 5)  
# print(c1 + c2)  

# c1 += 5
# print(c1)  

# c1 += c2
# print(c1)  

# print(c1 + c3)  


# 🌟 Exercise 2: Import
# Instructions
# In a file named func.py create a function that sum 2 numbers, and prints the result
# In a file named exercise_one.py import the function and call it to print the result
# Hint: You can use the the following syntaxes:

# 🌟 Exercise 3: String module
# Instructions
# Generate random String of length 5
# Note: String must be the combination of the UPPER case and lower case letters only. No numbers and a special symbol.
# Hint: use the string module

import random
import string

def generate_random_string(length=5):
    """Generates a random string of the given length containing only uppercase and lowercase letters."""
    letters = string.ascii_letters  # Contains 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return ''.join(random.choice(letters) for _ in range(length))

# Generate and print a random string
random_string = generate_random_string()
print(random_string)

# 🌟 Exercise 4 : Current Date
# Instructions
# Create a function that displays the current date.
# Hint : Use the datetime module.

from datetime import date

def display_current_date():
    current_date = date.today()
    print("Current date:", current_date)

display_current_date()


# Exercise 5 : Amount of time left until January 1st
# Instructions
# Create a function that displays the amount of time left from now until January 1st.
# (Example: the 1st of January is in 10 days and 10:34:01hours).

from datetime import datetime

def time_until_new_year():
    now = datetime.now()
    next_year = now.year + 1
    new_year = datetime(next_year, 1, 1)  
    time_left = new_year - now
    
    days = time_left.days
    hours, remainder = divmod(time_left.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    print(f"The 1st of January is in {days} days and {hours}:{minutes}:{seconds} hours.")

time_until_new_year()


# Exercise 6 : Birthday and minutes
# Instructions
# Create a function that accepts a birthdate as an argument (in the format of your choice), then displays a message stating how many minutes the user lived in his life.

from datetime import datetime

def minutes_lived(birthdate_str):
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d") 
    now = datetime.now()
    
    time_lived = now - birthdate  
    minutes = time_lived.total_seconds() // 60  
    print(f"You have lived approximately {int(minutes):,} minutes.")


birthdate_input = input("Enter your birthdate (YYYY-MM-DD): ")
minutes_lived(birthdate_input)


# Exercise 7 : Faker Module
# Instructions
# Install the faker module, and take a look at the documentation and learn how to properly implement faker in your code.
# Create an empty list called users. Tip: It should be a list of dictionaries.
# Create a function that adds new dictionaries to the users list. Each user has the following keys: name, adress, langage_code. Use faker to populate them with fake data.

from faker import Faker
fake = Faker()
print(fake.name())  