"""Solution to Ellen's Alien Game exercise."""


class Alien:
    total_aliens_created = 0
    def __init__(self,x_coordinate,y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        Alien.total_aliens_created +=1
        self.health = 3
    #Methods
    #-------
    #hit(): Decrement Alien health by one point.

    def hit(self):
        self.health -=1

    
    #is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False
    
    #teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    def teleport(self,new_x,new_y):
        self.x_coordinate = new_x
        self.y_coordinate = new_y
    
    #collision_detection(other): Implementation TBD.
    def collision_detection(self,other):
        pass
def new_aliens_collection(positions):
    return [Alien(position[0], position[1]) for position in positions]

#TODO:  create the new_aliens_collection() function below to call your Alien class with a list of coordinates.
