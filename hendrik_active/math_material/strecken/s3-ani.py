from manimlib.imports import *

class s3ani(Scene):
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
        deltap = p1-p2
        deltapnorm = deltap/get_norm(deltap)

        theta = np.radians(90)
        r = np.array(( (np.cos(theta), -np.sin(theta),   0  ),
                       (np.sin(theta),  np.cos(theta),   0  ),
                       (0            ,     0         ,   0  )))
        senk= r.dot(deltapnorm)
        offset = 0.1
        offset_along= 0.5
        offset_connect =0.25
        U1 = p1+ senk*offset -deltapnorm*offset_along
        U2 = p2+ senk*offset +deltapnorm*offset_along
        V1 = p1 - senk*offset -deltapnorm*offset_along
        V2 = p2 - senk*offset+deltapnorm*offset_along
        s1 = p1-offset_connect*deltapnorm
        s2 = p2+offset_connect*deltapnorm
        LU = Line(U1, U2)
        LV = Line(V1, V2)
        #self.add(LU, LV )
        Lp1s1 = Line(p1, s1)
        # Ls1u1 = Line(s1,U1)
        # Ls1v1 = Line(s1,V1)

        #self.add(Lp1s1)#,Ls1u1,Ls1v1)
        Lp1s1.add_cubic_bezier_curve(s1,s1-deltapnorm*0.1,V1+deltapnorm*0.1,V1-deltapnorm*0.01)
        Lp1s1.add_cubic_bezier_curve(s1,s1-deltapnorm*0.1,U1+deltapnorm*0.1,U1)

        Lp2s2 = Line(p2, s2)
        # Ls2u2 = Line(s2,U2)
        # Ls2v2 = Line(s2,V2)
        #self.add(Lp2s2)   #,Ls2u2,Ls2v2)
        Lp2s2.add_cubic_bezier_curve(s2,s2+deltapnorm*0.1,V2-deltapnorm*0.1,V2)
        Lp2s2.add_cubic_bezier_curve(s2,s2+deltapnorm*0.1,U2-deltapnorm*0.1,U2)

        #self.add(dot1,dot2)
        start=VGroup(Line(dot1.get_center(), dot2.get_center()),dot1.copy(),dot2.copy()).scale(0.5)
        end= VGroup(Lp1s1, Lp2s2,LU,LV,dot1,dot2)
        end.scale(2)
        self.add(start)
        self.wait(1)
        self.play(ClockwiseTransform(start,end), run_time=3)
        self.wait(1)
if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim   -p  -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"s3ani"
    os.system(command_A + command_B)