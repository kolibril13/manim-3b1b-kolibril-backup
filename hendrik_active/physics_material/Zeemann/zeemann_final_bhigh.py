from manim import *

def z_func(z0, w0, t):
    z_val= z0 * np.exp(1j*w0*t)
    return z_val.real

def get_u(u0, w0, e, B0, m,t) :
    u_val = u0 * np.exp(1j*(w0-(e*B0)/(2*m))*t)
    return u_val

def get_v(u0, w0, e, B0, m,t) :
    v_val = u0 * np.exp(1j*(w0+(e*B0)/(2*m))*t)
    return v_val

class Zeemann1(Scene):
    def construct(self):
        num1 = TexMobject(r"{\large \textcircled{\small 2}} ")
        self.add(num1)

        z0=1
        u0= 1
        v0= 1
        w0=3
        B0=3.5
        e  =m = 1

        electron1 = Dot()
        electron1.time= 0
        def update_electron1(d,dt):
            d.time += dt
            p1= z_func(z0,w0, d.time)
            d.become(Dot(point=[p1*2.5,0,0]).shift(3*LEFT+2.5*DOWN).set_color(BLUE).scale(2))
        electron1.add_updater(update_electron1)

        electron2 = Dot()
        electron2.time= 0
        def update_electron2(d,dt):
            d.time += dt
            p2= (get_u(u0, w0, e, B0, m,d.time))
            d.become(Dot([p2.imag,p2.real*2.5,0]).shift(RIGHT*2).set_color(BLUE).scale(2))
        electron2.add_updater(update_electron2)

        electron3 = Dot()
        electron3.time= 0
        def update_electron3(d,dt):
            d.time += dt
            p3= (get_v(v0, w0, e, B0, m,d.time))
            d.become(Dot([-p3.imag,p3.real*2.5,0]).shift(RIGHT*5).set_color(BLUE).scale(2))
        electron3.add_updater(update_electron3)


        result_electron = Dot()
        result_electron.time= 0
        def update_result_electron(d,dt):
            d.time += dt
            x= electron1.get_x()
            y= (get_v(v0, w0, e, 0, m,d.time)).real*2.5
            d.become(Dot([x,y,0]).set_color(RED).scale(2))
        result_electron.add_updater(update_result_electron)

        ellipse1 = Ellipse(width=2, height=5).shift(2 * RIGHT).set_color(BLACK)
        ellipse2 = Ellipse(width=2, height=5).shift(5 * RIGHT).set_color(BLACK)

        p1 = [-5.5, -2.5, 0]
        p2 = [-0.5, -2.5, 0]
        p3 = [-0.5, 2.5, 0]
        l1 = Line(start=p1, end=p2).set_color(BLACK)
        l2 = Line(start=p2, end=p3).set_color(BLACK)
        l3 = Line(start=p3, end=p1).set_color(BLACK)


        bgArrows=[Arrow(start=[-6,0,0],end=[7,0,0]).shift(DOWN*0.8*j) for j in range(-4,5)]
        bgArrows = VGroup(*bgArrows).set_color(YELLOW).set_opacity(0.4)
        self.add(bgArrows)
        self.add(ellipse1,ellipse2,l1,l2,l3)
        self.add(electron1,electron2,electron3,result_electron)
        bo=TexMobject(r"\vec{B}_0 > 0").set_color( BLACK)
        bo.next_to(bgArrows.submobjects[0], DOWN,buff=0)
        bo.align_to(bgArrows.submobjects[0], LEFT)
        self.add(bo)

        num1 = TexMobject(r"{\large \textcircled{\small 1}} ").set_color(BLACK)
        num1.next_to(l1,DOWN,buff=SMALL_BUFF)
        num2 = TexMobject(r"{\large \textcircled{\small 2}} ").set_color(BLACK)
        num3 = TexMobject(r"{\large \textcircled{\small 3}} ").set_color(BLACK)
        num2.next_to(num3,UP)
        num23 = VGroup(num2,num3)
        num23.next_to(l2, RIGHT,buff=SMALL_BUFF)
        self.add(num2.copy().next_to(ellipse1,DOWN,buff=SMALL_BUFF))
        self.add(num3.copy().next_to(ellipse2,DOWN,buff=SMALL_BUFF))
        self.add(num1,num23)

        self.wait(10)



if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p  -c WHITE --video_dir ~/Downloads/  "
    command_B = module_name + " " + "Zeemann1"
    os.system(command_A + command_B)
