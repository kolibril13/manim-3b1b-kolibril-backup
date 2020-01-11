from manimlib.imports import *

class No10(Scene):
    def construct(self):
        N=2000
        concentration = N
        x  = np.random.uniform(-0.445*FRAME_WIDTH,0.445*FRAME_WIDTH, np.uint(concentration))
        y = np.random.uniform(-0.145*FRAME_HEIGHT,0.145*FRAME_HEIGHT, np.uint(concentration))
        sq= Rectangle(width=0.45*FRAME_WIDTH*2,height= 0.15*FRAME_HEIGHT*2)
        bg_con=VGroup()
        for xi, yi in zip(x,y):
            bg_con.add(Dot(point=[xi,yi,0],radius=0.03, fill_opacity=0.3))
        self.add(bg_con, sq)
        self.wait()

if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p -s  -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"No10"
    os.system(command_A + command_B)
