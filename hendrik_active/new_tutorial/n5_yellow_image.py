import matplotlib as mpl
from manimlib.imports import *
from PIL import Image

class Images(Scene):
    def construct(self):
        cm_hot = mpl.cm.get_cmap('hot')
        rgb_array= np.ones((2,2))
        im = np.array(rgb_array)
        im = cm_hot(im)
        im = np.uint8(im * 255)
        im = Image.fromarray(im)

        matrix= Image.fromarray((im * 255).astype('uint8'))

        print(matrix)
        img= ImageMobject(matrix)
        img.scale(3)
        self.add(img)
        self.wait(2)
if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim  -p -l -s   -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"Images"
    os.system(command_A + command_B)