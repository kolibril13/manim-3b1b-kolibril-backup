
from manimlib.imports import *
from hendrik_active.resusable_hendrik.histograms import *
from hendrik_active.resusable_hendrik.image_pro import *

class Experiment(Scene):
    CONFIG = {
        "y_min": 0,
        "y_max": 10    }
    def construct(self):
        light_source= Square().scale(1.2*2)
        light_source.rotate(-20, [0, 1, 0.05])
        light_source.move_to(2*LEFT)
        light_source.set_style(fill_color=YELLOW,fill_opacity=0.1)
        self.play((FadeInFromDown(light_source)))
        t_light_source= TextMobject("Lichquelle", color= YELLOW).next_to(light_source,UP)
        self.play( FadeIn(t_light_source))

        ## detector:
        original_square= Square(fill_opacity=1, fill_color=BLACK)
        original_square.to_corner(RIGHT)
        t_Fotodiode=TextMobject("Fotodiode", color= YELLOW)
        t_Fotodiode.next_to(original_square,UP)

        PIXELS=64
        square_ALL= [Square(fill_opacity=1 , side_length=0.18,fill_color=BLACK) for i in range(0,PIXELS)]
        j=0
        for  i,square_to_move in enumerate(square_ALL):
            if i%np.sqrt(PIXELS)==0:
                j+=1
            k= i-j*np.sqrt(PIXELS)
            square_to_move.move_to(4*UP+(LEFT*k+j*DOWN)*0.2)
        term = VGroup(*[square for square in square_ALL])
        original_sq2 = original_square.copy()
        term.scale(1.5*2)
        term.move_to(2*RIGHT)

        z_axis = Arrow(light_source.get_center(),term.get_center(), color= BLUE)
        z_axis.align_to(light_source, DOWN)
        z_axis.shift(DOWN*0.2)
        text_z_axis=TextMobject("z-Achse", color= BLUE).scale(0.8).next_to(z_axis,DOWN, SMALL_BUFF)
        self.play(FadeIn(z_axis,text_z_axis))

        self.play(FadeIn(original_square), FadeIn(original_sq2), Write(t_Fotodiode))


        # self.play(Transform(original_square, term), lag_ratio=0.2, run_time=4)
        term.rotate(-20, [0, 1, 0.05])
        t_Detektor = TextMobject("Detektor", color=YELLOW).next_to(term, UP)
        self.play(FadeIn(t_Detektor),Transform(original_square, term), lag_ratio=0.2, run_time=4)


        self.play(FadeOut(t_Fotodiode), FadeOut(original_sq2))

        # self.play(Transform(original_square,t2))
        self.wait(2)
        self.play(light_source.set_opacity, 1 , run_time=3)
        self.wait(2)
        l = self.mobjects
        old_animations=[FadeOut(x) for x in self.mobjects if x != original_square]
        self.play(*old_animations ,run_time=0.5, lag_ratio=1)
        self.wait(4)

        ## detecotor_part
        seed = 42 # initilize the randomness for the poisson noise
        np.random.RandomState(seed)
        poission_With_one_pixel=[]
        text_for_the_images= []
        histograms= []
        rep_rate=1
        photon_intensities= [10,50,100,200,255]
        # rep_rate=2
        # photon_intensities=[1]
        #
        max = 256

        for photons_val in photon_intensities:
            for i in range(0,rep_rate):
                 img=create_image(num_photons=photons_val)
                 img[img > max-1]=max-1
                 # im_sctretched=IPcontraststretch(img)
                 poission_With_one_pixel.append(img)
                 text_for_the_images.append(str(photons_val))

                 val = np.histogram(img, bins=[i for i in np.arange(0, max + 1)])
                 hist = Image_Histogram(val[1], val[0], x_scale=4 / max, y_scale=3/val[0].max())
                 histograms.append(hist)
                 print(photons_val)

        poission_With_one_pixel_ALL= [ImageMobject(img_a).scale(2.5) for img_a in poission_With_one_pixel]

        for amount_ani,(PLOT,text,hist) in enumerate(zip(poission_With_one_pixel_ALL,text_for_the_images,histograms)):
            big_Sq=Square()
            big_Sq.set_style(fill_opacity=1,fill_color=BLACK )
            self.clear()
            PLOT.to_edge(LEFT)
            big_Sq.surround(PLOT)
            if amount_ani == 0:
                self.play(Transform(term,big_Sq))
                self.add(PLOT)
                self.wait(2)
                t_2= TexMobject(r"\text{Photonenrate: }" + text +  r"\, \frac{\text{photons}}{s}")
                t_2.next_to(PLOT,DOWN)
                self.wait(2)
            else:
                self.add(big_Sq)
                self.add(PLOT)
                print(text)
                t_2= TexMobject(r"\text{Photonenrate: }" + text +  r"\, \frac{\text{photons}}{s}")
                t_2.next_to(PLOT,DOWN)

                t_2.to_edge(LEFT)
                self.add(t_2)
                hist.to_edge(RIGHT)
                self.add(hist)
                print(text)
                self.wait(1)




if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p -l -n11,200    -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"Experiment"
    os.system(command_A + command_B)