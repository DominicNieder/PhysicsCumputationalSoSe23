"""
Here the class of Forces is located
"""
from numba import njit
import numpy as np

# I could not decide if it would be more efficiant to sum up all gravitational potentialls
# and then to calculate the gradient (would need to deal with variables/seems problematic),
# or to directly calculate the Force and sum over all Forces to get the acceleration. 
# So I started coding both possebilities...
# I also asked myselfe if the force should be an object as in physics we often look at one 
# forcefield which is an object...

@njit    
def Gravitation_pot(pos_self:np.array, pos_2:np.array, mass_1:float, mass_2:float) -> float:
    """
    Calculates the gravitation Potential from exercise sheet 1
    """
    G = 6.67408*10**(-11)
    r_12:float = np.linalg.norm(pos_self-pos_2,pos_self-pos_2)
    e_pot = -G*mass_1*mass_2/r_12
    return(e_pot)  # taken from the exercise sheet

@njit 
def Gravitational_force(pos_self:np.array, pos_2:np.array, mass_self:float, mass_2:float) ->np.array:
    """
    Calculates and returns the gravitational Force (vector, np.arrayarray) between 2 objects
    """
    G = 6.67408*10**(-11)
    r_12_vec:np.array = pos_self-pos_2
    r_12:float = np.linalg.norm(pos_self-pos_2,pos_self-pos_2)
    r_12_pow3 = r_12*r_12*r_12
    force =G*mass_2*mass_self/r_12_pow3 *r_12_vec   # calculated via -grad(Gravitation_pot)

    return(force)
