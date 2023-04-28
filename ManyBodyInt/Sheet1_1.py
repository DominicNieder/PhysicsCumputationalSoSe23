import numpy as np
from numba import njit


class Heavy_Body():
    """
    The class of a Planet/Sun
    """
    def __init__(self:object, mass:float, name:str=None, position:list=None, velocity:list=None) -> None:
        """
        Collection necessary conditions for a planet: Phasespace variables (dim)
        made up of (Mass) positon (dim=3) and velocity (dim=3)
        """
        self.name = name
        self.positions = [position]
        self.velocity = [velocity]
        self.mass = mass
        pass
