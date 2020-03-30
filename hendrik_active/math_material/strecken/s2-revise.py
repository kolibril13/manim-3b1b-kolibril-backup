from manimlib.imports import *

class s2rev(Scene):
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
        v_along_endtoend = p2-p1
        v_along = v_along_endtoend/get_norm(v_along_endtoend)
        v_vert = np.array([v_along[1],-v_along[0] , 0 ])
        offset_connect =0.25
        offset_along= 0.5
        offset_vert = 0.1
        u1 = p1 + v_along*offset_along - v_vert*offset_vert
        v1 = p1 + v_along*offset_along + v_vert*offset_vert
        u2 = p2 - v_along*offset_along - v_vert*offset_vert
        v2 = p2 - v_along*offset_along + v_vert*offset_vert
        s1= p1 + v_along*offset_connect
        s2 = p2 - v_along*offset_connect
        self.add(Dot(u1), Dot(v1),Dot(u2), Dot(v2))
        LU = Line(u1, u2)
        LV = Line(v1, v2)
        self.add(LU, LV )
        Lp1s1 = Line(p1, s1)
        Ls1u1 = Line(s1,u1)
        Ls1v1 = Line(s1,v1)

        self.add(Lp1s1,Ls1u1,Ls1v1)

        Lp2s2 = Line(p2, s2)
        Ls2u2 = Line(s2,u2)
        Ls2v2 = Line(s2,v2)
        self.add(Lp2s2,Ls2u2,Ls2v2)

        self.add(dot1,dot2)


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim   -s -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"s2rev"
    os.system(command_A + command_B)