from manimlib.imports import *
from hendrik_active.resusable_hendrik.histograms import *
from hendrik_active.resusable_hendrik.image_pro import *
class Poisson_noise(Scene):
    def construct(self):
        seed = 42 # initilize the randomness for the poisson noise
        np.random.RandomState(seed)
        poission_With_one_pixel=[]
        text_for_the_images= []
        histograms= []
        rep_rate=1
        photon_intensities= range(1,2)
        # rep_rate=2
        # photon_intensities=[1]
        #
        max = 256


        for photons_val in photon_intensities:
            for i in range(0,rep_rate):
                 img=create_poission_noise_ball(num_photons=photons_val)
                 img[img > max-1]=max-1
                 im_sctretched=IPcontraststretch(img)
                 poission_With_one_pixel.append(im_sctretched)
                 text_for_the_images.append(str(photons_val))

                 val = np.histogram(img, bins=[i for i in np.arange(0, max + 1)])
                 hist = Image_Histogram(val[1], val[0], x_scale=4 / max, y_scale=3/val[0].max())
                 histograms.append(hist)
                 print(photons_val)

        poission_With_one_pixel_ALL= [ImageMobject(img_a).scale(2.5) for img_a in poission_With_one_pixel]

        for PLOT,text,hist in zip(poission_With_one_pixel_ALL,text_for_the_images,histograms):
            self.clear()
            PLOT.to_edge(LEFT)
            self.add(PLOT)
            print(text)
            t_2= TexMobject(r"\text{Photonenrate: }" + text +  r"\, \frac{\text{photons}}{s}")
            t_2.next_to(PLOT,DOWN)
            t_2.to_edge(LEFT)
            self.add(t_2)
            hist.to_edge(RIGHT)
            self.add(hist)
            print(text)
            self.wait(0.33)



if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command = "manim -p -s --leave_progress_bars " + module_name + " Poisson_noise"
    os.system(command)









