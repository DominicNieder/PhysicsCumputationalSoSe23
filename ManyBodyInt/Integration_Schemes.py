"""
Here a collection of methodes to update position/velocity vectors of one particles can be found.
1)Euler Algorithm
2)Verlet Algorithm
3)Velocity-Verlet Algorithm
These are taken from Exercise Sheet 1, though modiefied f(t) to a(t) with f(t)=m*a(t) <-> a(t)=f(t)/m,
the acceleration will be determined in Forces.
To determin the Energy the Velvet algorithm needed to return a velocity as well
"""
import numpy as np
from numba import njit
import Forces

@njit
def Euler_Algorithm(time_stepp:float, pos:np.array, vel:np.array, acc:np.array):
    """
    With current position and velocity and time step 
    returns updated position/velocity.
    Force exchangable with acceleration -> mass = 1 
    """
    upd_pos = pos+ time_stepp*vel + time_stepp*time_stepp/2 *acc  
    upd_vel = vel * time_stepp * acc  
    return(upd_pos,upd_vel)

@njit 
def Velvet_Algorithem(time_stepp:float, pos:np.array, vel_0:np.array, acc:np.array, fomer_pos:np.array=None):
    """
    Determines position after one time stepp 
    from the former position and current position;

    """
    if fomer_pos=None:
        return(Velocity_Velvet_posAlgorithem(time_stepp, pos, vel_0, acc))
    else:
        upd_pos = 2*pos-fomer_pos + time_stepp*time_stepp*acc
        upd_vel = (upd_pos-fomer_pos)/2/time_stepp
        return(upd_pos, upd_vel)

# On the seperation of Velocity Velvet Algorithem into a position update function
# and velocity update function: 
# as I unsure about the fact that for the velocity all updated positions would be needed to 
# determine the velocity - so I seperated the funktion, so that all positions and the all 
# velocities could be updated
@njit
def Velocity_Velvet_posAlgorithem(time_stepp:float, pos:np.array, vel:np.array, acc:np.array):
    """
    Determines only the position after one time stepp from
    current position, current velocity and acceleration
    """
    upd_pos = pos + vel*time_stepp + time_stepp*time_stepp/2*acc
    return(upd_pos)
@njit
def Velocity_Velvet_velAlgorithem(time_stepp:float, vel:np.array, acc:np.array, later_acc:np.array):
    """
    Determines only the velocity after one time stepp from current postion
    """
    upd_vel = vel + time_stepp/2 *(acc+later_acc)
    return(upd_vel)