import numpy as np
import matplotlib.pyplot as plt

x= [[(k+j)%2 for k in range(1,7)] for j in range(0,7)]
print(x)



# x= np.array ([ [0,1],
#                [1,1] ])
plt.imshow(x)
plt.show()
