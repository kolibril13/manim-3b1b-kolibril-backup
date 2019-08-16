from manimlib.imports import *

class Images(Scene):
    def construct(self):
        print("Start")
        n=256
        img_A= np.uint8([[i for i in range(0,256)]  for j in range(0,256)])
        img1= ImageMobject(img_A).scale(2)
        img1.next_to(ORIGIN,LEFT_SIDE, SMALL_BUFF)
        self.add(img1)
        self.wait(1)
if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command = "python3.7 -m manim -p -s -a --leave_progress_bars " + module_name
    os.system(command)

