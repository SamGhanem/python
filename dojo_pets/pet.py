class Pet:
    def __init__(self,name,type,tricks, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 80
        self.noise = noise
        
    def sleep(self):
        self.energy += 15
        return self
    
    def eat(self):
        self.energy += 5
        self.health += 10
        return self
    
    def play(self):
        self.health += 2
        self.energy -= 10
        return self
    
    def noises(self):
        print(self.noise)
        return self