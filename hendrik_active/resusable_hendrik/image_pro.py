import numpy as np
def circ(img, radius, circle_opacity):
    n, m = np.shape(img)
    for j in range(0, n):
        for k in range(0, m):
            if (j - n / 2) ** 2 + (k - m / 2) ** 2 < radius ** 2:
                img[j, k] = img[j, k] * (1 - circle_opacity)
    return img


def create_poission_noise_ball(num_photons=100):
    num_pixels = 512
    img_origin = np.ones((num_pixels, num_pixels))
    shot_noise_img = num_photons * img_origin
    shot_noise_img = circ(shot_noise_img, 75, circle_opacity=0.1)
    shot_noise = np.random.poisson(shot_noise_img, (num_pixels, num_pixels))
    return np.uint8(shot_noise)


def IPcontraststretch(image):
    image = np.asarray(image)
    M = image.max()
    m = image.min()
    stretched_img = (256 - 1) / (M - m) * (image - m)
    return np.uint8(stretched_img)