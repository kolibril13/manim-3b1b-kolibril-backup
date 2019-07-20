from manimlib.imports import *


class shape(ThreeDScene):

    def construct(self):
        resolution_fa=22
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        # self.set_camera_orientation(phi=90 * DEGREES, theta=-45 * DEGREES)
        form= ParametricFunction(lambda u : np.array([np.cos(u),np.sin(u),u])
                                 , t_min=-TAU, t_max=TAU)
        self.begin_ambient_camera_rotation(rate=0.1)  # Start move camera
        def param_plane(u,v):
            x=u
            y=v
            z=0
            return np.array([x,y,z])
        magic_plane=  ParametricSurface((param_plane) , resolution=(resolution_fa,resolution_fa),
                        v_min = -2, v_max = 2, u_min = -2, u_max = 2).scale_about_point(2,ORIGIN)

        def param_gauss(u,v):
            x=u
            y=v
            d = np.sqrt(x * x + y * y)
            sigma, mu = 0.4, 0.0
            z= np.exp(-((d - mu) ** 2 / (2.0 * sigma ** 2)))
            return np.array([x,y,z])

        magic_gauss= ParametricSurface((param_gauss),resolution=(resolution_fa, resolution_fa),
                                 v_min=-2,v_max=2,u_min=-2,u_max=2).scale_about_point(2,ORIGIN)
        magic_gauss.set_style(fill_opacity=1)
        magic_gauss.set_style(stroke_color=GREEN)
        magic_gauss.set_fill_by_checkerboard(GREEN,BLUE,opacity=0.1)
        axes = ThreeDAxes()
        self.add(axes)
        self.play(Write(magic_plane))
        self.play(Transform(magic_plane,magic_gauss))
        self.wait(2)
if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim   -p -l -s -c '#1C758A' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"shape"
    os.system(command_A + command_B)