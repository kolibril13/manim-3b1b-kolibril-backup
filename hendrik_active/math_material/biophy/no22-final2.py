from manimlib.imports import *

class No20(Scene):
    def construct(self):
        # background of scene
        N=200#0  #->2000 final
        concentration_fraction= 0.5
        concentration = concentration_fraction* N
        x  = np.random.uniform(-0.445*FRAME_WIDTH,0.445*FRAME_WIDTH, np.uint(concentration))
        y = np.random.uniform(-0.145*FRAME_HEIGHT,0.145*FRAME_HEIGHT, np.uint(concentration))
        sq= Rectangle(width=0.45*FRAME_WIDTH*2,height= 0.15*FRAME_HEIGHT*2)
        sq.set_style(stroke_color=DRAC_YELLOW)
        bg_con=VGroup()
        for xi, yi in zip(x,y):
            bg_con.add(Dot(point=[xi,yi,0],radius=0.03, fill_opacity=0.3))
        self.add(bg_con, sq)
        ## equation
        eq1 = TexMobject(r"\frac{dn^+}{dt} = "," - k^+_{off}", " + c_A \cdot k^+_{on}")
        eq1.submobjects[2].set_style(fill_opacity=0)
        self.add(eq1.to_edge(DL))


    # rate equation
        kP_off= 1.4
        kP_on = 11.6

        blue_dot = Dot(radius= 0.3, color= RED)

        wdPoffs = [Dot(point=LEFT) for i in range(0,2)]
        for val, wdPoff in enumerate(wdPoffs):
            wdPoff.move_to(blue_dot.get_center()+DOWN)
            wdPoff.rotate(np.random.uniform( -np.radians(30), np.radians(30)  ) ,about_point= blue_dot.get_center())
            wdPoff.set_opacity(0)
            wdPoff.subdot= Dot(point=blue_dot.get_center())
            wdPoff.time=val*0.5
        total_growth_particles= int(kP_on/kP_off*2)
        print(total_growth_particles)
        wdPons = [Dot(point=LEFT) for i in range(0,total_growth_particles)]
        for val, wdPon in enumerate(wdPoffs):
            wdPon.move_to(blue_dot.get_center()+DOWN)
            wdPon.rotate(np.random.uniform( -np.radians(30), np.radians(30)  ) ,about_point= blue_dot.get_center())
            wdPon.set_opacity(0)
            wdPon.subdot= Dot(point=blue_dot.get_center())
            wdPon.time=val*0.5

        def dnP():
            return kP_on*concentration_fraction- kP_off
        print(dnP())

        def shift_elements_by_rate(element, dt):
            element.shift(RIGHT*dt*dnP()*0.5)
        def update_red_dot(mob,dt):
            shift_elements_by_rate(mob, dt)
        def updat_wdPoff(mob,dt):
            if mob.time > 1:
                mob.time=0
                mob.move_to(blue_dot.get_center()+DOWN)
                mob.rotate(np.random.uniform( -np.radians(30), np.radians(30)  ) ,about_point= blue_dot.get_center())
            shift_elements_by_rate(mob, dt)
            point= blue_dot.get_center() + (mob.get_center()- blue_dot.get_center())*mob.time
            mob.subdot.move_to(point)
            mob.subdot.set_opacity(1-mob.time)
            mob.time += 1/self.camera.frame_rate  # one second

        blue_dot.add_updater(update_red_dot)
        [wdPoff.add_updater(updat_wdPoff)  for wdPoff in wdPoffs]

        #microtuble
        tubel= Line(sq.get_corner(LEFT), blue_dot.get_center(), stroke_width= 20)
        self.add(tubel)
        def update_line(mob):
            mob.become(Line(sq.get_corner(LEFT),blue_dot.get_center(), stroke_width= 20))
        tubel.add_updater(update_line)

        self.add(blue_dot)
        self.add(*wdPoffs)
        self.add(*[wdPoff.subdot for wdPoff in wdPoffs])
        self.wait(3)

if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p -l -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"No20"
    os.system(command_A + command_B)
