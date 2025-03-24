# 🌟 Exercise 1 : Pets
# Create another cat breed named Siamese which inherits from the Cat class.
# Create a list called all_cats, which holds three cat instances : one Bengal, one Chartreux and one Siamese.
# Those three cats are Sara’s pets. Create a variable called sara_pets which value is an instance of the Pet class, and pass the variable all_cats to the new instance.
# Take all the cats for a walk, use the walk method.

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    
class Siamese(Cat):
   def sing(self, sounds):
        return f'{sounds}'
   
bengal_cat = Bengal("Bengal", 3)
chartreux_cat = Chartreux("Chartreux", 4)
siamese_cat = Siamese("Siamese", 2)
   
all_cats = [bengal_cat, chartreux_cat, siamese_cat]

sara_pets = Pets(all_cats)
sara_pets.walk()



# 🌟 Exercise 2 : Dogs
# Instructions
# Create a class called Dog with the following attributes name, age, weight.
# Implement the following methods in the Dog class:
# bark: returns a string which states: “<dog_name> is barking”.
# run_speed: returns the dogs running speed (weight/age*10).
# fight : takes a parameter which value is another Dog instance, called other_dog. This method returns a string stating which dog won the fight. The winner should be the dog with the higher run_speed x weight.

# Create 3 dogs and run them through your class.

class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f'{self.name} is barking'
    
    def run_speed(self):
        return (self.weight/self.age*10)
    def fight(self, other_dog):
        self_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight

        if self_power > other_power:
            return f'{self.name} wins the fight'
        elif self_power < other_power:
            return f'{other_dog.name} wins the fight'
        else:
            return "It's a tie!"
        
dog1 = Dog("Buddy", 4, 15)
dog2 = Dog("Max", 3, 20)
dog3 = Dog("Charlie", 5, 18)

print(dog1.bark())  
print(dog2.run_speed())  
print(dog3.fight(dog1))


# 🌟 Exercise 3 : Dogs Domesticated
# Instructions
# Create a new python file and import your Dog class from the previous exercise.
# In the new python file, create a class named PetDog that inherits from Dog.
# Add an attribute called trained to the __init__ method, this attribute is a boolean and the value should be False by default.
# Add the following methods:
# train: prints the output of bark and switches the trained boolean to True

# play: takes a parameter which value is a few names of other Dog instances (use *args). The method should print the following string: “dog_names all play together”.

# do_a_trick: If the dog is trained the method should print one of the following sentences at random:
# “dog_name does a barrel roll”.
# “dog_name stands on his back legs”.
# “dog_name shakes your hand”.
# “dog_name plays dead”.


# Exercise 4 : Family
# Instructions
# Create a class called Family and implement the following attributes:

# members: list of dictionaries
# last_name : (string)

# Implement the following methods:

# born: adds a child to the members list (use **kwargs), don’t forget to print a message congratulating the family.
# is_18: takes the name of a family member as a parameter and returns True if they are over 18 and False if not.
# family_presentation: a method that prints the family’s last name and all the members’ details.

# Create an instance of the Family class, with the last name of your choice, and the below members. Then call all the methods you created in Point 2.


class Family:
    def __init__(self, members, last_name):
        self.members = members
        self.last_name = last_name

    def born(self, **kwargs):
         self.members.append(kwargs)  
         print(f"Congratulations! A new child, {kwargs['name']}, has been born into the {self.last_name} family!")
    
    def is_18(self, name):
        for member in self.members:
            if member['name'] == name: 
                return member['age'] >= 18
        
    def family_presentation(self):
        print(f"The {self.last_name} family:")
        for member in self.members:
            print(f"  Name: {member['name']}, Age: {member['age']}, Gender: {member['gender']}, Child: {member['is_child']}")


        
members = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
]

[
        {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
        {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
    ]

my_family = Family(members, "Smith")

my_family.family_presentation()

print(my_family.is_18("Michael"))  
print(my_family.is_18("Sarah"))    
print(my_family.is_18("John"))     

my_family.born(name="John", age=0, gender="Male", is_child=True)

my_family.family_presentation()


# Exercise 5 : TheIncredibles Family
# Instructions
# Create a class called TheIncredibles. This class should inherit from the Family class:
# This is no random family they are an incredible family, therefore the members attributes, will be a list of dictionaries containing the additional keys : power and incredible_name. (See Point 4)

# Add a method called use_power, this method should print the power of a member only if they are over 18 years old. If not raise an exception (look up exceptions) which stated they are not over 18 years old.

# Add a method called incredible_presentation which :

# Print a sentence like “*Here is our powerful family **”
# Prints the family’s last name and all the members’ details (ie. use the super() function, to call the family_presentation method)

class TheIncredibles(Family):
    def __init__(self, members, last_name):
        super().__init__(members, last_name)

    def use_power(self, name):
        for member in self.members:
            if member['name'] == name:
                if member['age'] >= 18:
                    print(f"{member['incredible_name']} uses their power: {member['power']}!")
                else:
                    raise Exception(f"{member['name']} is not over 18 years old and cannot use their power!")
            
    def incredible_presentation(self):
        print("\n🌟 Here is our incredible family! 🌟")
        super().family_presentation()
    
incredible_members =   [
        {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
        {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
    ]

incredible_family = TheIncredibles(incredible_members, "Incredibles")
incredible_family.incredible_presentation()

incredible_family.use_power("Michael")
incredible_family.use_power("Sarah")
incredible_family.born(name="Jack", age=0, gender="Male", is_child=True, power="Unknown Power", incredible_name="Baby Jack")

try:
    incredible_family.use_power("Jack")  
except Exception as e:
    print(e)