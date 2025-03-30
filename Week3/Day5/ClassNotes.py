# class Israeli:
#     prime_minister = "Bibi"
#     num_citizens = 0

#     def __init__(self, name):
#         self.name =  name
#         Israeli.num_citizens += 1
#         self.tz = Israeli.num_citizens

# hadriel = Israeli('Hadriel')

# # print(hadriel.name)
# # print(hadriel.tz)
# # print(hadriel.prime_minister)

# Arik = Israeli('Arik')

# # print(Arik.prime_minister)

# # Israeli.prime_minister = "LeBron"

# # print(Arik.prime_minister)

# ilan = Israeli('Ilan')

# print(Arik.tz)


# class Circle:
#     color = "red"

#     def __init__(self, diameter):
#         self.diameter = diameter

#     def grow(self, factor=2):
#         self.diameter = self.diameter * factor

#     def get_color(self):
#        return Circle.color

# circle1 = Circle(2)
# print(circle1.color)
# print(Circle.color)
# print(circle1.get_color())
# circle1.grow(3)
# print(circle1.diameter)

# class Person:

#     used_names = set()

#     def __init__(self, name, age):
#         if name in self.used_names:
#             name = input("That name is taken. Enter another name: ")

#         self.name = name
#         self.age = age
#         self.used_names.add(name)

#     @classmethod
#     def fromYear(cls, name, birth_year):
#         THIS_YEAR = 2020
#         return cls(name, THIS_YEAR - birth_year)

#     @property
#     def professional_name(self):
#         return "Mr " + self.name
    
# sharon = Person("Sharon", 29)
# markus = Person("Markus", 40)

# print(markus.professional_name)

# class MyClass(object):
#     count = 0

#     def __init__(self, val):
#         self.val = val
#         MyClass.count += 1

#     def set_val(self, newval):
#         self.val = newval

#     def get_val(self):
#         return self.val

#     @classmethod
#     def get_count(cls):
#         return cls.count

# object_1 = MyClass(10)
# print("\nValue of object : %s" % object_1.get_val())
# print(MyClass.get_count())

# object_2 = MyClass(20)
# print("\nValue of object : %s" % object_2.get_val())
# print(MyClass.get_count())


 #To overload a dunder method, we need to implement it in a class.

class Person:
  def __init__(self, name, lastName):
      self.name = name
      self.lastName = lastName


#Here we overloaded the method by redefining '__repr__ 'using 'def' and passed the argument '(self)'

  def __repr__(self):

# We can write whatever we want inside this method, but we have to return an object.

      return f"{self.__class__.__name__} : {self.name} {self.lastName}"

  def __add__(self,other):
      name = self.name[0] + other.name[1:]
      lastname = other.lastName
      return Person(name,lastname)

father = Person('John', 'Snow')
mother = Person('Kaleesi', 'MotherOfDragons')
# using the __add__() method
dragonChild = father + mother 

print(dragonChild)
# >>Person : Jaleesi MotherOfDragons