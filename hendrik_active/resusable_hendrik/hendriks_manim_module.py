#for later
import os
class hendriks_manim_module:

    def circ(img, rad):
        n, m = np.shape(img)
        for j in range(0, n):
            for k in range(0, m):
                if (j - n / 2) ** 2 + (k - m / 2) ** 2 < rad ** 2:
                    img[j, k] = img[j, k] * 0.9
        return img


    def create_poission_noise_ball( num_photons=100):
        num_pixels = 512
        img_origin = np.ones((num_pixels, num_pixels))
        shot_noise_img = num_photons * img_origin
        shot_noise_img = self.circ(shot_noise_img, 75)
        shot_noise = rs.poisson(shot_noise_img, (num_pixels, num_pixels))
        stretched_img = self.IPcontraststretch(shot_noise)
        return stretched_img


    def IPcontraststretch( image):
        image = np.asarray(image)
        M = image.max()
        m = image.min()
        stretched_img = (256 - 1) / (M - m) * (image - m)
        return np.uint8(stretched_img)

    def get_piano_sounds():
        piano_folder = "/home/jan-hendrik/python/projects/manim-new/projects_hendrik/piano_sounds/small_piano/"
        all_files = []
        for (piano_folder, dirnames, filenames) in os.walk(piano_folder):
            for f in filenames:
                all_files.append(os.path.join(f))
        sounds = {str(element[4:-4]): piano_folder + str(element) for element in all_files}
        return sounds