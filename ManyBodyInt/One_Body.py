import numpy as np
from numba import njit
import Integration_Schemes
import Forces

# First I thought that I need to simulate planets and planets are objects so I will have the 
# object class of a panet or more generally speaking of an Atom but I notice that all these 
# variables could also be stored in the System so I wondered if the object "Atom" would be 
# needed at all, I will try without this object for now.
# Speaking from the perspective of spezial relativity I think it would make more sence with 
# the "Atom" object. This would be a completly different piece of cake...
class Atom(object): 
    def __init__(self:object, mass:float, position:list=None, velocity:list=None, name:str=None) -> None:
        """
        Collection necessary conditions for a planet: Phasespace variables (dim)
        made up of (Mass) positon (dim=3) and velocity (dim=3)
        """
        self.name = name
        self.current_pos = position
        self.current_vel = velocity
        self.current_acc = None
        self.positions = [position]
        self.velocity = [velocity]
        self.mass = mass
        pass

    def Update(self, total_acc:np.array):
        """
        Updates the position value.
        """
        
        pass
        
