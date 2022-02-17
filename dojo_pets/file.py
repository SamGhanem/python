from pet import Pet

class Ninja:
    def __init__(self,first_name,last_name,pet,treats):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = 80
        
    def walk(self):
        self.pet.play()
        return self
    
    def feed(self):
        if (self.pet_food > 0):
            self.pet_food -= 50 
            self.pet.eat()
            
        else:
            print("sorry no food for you")
        return self
    
    def bathe(self):
        self.pet.noises()
        return self
    
    


lola = Pet("Lola", "Dog","all of them","bark")
print(lola.name)
sam = Ninja("Sam","Ghanem",lola,"bully sticks")
sam.feed()
print(lola.health)
print(lola.energy)

sam.bathe()

sam.feed()
print(lola.health)
print(lola.energy)

sam.walk()
print(lola.health)
print(lola.energy)