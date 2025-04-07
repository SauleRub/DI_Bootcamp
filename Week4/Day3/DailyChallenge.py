# Part 1 : Quizz :
# Answer the following questions

# What is a class?
# What is an instance?
# What is encapsulation?
# What is abstraction?
# What is inheritance?
# What is multiple inheritance?
# What is polymorphism?
# What is method resolution order or MRO?


# Part 2: Create a deck of cards class.
# The Deck of cards class should NOT inherit from a Card class.

# The requirements are as follows:

# The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
# The Deck class :
# should have a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
# should have a method called deal which deals a single card from the deck. After a card is dealt, it should be removed from the deck.


# Part 1: Quizz Questions
# 	1.	What is a class?
# 		A class is kind of like a blueprint or template for creating objects. It defines what properties and actions the objects created from it will have. So, if you have a Car class, it’s just a plan, but you can create specific cars from that plan, each with its own color, model, etc.
# 	2.	What is an instance?
# 		An instance is just an actual object made from a class. If the class is Dog, then an instance of that class could be a specific dog, like “Buddy,” that has its own name, breed, and characteristics. So, the class is the general idea, and the instance is the real thing.
# 	3.	What is encapsulation?
# 		Encapsulation is about hiding the complicated stuff and only showing what’s necessary. Like, when you drive a car, you don’t need to know exactly how the engine works under the hood. You just press the gas pedal and go. In programming, it means keeping data hidden and controlling access through methods, so you don’t mess with things you shouldn’t.
# 	4.	What is abstraction?
# 		Abstraction is simplifying things by hiding all the unnecessary details. You only need to know what something does, not how it does it. For example, when you’re using a phone, you don’t care about the code that makes it work, you just care that it works. It’s all about focusing on the big picture.
# 	5.	What is inheritance?
# 		Inheritance lets one class (the child) inherit properties and methods from another class (the parent). Think of it like a family tree. So, if you have a Person class, you might create a Student class that gets all the basic stuff from Person (like name and age), but you can also add extra stuff for students, like grades.
# 	6.	What is multiple inheritance?
# 		Multiple inheritance is when a class can inherit from more than one parent class. So, a FlyingCar could inherit from both a Car class and a FlyingVehicle class, getting all the properties and methods from both. It’s like mixing two things together to create something new.
# 	7.	What is polymorphism?
# 		Polymorphism is the idea that one function or method can work in different ways depending on the object it’s used on. For example, if you have a speak() method, a dog might bark, and a cat might meow, but they both use the same speak() method. It’s all about making things more flexible.
# 	8.	What is method resolution order or MRO?
# 		MRO is basically the order in which Python looks for methods when you’re working with multiple inheritance. It’s how Python decides which class to get a method from when you have multiple parent classes. Python uses a specific order (called C3 linearization) to figure this out, so you don’t end up with any confusion.

import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [Card(suit, value) for suit in self.suits for value in self.values]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) == 0:
            return None  
        return self.cards.pop()  


deck = Deck() 
deck.shuffle()  
card = deck.deal()  
print(card) 
