import numpy as np
img= np.random.randint(1,40, (10,10))
img[img > 20]=20
print(img)