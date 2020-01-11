from manimlib.imports import *

class No4(Scene):
    def construct(self):
        N=1000
        concentration = 0.8*N
        x  = np.random.uniform(-0.5*FRAME_WIDTH,0.5*FRAME_WIDTH, np.uint(concentration))
        y = np.random.uniform(-0.5*FRAME_HEIGHT,0.5*FRAME_HEIGHT, np.uint(concentration))
        bg_con=VGroup()
        for xi, yi in zip(x,y):
            bg_con.add(Dot(point=[xi,yi,0],radius=0.03, fill_opacity=0.3))
        self.add(bg_con)
        self.wait()


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p -s -l  -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"No4"
    os.system(command_A + command_B)
