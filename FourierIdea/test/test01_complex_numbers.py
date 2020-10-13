# split in abs and phase


import numpy as np
r=   255*np.ones((3,3))
phi_rad= np.random.uniform(0,2*np.pi, (3,3))
#phi_rad= 3/2*np.pi*np.ones((3,3))
z=r* np.exp(1j * phi_rad)
print(np.abs(z))
print(np.angle(z, deg=True))