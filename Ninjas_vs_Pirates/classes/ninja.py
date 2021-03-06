class Ninja:

    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , pirate ):
        if self.speed >= 10:
            pirate.health -= (self.strength * 2)
            self.speed = 5
        else:
            self.speed += 5
            pirate.health -= self.strength
        if pirate.health <= 0 :
            pirate.health = 0 
            print(f"{self.name} GAME OVER!!!")
        return self