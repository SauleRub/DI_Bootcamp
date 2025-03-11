#Given this list:
#list1 = [5, 10, 15, 20, 25, 50, 20]
#find the value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of a value


list1 = [5, 10, 15, 200, 25, 50, 20]

twenty_index = list1.index(20)

print(twenty_index)

list1[twenty_index] = 200

print(list1)


#a_tuple = (10, 20, 30, 40)

#Expected output:

#a_tuple = (10, 20, 30, 40)
# Your code
# should print 10
# should print 20
# should print 30
# should print 40

a_tuple = (10, 20, 30, 40)

a = a_tuple[0]
b = a_tuple[1]
c = a_tuple[2]
d = a_tuple[3]


cities = ["London", "San Francisco", "Paris", "Barcelona"]


for city in cities:
    print("I once went to", city)

for num in range(0,11,2):
    print(num)


sum_this_list = [1,2,3,4,5]

print(sum(sum_this_list))


 #Accept a number from the user and print its multiplication table

num = int(input("Enter a number: "))

print(f"Multiplication table of {num}:")
for number in range(1,11):
    print(f"{num}x{number} = {num * number}")


#while loop

a_number = 1

while a_number < 12:
    print(a_number)
    a_number += 1

#password

password = ''
while password != '123':
    password = input('What is the top secret password? ')
print('You guessed the right password!')


#Print the numbers from 1 to 10 using while loop

a_number = 1

while a_number <=10:
    print(a_number)
    a_number+=10


active = True

while active: 
    city = input("Please enter the name of a city you have visited (enter 'quit' when you are finished): ")
    if city == 'quit':
        break
    elif city == 'leave me alone':
        active = False
    elif city == 'stop':
        active = False
    else:
        print("I'd love to go to", city)

print("Goodbye !")

g = 1
while g<= 12:
    g+=1
    
    if g == 7:
        continue

    print(g)
    

