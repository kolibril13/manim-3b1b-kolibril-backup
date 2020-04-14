from manimlib.imports import *
import numpy as np
import matplotlib.pyplot as plt


# Defining the constants
h = 6.626e-34   # Planck constant
k = 1.38e-23    # Boltzman constant
c = 3e+8		# Speed of light in vacuum
# Defining a function for calculating energy density as a function of wavelength
def planck_lamba(L, T):
    # Breaking down the formula
    a = (8 * math.pi * h * c)/(L ** 5)
    b = (h * c)/(L * k * T)
    E = np.exp(b) - 1
    U = a/E
    return U
def make_plot():


    # Computing arrays for wavelengths and frequencies
    L = np.arange(1e-9, 4e-6, 1e-9)			# Lamda
    f = np.arange(1e+13, 150e+13, 1e+13)	# Nu



    # Calculation of energy desnsities as functions of wavelengths at different value of temperatures
    UL3500 = planck_lamba(L, 3500)	# T = 3500 K
    UL3500m = np.argmax(UL3500)
    UL4000 = planck_lamba(L, 4000)	# T = 4000 K
    UL4000m = np.argmax(UL4000)
    UL4500 = planck_lamba(L, 4500)	# T = 4500 K
    UL4500m = np.argmax(UL4500)
    UL5000 = planck_lamba(L, 5000)	# T = 5000 K
    UL5000m = np.argmax(UL5000)
    UL5500 = planck_lamba(L, 5500)	# T = 5500 K
    UL5500m = np.argmax(UL5500)

    # Ploting above calculations
    plt.figure(1)	# Energy density as a function of wavelength
    UL3500p	= [UL3500m]
    UL4000p	= [UL4000m]
    UL4500p	= [UL4500m]
    UL5000p	= [UL5000m]
    UL5500p	= [UL5500m]
    plt.annotate('3500K', xy=(745, 102), xytext=(785, 102), fontstyle = "italic")
    plt.plot(L*1e+9, UL3500*1e-3, marker = "o", markevery = UL3500p)
    plt.annotate('4000K', xy=(640, 188), xytext=(640, 188), fontstyle = "italic")
    plt.plot(L*1e+9, UL4000*1e-3, marker = "o", markevery = UL4000p)
    plt.ylim(0,920)
    plt.xlim(100, 2000)
    plt.xlabel(r"$\lambda$ / 10$^{-9}$ [m]", fontsize = 12, fontweight = "bold")
    plt.ylabel(r"U($\lambda$,T) / 10$^{3}$ [J/m$^{4}$]", fontsize = 12, fontweight = "bold")
    plt.title("Energy density as a function of wavelength", fontsize = 14, color = "b", fontweight = "bold", fontstyle = "italic")
    plt.savefig("plot11",bbox_inches='tight',dpi=200)

class Matplotlibtest(Scene):
    def construct(self):
        make_plot()
        dot = Dot()
        self.add(dot)
        plotbackground= ImageMobject("plot11.png").scale(3)
        plotbackground.background_rectangle = SurroundingRectangle(plotbackground, buff=0)
        self.add( plotbackground,plotbackground.background_rectangle)
        x = np.arange(1e-9, 4e-6, 1e-9)			# Lamda
        y = planck_lamba(x, 3500)*0.00001
        sin_curve = VMobject()
        sin_curve.set_points_smoothly([[xi,yi,0]
                                       for xi, yi in zip(x,y) ] )
        sin_curve.set_color(GREEN)

        sin_curve.stretch_to_fit_width(plotbackground.get_width())
        sin_curve.stretch_to_fit_height(plotbackground.get_height())
        sin_curve.align_to(plotbackground, DOWN)

        x = np.arange(1e-9, 4e-6, 1e-9)			# Lamda
        y = planck_lamba(x, 2500)*0.00001
        sin_curve2 = VMobject()
        sin_curve2.set_points_smoothly([[xi,yi,0]
                                       for xi, yi in zip(x,y) ] )
        sin_curve2.set_color(RED)

        sin_curve2.stretch_to_fit_width(plotbackground.get_width())
        sin_curve2.stretch_to_fit_height(plotbackground.get_height())
        sin_curve2.align_to(plotbackground, DOWN)

        print("no1 :  " , plotbackground.get_width())
        print("no2 :  " , sin_curve.get_width())
        self.play(Write(sin_curve))
        self.play(Transform(sin_curve,sin_curve2))
        self.wait()


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p  -s -c WHITE --video_dir ~/Downloads/  "
    command_B = module_name +" " +"Matplotlibtest"
    os.system(command_A + command_B)