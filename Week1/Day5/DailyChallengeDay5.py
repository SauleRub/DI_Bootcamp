# Challenge 1
# Ask the user for a number and a length.
# Create a program that prints a list of multiples of the number until the list length reaches length.
# Examples

# number: 7 - length 5 ➞ [7, 14, 21, 28, 35]

# number: 12 - length 10 ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]

# number: 17 - length 6 ➞ [17, 34, 51, 68, 85, 102]

def letter_indexes(word):
    letter_dict = {}
    for index, letter in enumerate(word):
        if letter not in letter_dict:
            letter_dict[letter] = []
        letter_dict[letter].append(index)
    return letter_dict

word1 = "dodo"
word2 = "froggy"
word3 = "grapes"

print(letter_indexes(word1))  
print(letter_indexes(word2))  
print(letter_indexes(word3))  

   
# Challenge 2
# Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.
# Examples

# user's word : "ppoeemm" ➞ "poem"

# user's word : "wiiiinnnnd" ➞ "wind"

# user's word : "ttiiitllleeee" ➞ "title"

# user's word : "cccccaaarrrbbonnnnn" ➞ "carbon"

def affordable_items(items_purchase, wallet):
    
    wallet_amount = int(wallet.replace('$', '').replace(',', ''))
    
    affordable = []
    
    for item, price in items_purchase.items():
        item_price = int(price.replace('$', '').replace(',', ''))
        if item_price <= wallet_amount:
            affordable.append(item)
    
    affordable.sort()
    
    return affordable if affordable else "Nothing"

items1 = {
    "Water": "$1",
    "Bread": "$3",
    "TV": "$1,000",
    "Fertilizer": "$20"
}
wallet1 = "$300"
print(affordable_items(items1, wallet1))  

items2 = {
    "Apple": "$4",
    "Honey": "$3",
    "Fan": "$14",
    "Bananas": "$4",
    "Pan": "$100",
    "Spoon": "$2"
}
wallet2 = "$100"
print(affordable_items(items2, wallet2))  

items3 = {
    "Phone": "$999",
    "Speakers": "$300",
    "Laptop": "$5,000",
    "PC": "$1200"
}
wallet3 = "$1"
print(affordable_items(items3, wallet3))  
