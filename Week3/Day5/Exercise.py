# 🌟 Exercise 1 – Random Sentence Generator
# Instructions
# Description: In this exercise we will create a random sentence generator. We will do this by asking the user how long the sentence should be and then printing the generated sentence.

# Hint : The generated sentences do not have to make sense.

# Download this word list

# Save it in your development directory.

# Create a function called get_words_from_file. This function should read the file’s content and return the words as a collection. What is the correct data type to store the words?

# Create another function called get_random_sentence which takes a single parameter called length. The length parameter will be used to determine how many words the sentence should have. The function should:
# use the words list to get your random words.
# the amount of words should be the value of the length parameter.

# Take the random words and create a sentence (using a python method), the sentence should be lower case.

# Create a function called main which will:

# Print a message explaining what the program does.

# Ask the user how long they want the sentence to be. Acceptable values are: an integer between 2 and 20. Validate your data and test your validation!
# If the user inputs incorrect data, print an error message and end the program.
# If the user inputs correct data, run your code.

import os

def get_words_from_file():
    file_path = "/Users/saulerub/DI_Bootcamp/Week3/Day5/words.txt"
    with open(file_path, "r") as file:
        words = file.read().splitlines()
    return words

import random

def get_random_sentence(length):
    words = get_words_from_file()  # Get words from the file
    if length < 2 or length > 20:
        raise ValueError("Length must be between 2 and 20.")

    sentence = " ".join(random.choices(words, k=length))
    return sentence.lower()

def main():
    print("Welcome to the Random Sentence Generator!")
    print("You can choose a sentence length between 2 and 20 words.")

    try:
        length = int(input("Enter the length of the sentence: "))
        if 2 <= length <= 20:
            sentence = get_random_sentence(length)
            print("\nYour random sentence:")
            print(sentence)
        else:
            print("Error: Please enter a number between 2 and 20.")
    except ValueError:
        print("Error: Please enter a valid integer.")

if __name__ == "__main__":
    main()


# 🌟 Exercise 2: Working with JSON

# Access the nested “salary” key from the JSON-string above.
# Add a key called “birth_date” to the JSON-string at the same level as the “name” key.
# Save the dictionary as JSON to a file.

import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

data = json.loads(sampleJson)

salary = data["company"]["employee"]["payable"]["salary"]
print("Salary:", salary)  

data["company"]["employee"]["birth_date"] = "1999-09-02"

with open("updated_data.json", "w") as file:
    json.dump(data, file, indent=4)  

print("Updated JSON saved to 'updated_data.json'")