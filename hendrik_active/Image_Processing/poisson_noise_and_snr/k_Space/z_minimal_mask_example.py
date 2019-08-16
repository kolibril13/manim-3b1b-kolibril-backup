from manimlib.imports import *
from hendrik_active.Image_Processing.poisson_noise_and_snr.k_Space.ImProImports import \
    FourierMathJuggling,Image_coordinate_system, KSpace, Realspace,Comp_axis


class MathMagic:
    def __init__(self, array):
        self.array_input = array
        self.array_output = self.array_input.copy()
        self.pixels = len(self.array_input)

    def get_array(self):
        return self.array_output

    # def relu(self,start,end):
    #     return np.maximum(start, end)

    def linear_step_func(self,x, x0, x1):
        x = np.maximum(x0, x)
        x = np.minimum(x, x1)
        x = x / x1
        return x


    def p2(self, step): #creates a function that returns 0.5, .. 0.5 ,0.6...1
        val= self.linear_step_func(step,0.5,1)
        return val

    def p1(self, step): #creates a function that returns 0.5, .. 0.5 ,0.6...1
        val= self.linear_step_func(step,0,0.5)
        return val

    def make_mask(self,step): # step goes from 0 to 1
        mask= np.full((3,3),self.p2(step))
        mask[1,1]=self.p1(step)
        return mask

    def apply_mask(self,t):
        mask= self.make_mask(t)
        self.array_output=  self.array_input*mask
np.set_printoptions(precision=1)
np.set_printoptions(suppress=True)
class se(Scene):
    def construct(self):
        sq_array = VGroup(*[Square(side_length=0.1).move_to((LEFT * 2*i + 2*UP)) for i in range(0, 3)])
        sq_array.add(*[Square(side_length=0.1).move_to((LEFT * 2*i )) for i in range(0, 3)])
        sq_array.add(*[Square(side_length=0.1).move_to((LEFT * 2*i - 2*UP )) for i in range(0, 3)])
        sq_array.move_to(ORIGIN).scale(1.3)
        self.add(sq_array)
        my_tracker = ValueTracker(0)
        end_val = 1
        final_heights = np.ones((3,3))
        a_math = MathMagic(final_heights)
        def updater_func(mob):
                a_math.apply_mask(my_tracker.get_value())
                new_array=a_math.get_array()
                hght_vals= new_array.flatten()
                print(hght_vals)
                [el.set_height(i) for i,el in zip(hght_vals,sq_array.submobjects) ]
                return mob

        self.play(my_tracker.increment_value, end_val,
                  UpdateFromFunc(sq_array, updater_func),
                  rate_func=linear, run_time=2)
        self.wait(2)


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim  -p -l  -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"se"
    os.system(command_A + command_B)