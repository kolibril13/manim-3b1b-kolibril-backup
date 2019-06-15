from manimlib.imports import *

from active_projects.eop.reusables.histograms import *

class Poisson_noise(Scene):

    def circ(self,img, radius, circle_opacity):
        n, m = np.shape(img)
        for j in range(0, n):
            for k in range(0, m):
                if (j - n / 2) ** 2 + (k - m / 2) ** 2 < radius ** 2:
                    img[j, k] = img[j, k] * (1-circle_opacity)
        return img

    def create_poission_noise_ball(self, num_photons=100):
        num_pixels = 512
        img_origin = np.ones((num_pixels, num_pixels))
        shot_noise_img = num_photons * img_origin
        shot_noise_img = self.circ(shot_noise_img, 75, circle_opacity= 0.1)
        shot_noise = np.random.poisson(shot_noise_img, (num_pixels, num_pixels))
        return np.uint8(shot_noise)

    def IPcontraststretch(self,image):
        image = np.asarray(image)
        M = image.max()
        m = image.min()
        stretched_img = (256 - 1) / (M - m) * (image - m)
        return np.uint8(stretched_img)

    def construct(self):
        seed = 42 # initilize the randomness for the poisson noise
        np.random.RandomState(seed)
        poission_With_one_pixel=[]
        text_for_the_images= []
        histograms= []
        rep_rate=20
        photon_intensities= [1,2,3,4,5,6,7,8,9,10,20,30,40,50,100,120,130,140]

        # rep_rate=2
        # photon_intensities=[1]
        #
        max = 256


        for photons_val in photon_intensities:
            for i in range(0,rep_rate):
                 img=self.create_poission_noise_ball(num_photons=photons_val)
                 im_sctretched=self.IPcontraststretch(img)
                 poission_With_one_pixel.append(im_sctretched)
                 text_for_the_images.append(str(photons_val))

                 val = np.histogram(img, bins=[i for i in np.arange(0, max + 1)])
                 hist = Image_Histogram(val[1], val[0], x_scale=4 / max, y_scale=3/val[0].max())
                 histograms.append(hist)

        poission_With_one_pixel_ALL= [ImageMobject(img_a).scale(2.5) for img_a in poission_With_one_pixel]

        for PLOT,text,hist in zip(poission_With_one_pixel_ALL,text_for_the_images,histograms):
            self.clear()
            PLOT.to_edge(LEFT)
            self.add(PLOT)
            print(text)
            t_2= TexMobject(r"\text{Rate of incident photons: }" + text +  r"\, \frac{\text{photon}}{s}")
            t_2.next_to(PLOT,DOWN)
            t_2.to_edge(LEFT)
            self.add(t_2)
            hist.to_edge(RIGHT)
            self.add(hist)
            self.wait(0.33)



if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command = "python3.7 -m manim -p   -a --leave_progress_bars " + module_name
    os.system(command)









