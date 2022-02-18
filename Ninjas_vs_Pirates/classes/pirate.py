class Pirate:

    def __init__( self , name ):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 100

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack ( self , ninja ):
        if self.health <= 0 :
            self.health = 0 
            print(f"{self.name} GAME OVER!!!")
        elif self.speed >= 10:
            ninja.health -= (self.strength * 2)
            self.speed = 3
        else:
            self.speed += 3
            ninja.health -= self.strength
        return self

