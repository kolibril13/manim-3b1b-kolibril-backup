from manimlib.imports import *
from manimlib.utils.bezier import bezier

class spline(Scene):
    def construct(self):
        dot = Dot()
        self.add(dot)
        pA1= [-6,2,0]
        pA2= [-2,2,0]
        pB1= [-6,-2,0]
        pB2= [-2,-2,0]
        pC1= [2,0,0]
        pC2= [6,0,0]
        lA = Line(pA1,pA2)
        lB = Line(pB1,pB2)
        lC = Line(pC1,pC2)
        offsetab= 3
        offsetc=2
        lA.add_cubic_bezier_curve(pA2,pA2+RIGHT*offsetab,pC1+LEFT*offsetc,pC1)
        lB.add_cubic_bezier_curve(pB2,pB2+RIGHT*offsetab,pC1+LEFT*offsetc,pC1)
        self.add(lA,lB,lC)
        curve_exp = VMobject()
        # l1.sector.add_cubic_bezier_curve_to([
        # l1.sector.add_cubic_bezier_curve_to([
        # curve_exp.set_points_smoothly([p2,p2+RIGHT, ORIGIN,p3] )
        # curve_exp.set_points_smoothly([p2,p2+RIGHT, ORIGIN,p3] )
        # self.add(curve_exp)
#

if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim  -s -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"spline"
    os.system(command_A + command_B)