from manimlib.imports import *

class Gauss(Scene):

    def show_pendulum(self, arc_angle = np.pi, arc_color = GREEN):
        self.c_label= Dot()
        self.p_dot= Dot()
        self.p_point= [0,0,0]
        self.c_point = [1,1,1]
        words = TextMobject(": Instantaneous center of rotation")
        words.next_to(self.c_label)
        line = Line(self.p_point, self.c_point)
        line_angle = line.get_angle()+np.pi
        line_length = line.get_length()
        line.add(self.p_dot.copy())
        line.get_center = lambda : self.c_point
        tangent_line = Line(3*LEFT, 3*RIGHT)
        tangent_line.rotate(line_angle-np.pi/2)
        tangent_line.shift(self.p_point)
        tangent_line.set_color(arc_color)
        right_angle_symbol = VMobject(
            Line(UP, UP+RIGHT),
            Line(UP+RIGHT, RIGHT)
        )
        right_angle_symbol.scale(0.3)
        right_angle_symbol.rotate(tangent_line.get_angle()+np.pi)
        right_angle_symbol.shift(self.p_point)

        self.play(ShowCreation(line))
        self.play(ShimmerIn(words))
        self.wait()
        pairs = [
            (line_angle, arc_angle/2),
            (line_angle+arc_angle/2, -arc_angle),
            (line_angle-arc_angle/2, arc_angle/2),
        ]
        arcs = []
        for start, angle in pairs:
            arc = Arc(
                angle = angle,
                radius = line_length,
                start_angle = start,
                color = GREEN
            )
            arc.shift(self.c_point)
            self.play(
                ShowCreation(arc),
                ApplyMethod(
                    line.rotate_in_place,
                    angle,
                    path_func = path_along_arc(angle)
                ),
                run_time = 2
            )
            arcs.append(arc)
        self.wait()
        self.play(Transform(arcs[1], tangent_line))
        self.add(tangent_line)
        self.play(ShowCreation(right_angle_symbol))
        self.wait()

        self.tangent_line = tangent_line
        self.right_angle_symbol = right_angle_symbol
        self.pc_line = line
        self.remove(words, *arcs)
    def construct(self):


        self.show_pendulum()
        A = np.array([-2,-1,0])
        B = np.array([2,-1,0])
        C = np.array([0,2,0])
        triang = Polygon(A,B,C)
        line1= Line(A,B , color=YELLOW)
        B_ext= B + 0.2*(B-A)
        line2= DashedLine(B ,B_ext , color=YELLOW)
        self.add(triang)
        lineA=VGroup(line1,line2)
        self.play(ShowCreation(lineA), run_time=2)
        self.wait(2)

    
if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p -s  --video_dir ~/Downloads/  "
    command_B = module_name +" " +"Gauss"
    os.system(command_A + command_B)