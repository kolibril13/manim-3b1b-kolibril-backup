from manimlib.imports import *

class PrincipleComponent(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=40 * DEGREES)
        self.begin_ambient_camera_rotation(0.2)
        surf = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                u**2-v**2
            ]),
            resolution=(6, 32),
        v_min=-1,v_max=1,u_min=-1,u_max=1
        ).set_shade_in_3d(True)
        comp1=Circle(radius=2, fill_color=GREEN, fill_opacity=0.4).rotate(PI/2, LEFT).move_to(ORIGIN).shift(OUT*2).set_shade_in_3d(True)
        self.add(comp1)
        comp1=Circle(radius=2, fill_color=BLUE, fill_opacity=0.4).rotate(PI/2, LEFT).rotate(PI/2, IN).move_to(ORIGIN).shift(IN*2).set_shade_in_3d(True)
        self.add(comp1)
        dot = Dot()
        self.add(dot)
        self.add(surf)
        self.wait(3)

    
if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p  -s -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"PrincipleComponent"
    os.system(command_A + command_B)