# DailyChallengeDay1.py

import random

user_input = input("Enter a string that is exactly 10 characters: ")

if len(user_input) < 10:
    print("string not long enough")
elif len(user_input) > 10:
    print("string is too long")
else:
    print("perfect string")

    print(user_input[0])
    print(user_input[-1])

    for i in range(1, len(user_input)+1):
        print(user_input[:i])

    user_input_list = list(user_input)
    random.shuffle(user_input_list)
    jumbled_string = ''.join(user_input_list)
    print(jumbled_string)
    input_string = input("Enter a string: ")
print(input_string.upper())
