#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age
  

#Instantiate the Cat object with 3 cats
cat1 = Cat('judy', 3)
cat2 = Cat('josh', 9)
cat3 = Cat('jackson', 5)

#Create a function that finds the oldest cat
def oldest(*args):
    return max(args)

print(f'The oldest cat is {oldest(cat1.age, cat2.age, cat3.age)} years old')