
from hendrik_active.Image_Processing.FourierIdea.ImProImports import *
from manimlib.imports import *
linear_step_func=StepFunctions.linear_step_func
global k_plane_size
k_plane_size=0.7


################################IMPORTANT HERE
scene = "Scene01_different_amplitudes"  # FULL ANIMATION SCENE phase with real out
class Scene01_different_amplitudes(Scene):  # with real plane on the right

    def construct(self):
       self.add(FLOWER(20).scale(1))
       self.add(Dot())

if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim  -l -s -p     -c '#1C758A' --video_dir ~/Downloads/  "
    command_B = module_name +" " + scene
    os.system(command_A + command_B)