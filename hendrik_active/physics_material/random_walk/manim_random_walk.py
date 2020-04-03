from manimlib.imports import *

class PrincipleComponent(Scene):
    def construct(self):
        steps=np.loadtxt("random_steps.csv")
        print(steps.shape)
        stepx= steps[0,:300]
        stepy= steps[1,:300]
        stepx=stepx/max(abs(stepx))*FRAME_WIDTH/2
        stepy=stepy/max(abs(stepy))*FRAME_HEIGHT/2
        Dots=VGroup(*[Dot(point=[x,y,0]) for x,y in zip(stepx,stepy)])
        self.play(FadeIn(Dots),lag_ratio=0.1 , run_time=3)


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim   -p -l -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"PrincipleComponent"
    os.system(command_A + command_B)