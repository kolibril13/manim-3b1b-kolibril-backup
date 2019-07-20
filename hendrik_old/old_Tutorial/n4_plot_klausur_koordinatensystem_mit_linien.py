from manimlib.imports import *
class Generation(GraphScene):
    CONFIG = {
        "y_axis_label": r"T[$^\circ C$]",
        "x_axis_label": r"$\Delta Q$",
        "y_min": -8,
        "y_max": 30,
        "x_min": 0,
        "x_max": 40,
        "y_labeled_nums": np.arange(-5,34,5),
        "x_labeled_nums": np.arange(0, 40, 5),

    }

    def construct(self):
        data= [20,0, 0,-5]
        zufuhr= np.array([0,8,30,1])
        x   = [0, 8,38,39]
        print(x)
        squ = Rectangle(height=np.sum(TOP) * 2, width=np.sum(LEFT_SIDE) * 2,
                        fill_color=DRAC_GREY, fill_opacity=0.8)
        #make the intro of the plot
        self.play(FadeIn(squ))
        self.setup_axes(animate=True)
        dot_ALL = [Dot() for k in range(0,len(data))]
        for time , dot in enumerate(dot_ALL):
            dot.move_to(self.coords_to_point(x[time], data[time]))
            self.add(dot)
            self.wait(1)
            print(time)
        l1= Line(dot_ALL[0].get_center(), dot_ALL[1].get_center())
        l2= Line(dot_ALL[1].get_center(), dot_ALL[2].get_center())
        l3= Line(dot_ALL[2].get_center(), dot_ALL[3].get_center())

        self.add(l1,l2,l3)
        self.wait()

if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p -s -t -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name + " " + "Generation"
    os.system(command_A + command_B)
