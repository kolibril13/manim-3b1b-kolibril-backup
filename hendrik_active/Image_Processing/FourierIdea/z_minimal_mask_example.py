from manimlib.imports import *

class MathMagic:
    def __init__(self, array):
        self.array_input = array
        self.array_output = self.array_input.copy()
        self.pixels = len(self.array_input)

    def get_array(self):
        return self.array_output

    @staticmethod
    def linear_step_func(x, x0, x1):
        y= np.piecewise(x, [
        x < x0,
        (x >= x0) & (x <= x1),
        x > x1],
            [0.,
            lambda x: x/(x1-x0)+x0/(x0-x1),
             1.]
        )
        return y

    def p3(self, step): #creates a function that returns 0.5, .. 0.5 ,0.6...1
        val= self.linear_step_func(step,0,1)
        return val

    def p2(self, step): #creates a function that returns 0.5, .. 0.5 ,0.6...1
        val= self.linear_step_func(step,0.5,1)
        return val

    def p1(self, step): #creates a function that returns 0,0.1,0.2...0.5
        val= self.linear_step_func(step,0,0.5)
        return val

    def make_mask(self,pixel,step): # step goes from 0 to 1
        mask= np.full(pixel,self.p2(step))
        mask[1,1]=self.p1(step)
        mask[4,4]=self.p3(step)
        return mask

    def apply_mask(self,pixel,t):
        mask= self.make_mask(pixel,t)
        self.array_output=  self.array_input*mask

class ControlSubmobjects(Scene):
    def construct(self):
        PIXEL = 5
        sq_array= VGroup()
        for x in range(PIXEL):
            for y in range(PIXEL):
                dot = Dot(point=(x, y, 0),side_length=0.1)
                sq_array.add(dot)
        sq_array.move_to(ORIGIN)
        self.add(sq_array)
        my_tracker = ValueTracker(0)
        end_val = 1
        final_heights = np.ones((PIXEL,PIXEL))
        a_math = MathMagic(final_heights)
        def updater_func(mob):
                a_math.apply_mask((PIXEL,PIXEL),my_tracker.get_value())
                new_array=a_math.get_array()
                hght_vals= new_array.flatten()
                [el.set_height(i+0.01) for i,el in zip(hght_vals,sq_array.submobjects) ]
                return mob

        self.play(my_tracker.increment_value, end_val,
                  UpdateFromFunc(sq_array, updater_func),
                  rate_func=linear, run_time=2)
        self.wait(2)


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim  -p  -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"ControlSubmobjects"
    os.system(command_A + command_B)