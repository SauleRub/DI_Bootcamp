# Read the file line by line
# Read only the 5th line of the file
# Read only the 5 first characters of the file
# Read all the file and return it as a list of strings. Then split each word
# Find out how many occurences of the names "Darth", "Luke" and "Lea" are in the file
# Append your first name at the end of the file
# Append "SkyWalker" next to each first name "Luke"

# with open("names.txt", "r") as file:
#     text = file.read()
#     print(text)

file_path = "/Users/saulerub/DI_Bootcamp/Week4/Day1/names.txt"

try:
    with open(file_path, "r") as file:
        print("File opened successfully!")
        print(file.readline())  
except FileNotFoundError:
    print("File not found!")
except Exception as e:
    print("Error:", e)

try:
    with open(file_path, "r") as file:
        lines = file.readlines()
        print(lines[4].strip()) 
except FileNotFoundError:
    print("File not found!")
except Exception as e:
    print("Error:", e)


with open(file_path, "r") as file:
    print(file.read(5))  

with open(file_path, "r") as file:
    content = file.read()
    words = content.split()  
    print(words) 

with open(file_path, "r") as file:
    content = file.read()
    print("Darth:", content.count("Darth"))
    print("Luke:", content.count("Luke"))
    print("Lea:", content.count("Lea"))

with open(file_path, "a") as file:
    file.write("\nSaule")  

with open(file_path, "r") as file:
    content = file.read()

content = content.replace("Luke", "Luke SkyWalker")

with open(file_path, "w") as file:
    file.write(content)