from manimlib.imports import *

class PCA(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=45 * DEGREES,theta=-45*DEGREES)
        self.add(ThreeDAxes())
        self.begin_ambient_camera_rotation(0.3)
        A= np.random.uniform(0,2, 100)
        B= np.random.uniform(0,2, 100)
        C= np.random.uniform(0,2, 100)
        Dots = VGroup(*[Dot(point=(a,b,c)) for a,b,c in zip(A,B,C)])
        Dots_shaddow= Dots.copy().set_opacity(0.1)
        Dots_z0 = Dots.copy().set_color(DRAC_ORANGE)
        rect=Rectangle(width= 3,height=3, fill_color= DRAC_ORANGE, fill_opacity=0.4, stroke_color = BLACK)
        rect.shift(UP+RIGHT)
        self.add(rect)
        self.add(Dots)
        self.add(Dots_shaddow)
        [objec.set_z(0) for  objec in Dots_z0.submobjects]
        self.wait()
        self.play(Transform(Dots,Dots_z0), run_time=2)
        self.wait()

if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p  -m -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name + " " + "PCA"
    os.system(command_A + command_B)

