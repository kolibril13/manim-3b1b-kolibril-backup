# split in abs and phase
import cmath
import numpy as np
r=   255*np.ones((3,3))
phi= np.pi*np.ones((3,3))
z=r* np.exp(1j * phi)

def get_k_amp_array(z):
    return abs(z)

def get_k_ph_array(z):
    return np.array([[cmath.phase(z_row) for z_row in z_col] for z_col in z ])

amp_array=  get_k_amp_array(z)
ph_array=   get_k_ph_array(z)

print(amp_array)
print(ph_array)
print(np.rad2deg(ph_array))
