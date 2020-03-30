from manimlib.imports import *

class s1(Scene):
    def construct(self):
        np.random.seed(int(time.time()))
        np.random.seed(42)
        area = 4
        x1 = np.random.randint(-area,area)
        y1 =  np.random.randint(-area,area)
        p1 = np.array([x1,y1,0])
        dot1 = Dot(point=p1).set_color(BLUE)

        x2 =  np.random.randint(-area,area)
        y2 =  np.random.randint(-area,area)
        p2 =  np.array([x2,y2,0])
        dot2 = Dot(p2).set_color(RED)
        l1 = DashedLine([x1,y1,0], [x2,y2,0])
        #self.add(l1)
        self.add(dot1,dot2)
        self.wait(2)
        deltap = p1-p2
        deltapnorm = deltap/get_norm(deltap)

        theta = np.radians(90)
        r = np.array(( (np.cos(theta), -np.sin(theta),   0  ),
                       (np.sin(theta),  np.cos(theta),   0  ),
                       (0            ,     0         ,   0  )))
        senk= r.dot(deltapnorm)
        offset = 0.1
        offset_along= 0.5
        U1 = p1+ senk*offset
        U2 = p2+ senk*offset
        V1 = p1 - senk*offset
        V2 = p2 - senk*offset
        LU = Line(U1, U2)
        LV = Line(V1, V2)
        self.add(LU, LV )



if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim   -s -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"s1"
    os.system(command_A + command_B)