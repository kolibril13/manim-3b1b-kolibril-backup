from manimlib.imports import *

class lag3(ThreeDScene):
    def construct(self):
        axes=Axes()
        self.t_offset=0
        def func(t):
            return np.array((np.cos(2* t), 2*np.sin( t), 0))
        func = ParametricFunction(func, t_max=2*TAU, fill_opacity=0)
        curve=func
        dot=Dot()
        label = TextMobject("(x(t),y(t))")
        label.next_to(dot,RIGHT, buff=SMALL_BUFF)
        dot.move_to(curve.point_from_proportion(0))

        def update_dot(mob,dt):
            rate=dt*0.3
            mob.move_to(curve.point_from_proportion((self.t_offset + rate)%1))
            self.t_offset += rate

        def update_label(obj):
            obj.next_to(dot,RIGHT,buff=SMALL_BUFF)


        dot.add_updater(update_dot)
        label.add_updater(update_label)


        self.add(axes)

        self.add(curve,dot,label)

        self.wait(4)
        self.wait(4)
        dot.clear_updaters()
        self.wait(2)
        self.wait()



if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p -l -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name + " " + "lag3"
    os.system(command_A + command_B)

