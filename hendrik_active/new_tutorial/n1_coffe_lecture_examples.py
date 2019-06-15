from manimlib.imports import *
class COFFE1(Scene):
    def construct(self):
        grid = NumberPlane()
        grid_title = TextMobject("Grid")
        grid_title.scale(1.5)

        self.add(grid, grid_title)  # Make sure title is on top of grid
        self.play(
            FadeInFromDown(grid_title),
            ShowCreation(grid, run_time=1, lag_ratio=0.1),
        )
        self.wait()

        grid_transform_title = TextMobject(
            "Grid Transformation"
        )
        grid_transform_title.move_to(grid_title, UL)
        grid.prepare_for_nonlinear_transform()
        self.play(
            grid.apply_function,
            lambda p: p + np.array([np.sin(p[1]),np.sin(p[0]),0,]),run_time=3)
        self.wait()
        self.play(
            Transform(grid_title, grid_transform_title)
        )
        self.wait()
class COFFE2(Scene):
    def construct(self):
        title = TexMobject(r"i\hbar\frac{\partial\psi\left(x,t\right)}{\partial t}=-\frac{\hbar^{2}}{2m}\frac{\partial^{2}\psi\left(x,t\right)}{\partial x^{2}}+V\cdot\psi\left(x,t\right)")
        tex2 = TexMobject(r"i\hbar\frac{\partial\psi\left(x,t\right)}{\partial t}",r"=-\frac{\hbar^{2}}{2m}\frac{\partial^{2}\psi\left(x,t\right)}{\partial x^{2}}",r"+V\cdot\psi\left(x,t\right)")
        tex2.set_color_by_tex(r"i\hbar\frac{\partial", color=DARK_BLUE)
        tex2.set_color_by_tex(r"-\frac{\hbar^{", color=GREEN)
        tex2.set_color_by_tex(r"+V", color=YELLOW)
        VGroup(title, tex2).arrange(DOWN)
        self.play( Write(title)) #1
        self.play(FadeInFrom(tex2, UP)) #2
        self.wait(2) #3

        transform_title = TexMobject(r"\frac{\partial \rho}{\partial t}+ \frac{\partial(\rho u_{i})}{\partial x_{i}} = 0")

        transform_title.to_corner(UP + LEFT)
        self.play(
            Transform(title, transform_title),
            LaggedStart(*map(FadeOutAndShiftDown, tex2)),
        ) #4
        self.wait() #5


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p   -c '#2B2B2B' --video_dir ~/Downloads/ "
    command_B = module_name + " COFFE2"
    os.system(command_A + command_B)
