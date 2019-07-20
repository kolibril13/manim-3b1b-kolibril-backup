import numpy as np
import matplotlib.pyplot as plt
pixel=30
img = np.fromfunction(lambda u,v: np.sin(u)+np.cos(v) ,(pixel,pixel))

print(img)
fourier= np.fft.fft2(img)
fourier_s=np.fft.fftshift(fourier)
print(fourier)
plt.subplot(1,2,1)
plt.imshow(img)
plt.subplot(1,2,2)
plt.imshow(abs(fourier_s))
plt.show()
# magnitude_spectrum = 20*np.log(np.abs(F2))
# b.pltx(bw_img,magnitude_spectrum)