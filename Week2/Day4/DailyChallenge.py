# Challenge 1 : Sorting


# Instructions
# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Use List Comprehension
# Example:

# Suppose the following input is supplied to the program: without,hello,bag,world
# Then, the output should be: bag,hello,without,world


input_string = input("Enter comma-separated words: ")

sorted_words = ','.join(sorted([word.strip() for word in input_string.split(',')]))

print("Sorted words:", sorted_words)

# Challenge 2 : Longest Word
# Instructions
# Write a function that finds the longest word in a sentence. If two or more words are found, return the first longest word.
# Characters such as apostrophe, comma, period count as part of the word (e.g. O’Connor is 8 characters long).

def longest_word(sentence):
    # Split the sentence into words
    words = sentence.split()
    
    # Find the word with the maximum length
    longest = max(words, key=len)
    
    return longest

# Test cases
print(longest_word("Margaret's toy is a pretty doll."))  
print(longest_word("A thing of beauty is a joy forever."))  
print(longest_word("Forgetfulness is by all means powerless!"))  