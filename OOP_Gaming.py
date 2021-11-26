#OOP
class PlayerCharacter:
  def __init__ (self,name,age):
    self.name = name
    self.age = age
#atributes~specification that defines a property of an object, element or file

def run (self):
  print ('run')
  return 'done'

player1 = PlayerCharacter ('Cindy',44)
player2 = PlayerCharacter ( 'Tom',21)
player2.attack = 50
print (player1.name)
print (player2.age)
#self ~ makes attribute dinamic.Makes it specific for object (player1,player 2 are objects)