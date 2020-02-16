from manimlib.imports import *

class PrincipleComponent(ThreeDScene):
    def construct(self):
        self.camera.frame_center.shift(2 * LEFT)
        time=1
        self.set_camera_orientation(phi=40 * DEGREES)
        self.begin_ambient_camera_rotation(0.2)
        grid= 15
        size=1.4
        surf1 = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                u**2-v**2
            ]),
            resolution=(grid, grid),
            v_min=-size,v_max=size,u_min=-size,u_max=size
        ).set_shade_in_3d(True).set_style(fill_opacity=0,stroke_width=2 , stroke_color=GREEN)
        # surf2 = ParametricSurface(
        #     lambda u, v: np.array([
        #         u,
        #         v,
        #         u**2+v**2
        #     ]),
        #     resolution=(grid, grid),
        #     v_min=-size,v_max=size,u_min=-size,u_max=size
        # ).set_shade_in_3d(True).set_style(fill_opacity=0,stroke_width=2 , stroke_color=BLUE)
        comp1=Circle(radius=0.5, fill_color=WHITE, fill_opacity=0.4).rotate(PI/2, LEFT).move_to(ORIGIN).shift(OUT*1/2).set_shade_in_3d(True)
        comp2=Circle(radius=0.5, fill_color=WHITE, fill_opacity=0.4).rotate(PI/2, LEFT).rotate(PI/2, IN).move_to(ORIGIN).shift(IN*1/2).set_shade_in_3d(True)
        comp1.set_style(fill_color=WHITE, stroke_opacity=0)
        comp2.set_style(fill_color=WHITE,stroke_opacity=0)

        t0= TextMobject("Parametric Surface:").scale(0.5).to_corner(UR).shift(2*LEFT)
        t0b= TexMobject(r"z(x,y) = x^2-y^2").scale(0.5).next_to(t0,DOWN).set_color(GREEN)
        t1= TextMobject("Definition of the Gaussian Curvature:").scale(0.5).next_to(t0b,DOWN)
        ancor= t1.copy()
        t2= TexMobject(r"K = \frac{1}{R_1} \cdot \frac{1}{R_2}").scale(0.5).next_to(t1,DOWN)
        t3= TextMobject("Find principle curvatures in Point (0,0) by",).scale(0.5).next_to(t2,DOWN).align_to(ancor,LEFT)
        t4= TextMobject("adding two circles tangential to the surface").scale(0.5).next_to(t3,DOWN, buff=0.1).align_to(ancor,LEFT)
        t5= TexMobject(r"R_1 = 0.5").scale(0.5).next_to(t4,DOWN).align_to(ancor,LEFT)
        t6= TexMobject(r"R_2 = -0.5").scale(0.5).next_to(t5,DOWN).align_to(ancor,LEFT)
        t7= TexMobject(r"\rightarrow K = -4").scale(0.5).next_to(t6,DOWN).align_to(ancor,LEFT)
        t8= TextMobject("Principle curvatures have different signs").scale(0.5).next_to(t7,DOWN).align_to(ancor,LEFT)
        t9 =TexMobject(r"\rightarrow \text{Gaussian curvature negative}").scale(0.5).next_to(t8,DOWN).align_to(ancor,LEFT)
        t10=TexMobject(r"\rightarrow \text{Point (0,0) is a saddle point}").scale(0.5).next_to(t9,DOWN).align_to(ancor,LEFT)
        dot = Dot()
        self.add_fixed_in_frame_mobjects(t0,t0b)
        self.play(FadeIn(surf1),FadeIn(dot))
        self.add_fixed_in_frame_mobjects(t1,t2)
        self.wait()
        self.add_fixed_in_frame_mobjects(t3,t4)
        self.wait()
        self.play(FadeInFrom(comp1,direction=-IN))
        self.add_fixed_in_frame_mobjects(t5)
        self.wait()
        self.play(FadeInFrom(comp2,direction= IN))
        self.add_fixed_in_frame_mobjects(t6)
        self.wait()
        # t7= TexMobject(r"\rightarrow K = -4").scale(0.5).next_to(t6,DOWN).align_to(ancor,LEFT)
        # self.wait(1)
        # self.add_fixed_in_frame_mobjects(t7)
        # self.wait(time)
        # self.add_fixed_in_frame_mobjects(t8)
        # self.wait(time)
        # self.add_fixed_in_frame_mobjects(t9)
        # self.add_fixed_in_frame_mobjects(t10)
        #
        # self.wait(1)
        # #self.play(Transform(surf1,surf2))
        # self.wait(3)


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p -s --video_dir ~/Downloads/  "
    command_B = module_name +" " +"PrincipleComponent"
    os.system(command_A + command_B)