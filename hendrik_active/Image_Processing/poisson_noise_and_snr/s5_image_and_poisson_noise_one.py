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
        rep_rate=4
        photon_intensities= [1,5,10,50,200,500]

        # rep_rate=2
        # photon_intensities=[1]
        #
        max = 256
        i=1
        photons_val=100
        img=create_poission_noise_ball(num_photons=photons_val)
        print(img)
        img[img > max-1]=max-1
        img = np.uint(img)
        print(img)
        im_sctretched=IPcontraststretch(img)
        poission_With_one_pixel.append(im_sctretched)
        text_for_the_images.append(str(photons_val))

        val = np.histogram(img, bins=[i for i in np.arange(0, max + 1)])
        hist = Image_Histogram(val[1], val[0], x_scale=4 / max, y_scale=3/val[0].max())

        histograms.append(hist)
        poission_With_one_pixel_ALL= [ImageMobject(img_a).scale(2.5) for img_a in poission_With_one_pixel]

        for PLOT,text,hist in zip(poission_With_one_pixel_ALL,text_for_the_images,histograms):
            #self.clear()
            PLOT.to_edge(LEFT)
            brace1=Brace(PLOT,RIGHT)
            eq_text1 = brace1.get_text("512 Pixel")
            text2= TextMobject("512 Pixel")
            t_2= TexMobject(r"\text{Rate of incident photons: }" + text +  r"\, \frac{\text{photon}}{s}")
            t_2.next_to(PLOT,DOWN)
            t_2.to_edge(LEFT)
            self.add(t_2)
            hist.to_edge(RIGHT)
            bgr = Square().surround(hist)
            self.add(bgr)
            self.add(hist)

            print(text)
            self.wait(0.33)



if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command = "python3.7  -m manim  -sl -p --leave_progress_bars " + module_name + " Poisson_noise"
    os.system(command)









