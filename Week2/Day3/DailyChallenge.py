matrix = [
    ['7', 'i', 'i'],
    ['T', 's', 'x'],
    ['h', '%', '?'],
    ['i', ' ', '#'],
    ['s', 'M', ' '],
    ['$','a', ' '],
    ['#', 't', '%'],
    ['^', 'r', '!']
]

decoded_message = []

for col in range(len(matrix[0])):  
    for row in range(len(matrix)):  
        char = matrix[row][col]  
        if char.isalpha():  
            decoded_message.append(char)  

decoded_message_str = ''.join(decoded_message)

print(decoded_message_str)