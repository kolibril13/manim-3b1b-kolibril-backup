from manimlib.imports import *


class Shapes(Scene):
    CONFIG ={
        "color": [DARK_BLUE , DARK_BROWN, BLUE_E, BLUE_D, BLUE_A, TEAL_B, GREEN_B, YELLOW_E],
        "radius": [1+rad*0.1 for rad,col in enumerate("color")]
    }
    def construct(self):
        print("Startii")
        cirlce_Subset=[]
        x=[]
        for k in np.arange(0,4,1):

            cirlce_Subset.extend([Circle(radius=rad+k,stroke_width=10, color = col)
                         for rad,col in zip(self.radius,self.color)])
            print(cirlce_Subset)
            x.append(VGroup(cirlce_Subset))
        #     # cirlce_Subset.append(Dot())
        # print(cirlce_Subset)
        # for circ in cirlce_Subset:
        for element in x:
            self.play(GrowFromCenter(element))
        self.wait(2)


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command = "python3.7 -m manim  -p  -a --leave_progress_bars " + module_name
    os.system(command)

