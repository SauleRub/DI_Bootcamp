# def say_hello(username):
#     """A function that says hello"""
#     print(f"Hello, {username}!") 

# say_hello('Sam')
# say_hello('Markus')

# def say_hello(username, language="HE"):
#     if language == "EN":
#         print("Hello "+username)
#     elif language == "FR":
#         print("Bonjour "+username)
#     elif language == "HE":
#         print("Shalom "+username)
#     elif language == "LT":
#         print("Labas "+username)
#     else:
#         print("This language is not supported"+ language)


# say_hello('Sam', 'EN')
# say_hello('Markus', 'FR')
# say_hello('Arik', 'HE')
# say_hello('Saule', 'LT')

# say_hello('Ilan')




# def format_name(first_name, last_name):
#     return (first_name.title(), last_name.title())

# first, last = format_name("RICk", "mORTY")
# print(first)
# print(last)

# def calculation(a, b):
#     addition = a + b
#     substraction = a - b
#     return addition, substraction

# res = calculation(40, 10)
# print(res)

# def greet_users(users):             # users should be a list
#     for user in users:              # Because it's a list, we can loop through it
#         print("Hello " + user.title() + " !")       # For each user, print "hello" and then his name

# usernames = ["steve", "stan", "debbie"]
# greet_users(usernames)

# dir(greet_users)


# def kwargs_processor(**kwargs):
#     print(kwargs)

# kwargs_processor(teacher="aaron", student="markus")

# def sample(name, age, *args, **kwargs):
#     print(f"{name} went to the park. He is {age}")
#     print(args)
#     print(kwargs)

# sample("Brutus", 55, "charlie", location = "TLV", writing = "pen")

# def upper_string(s):
#     return s.upper()

# fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
# map_object = map(upper_string, fruit)

# print(list(map_object))

# def starts_with_A(s):
#     return s[0] == "A"

# fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
# filtered_object = filter(starts_with_A, fruit)

# print(list(filtered_object))

people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]

short_names = filter(lambda name: len(name)<=4, people )
display_names = map(lambda name: f"hello {name}!!!", short_names)

for greeting in list(display_names):
    print(greeting)

