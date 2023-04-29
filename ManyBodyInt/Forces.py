"""
Here the class of Forces is located
"""
from numba import njit
import numpy as np

class Fores():
    """
    The class of forces carries the functions to calculate the acceleration for each
    Physical Object
    """
    def __init__(self) -> None:
        pass

    @njit    
    def Gravitation_pot(self, pos_1:np.array, pos_2:np.array, mass_1:float, mass_2:float) -> float:
        """
        Gravitation Potential from exercise sheet 1
        """
        G = 6.67408*10**(-11)
        r_12:float = np.linalg.norm(pos_1,pos_2)
        return(-G*mass_1*mass_2/r_12)
