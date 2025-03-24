from dogs import Dog  
import random  

class PetDog(Dog):  
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)  
        self.trained = False  

    def train(self):
        """Train the dog: make it bark and set trained to True"""
        print(self.bark())  
        self.trained = True  

    def play(self, *other_dogs):
        """Play with other dogs"""
        dog_names = ", ".join(dog.name for dog in other_dogs)
        print(f"{self.name}, {dog_names} all play together.")

    def do_a_trick(self):
        """Perform a trick only if the dog is trained"""
        if self.trained:
            tricks = [
                f"{self.name} does a barrel roll.",
                f"{self.name} stands on his back legs.",
                f"{self.name} shakes your hand.",
                f"{self.name} plays dead."
            ]
            print(random.choice(tricks))  
        else:
            print(f"{self.name} is not trained yet and refuses to do a trick!")


dog1 = PetDog("Buddy", 3, 20)
dog2 = PetDog("Charlie", 5, 30)
dog3 = PetDog("Rocky", 2, 15)

dog1.train()

dog1.play(dog2, dog3) 


dog1.do_a_trick() 

dog3.do_a_trick()  
