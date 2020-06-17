from manimlib.imports import *

class No8(Scene):
    def construct(self):
        eq1 = TexMobject(r"\frac{dn^+}{dt} = c_A \cdot k^+_{on} - k^+_{off}")
        self.add(eq1.to_edge(DL))
        N=1000
        concentration = 3*N
        x  = np.random.uniform(-0.5*FRAME_WIDTH,0.5*FRAME_WIDTH, np.uint(concentration))
        y = np.random.uniform(-0.5*FRAME_HEIGHT,0.5*FRAME_HEIGHT, np.uint(concentration))
        bg_con=VGroup()
        for xi, yi in zip(x,y):
            bg_con.add(Dot(point=[xi,yi,0],radius=0.03, fill_opacity=0.3))
        self.add(bg_con)
        self.wait()
        red_dot = Dot(radius= 0.3, color= RED)
        red_dot.shift(UP*3)



        white_dots = [Dot(point=LEFT) for i in range(0,10)]
        self.add(red_dot)
        [dot.rotate(np.random.uniform(-PI,PI) ,about_point= red_dot.get_center()) for dot in white_dots]
        for i, dot in enumerate(white_dots):
            dot.time= 0.1*i
        self.add(*white_dots)

        def update_red_dot(mob,dt):
            mob.rotate(angle= -0.01,about_point= ORIGIN)
            #mob.shift(RIGHT*dt*1) #### CHANGE A
        def update_white_dot(mob,dt):
            if mob.time > 1:
                mob.time=0
                mob.move_to(red_dot.get_center()+RIGHT)
                mob.rotate(np.random.uniform(-PI,PI) ,about_point= red_dot.get_center())
            #            mob.shift(RIGHT*dt*1) #### CHANGE B
            mob.rotate(angle= -0.01,about_point= ORIGIN)

            point= mob.get_center() + (red_dot.get_center()- mob.get_center())*mob.time
            mob.move_to(point)
            mob.time += 1/60

        red_dot.add_updater(update_red_dot)
        [white_dot.add_updater(update_white_dot) for white_dot in white_dots]

        path = VMobject()
        dot = red_dot
        path.set_points_as_corners([dot.get_center(),dot.get_center()+UP*0.01])
        def update_path(path):
            previus_path = path.copy()
            previus_path.add_points_as_corners([dot.get_center()])
            path.become(previus_path)

        path.add_updater(update_path)

        self.add(path,dot)
        self.wait(3.2)

if __name__ == "__main__":
    manim_main = Path.home() / "projects/manim/manim.py"
    command_A =   f"{manim_main}  -l -p -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = f"{Path(__file__).resolve()}   "
    os.system(command_A + command_B)