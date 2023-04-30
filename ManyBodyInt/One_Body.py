import numpy as np
from numba import njit
import Global_System as GS
import Forces

class Atom():
    """
    The class of a Planet/Sun
    """
    def __init__(self:object, mass:float, position:list=None, velocity:list=None, name:str=None) -> None:
        """
        Collection necessary conditions for a planet: Phasespace variables (dim)
        made up of (Mass) positon (dim=3) and velocity (dim=3)
        """
        self.name = name
        self.current_pos = position
        self.current_vel = velocity
        self.positions = [position]
        self.velocity = [velocity]
        self.mass = mass
        pass

    def Update_pos(self):
        """
        Updates the position value
        """
        
        pass
        
