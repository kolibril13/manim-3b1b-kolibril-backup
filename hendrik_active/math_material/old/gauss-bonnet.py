from manimlib.imports import *

class Gauss(Scene):
    def construct(self):
        A = np.array([-2,-1,0])
        B = np.array([2,-1,0])
        C = np.array([0,2,0])
        triang = Polygon(A,B,C)
        lineA1= Line(A,B , color=YELLOW)
        lineB1= Line(B,C , color=YELLOW)
        B_ext= B + (B-A)/np.linalg.norm(B-A)
        lineA2= DashedLine(B ,B_ext , color=YELLOW)
        self.add(triang)
        lineA=VGroup(lineA1,lineA2)
        self.play(ShowCreation(lineA), run_time=2)
        pairs = [
            (lineA1.get_angle(), lineB1.get_angle())]
        arcs = []
        for start, angle in pairs:
            arc = Arc(
                angle = angle,
                radius = 1,
                start_angle = start,
                color = GREEN
            )
            arcs.append(arc)
        arc[0].shift(B)
        alpha = TexMobject("\\alpha").scale(0.6)
        beta = TexMobject("\pi-\\alpha").scale(0.6)
        alpha.next_to(B, 1*UP+1.5*LEFT)
        beta.next_to(B, 1*UP+0.2*RIGHT)
        angleB= VGroup(arc[0],alpha,beta)
        self.play(ShowCreation(angleB))

if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p   --video_dir ~/Downloads/  "
    command_B = module_name +" " +"Gauss"
    os.system(command_A + command_B)