#OOP
class PlayerCharacter:
    #class object attribute
    membership = True 
    def __init__(self, name, age):
        if (age > 18):
            self.name = name #attribute
            self.age = age
    
    def shout(self):
        print(f'{self.name} Jean is not my love') 
    
player1 = PlayerCharacter('Billy', 10)

print(player1.shout())
