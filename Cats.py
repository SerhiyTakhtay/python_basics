#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age
bob = Cat('bob',3)
martin = Cat('martin',5)
jack = Cat ('jack', 2)

def find_oldest_cat(*args):
  return max (args)

print (f' "The oldest cat is {find_oldest_cat (bob.age, martin.age ,jack.age )} years old."')

# 1 Instantiate the Cat object with 3 cats
