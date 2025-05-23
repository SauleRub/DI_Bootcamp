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
