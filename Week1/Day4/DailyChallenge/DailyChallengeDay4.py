# Challenge 1
# Ask the user for a number and a length.
# Create a program that prints a list of multiples of the number until the list length reaches length.
# Examples

# number: 7 - length 5 ➞ [7, 14, 21, 28, 35]
# number: 12 - length 10 ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]
# number: 17 - length 6 ➞ [17, 34, 51, 68, 85, 102]

def multiples_of_number(number, length):
    multiples = []
    for num in range(1, length + 1):
        multiples.append(number * num)
    return multiples

print(multiples_of_number(7, 5))
print(multiples_of_number(12, 10))
print(multiples_of_number(17, 6))


# Challenge 2
# Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.
# Examples

#user's word : "ppoeemm" ➞ "poem"
#user's word : "wiiiinnnnd" ➞ "wind"
#user's word : "ttiiitllleeee" ➞ "title"
#user's word : "cccccaaarrrbbonnnnn" ➞ "carbon"

def remove_consecutive_dub(word):
    result = [word[0]]
    for num in range(1, len(word)):
        if word[num] != word[num - 1]:
            result.append(word[num])
    return ''.join(result)

print(remove_consecutive_dub("ppoeemm"))
print(remove_consecutive_dub("wiiinnnnd"))
print(remove_consecutive_dub("ttiiitllleeee"))
print(remove_consecutive_dub("cccccaaarrrbbonnnn"))
