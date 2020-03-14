from manimlib.imports import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot
from skimage import io

class tomo2curve(Scene):
    def construct(self):
        imgs = io.imread('reconstructed_02.tif')
        x= np.array([0.78297872, 0.77386018, 0.68085106, 0.68024316, 0.84984802,
                  0.79696049, 0.75866261, 0.73617021, 0.61519757, 0.69969605,
                  0.74407295, 0.73009119, 0.73009119, 0.843769  , 0.72522796,
                  0.70759878, 0.73069909, 0.71489362, 1.        , 0.85775076,
                  0.95075988, 0.19452888, 0.08510638, 0.08510638, 0.08510638,
                  0.3550152 , 0.38297872, 0.48024316, 0.62735562, 0.49604863,
                  0.51428571, 0.45653495, 0.55927052, 0.4881459 , 0.51428571,
                  0.46443769, 0.52462006, 0.69118541, 0.68449848, 0.61155015,
                  0.66443769, 0.49179331, 0.39027356, 0.49848024, 0.40729483,
                  0.31428571, 0.36656535, 0.6443769 , 0.65775076, 0.53556231,
                  0.22978723, 0.00790274, 0.        , 0.05167173])
        x2 = np.array([0.97526882, 0.9827957 , 0.97419355, 0.97311828, 0.98602151,
                    0.98817204, 0.97956989, 0.97741935, 0.9655914 , 0.96774194,
                    0.97526882, 0.98494624, 0.99354839, 1.        , 0.98709677,
                    0.98172043, 0.97956989, 0.97741935, 0.96236559, 0.8688172 ,
                    0.72150538, 0.42580645, 0.22580645, 0.1344086 , 0.13010753,
                    0.24408602, 0.33763441, 0.42258065, 0.49139785, 0.50967742,
                    0.53978495, 0.55376344, 0.57956989, 0.57956989, 0.59032258,
                    0.60215054, 0.64301075, 0.70215054, 0.72580645, 0.71290323,
                    0.68387097, 0.60860215, 0.54731183, 0.52903226, 0.49032258,
                    0.46344086, 0.48172043, 0.53333333, 0.50107527, 0.38494624,
                    0.20645161, 0.05268817, 0.        , 0.01505376])
        curve_teo = VMobject()
        curve_teo.set_points_smoothly([[xi,yi,0]
                                       for xi, yi in zip(np.linspace(0,2,len(x)),x) ] ).scale(4)
        curve_teo.set_style(stroke_color=BLUE)
        curve_exp = VMobject()
        curve_exp.set_points_smoothly([[xi,yi,0]
                                       for xi, yi in zip(np.linspace(0,2,len(x2)),x2) ] ).scale(4)
        curve_teo.set_style(stroke_width=4)
        curve_exp.set_style(stroke_width=4,stroke_color=DRAC_ORANGE)
        self.wait()
        self.play(Write(curve_teo), rate_func=linear,run_time=3)
        self.add(curve_teo.copy().set_style(stroke_opacity=0.2))
        t=TexMobject(r"\phi(x,y) = 2\pi F \mathcal{F}^{-1} \left( \frac{\mathcal{F}(I/I_0-1)}{|k^0_\bot|^2+\alpha}\right)")
        self.play(FadeIn(t.to_edge(DOWN)))
        self.wait(2)
        self.play(Transform(curve_teo,curve_exp), run_time=3)

        self.wait(2)
if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p  -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"tomo2curve"
    os.system(command_A + command_B)