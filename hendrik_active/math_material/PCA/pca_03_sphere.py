from manimlib.imports import *
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

class PCA(ThreeDScene):
    def construct(self):
        radius = 3
        self.set_camera_orientation(phi=45 * DEGREES)
        self.begin_ambient_camera_rotation(0.2)
        sphere = ParametricSurface(
            lambda u, v: np.array([
                radius*np.cos(u)*np.cos(v),
                radius*np.cos(u)*np.sin(v),
                radius*np.sin(u)
            ]),v_min=0,v_max=TAU,u_min=-PI/2,u_max=PI/2,checkerboard_colors=[RED_D, RED_E],
            resolution=(15, 32)).set_opacity(0.3)
        def point_on_sphere(u,v):
            return np.array((radius*np.sin(u) * np.cos(v),
                             radius*np.sin(u) * np.sin(v),
                             radius*np.cos(u)))
        dot_temp = Dot(point_on_sphere(0.9,4))
        line_to_dot = Line(ORIGIN, dot_temp)
        self.add(line_to_dot)
        unit_vector = line_to_dot.get_vector()
        dot_tip = Dot(dot_temp.get_center(),radius=1, color= GREEN ).set_opacity(0.3)
        dot_tip.rotate_to_match_vector(unit_vector)
        self.add(dot_tip)
        self.add(sphere)
        self.wait()

        #rect=Rectangle(width= 3,height=3, fill_color= DRAC_ORANGE, fill_opacity=0.4, stroke_color = BLACK)
if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p  -s  -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name + " " + "PCA"
    os.system(command_A + command_B)

