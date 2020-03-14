from manimlib.imports import *

class change(Scene):
    def construct(self):
        pixX,pixY=(200,200)
        im1 = [[(i+j)*5 for i in range(pixX)] for j in range(pixY)]
        im2 = np.random.randint(0, 255, size=(15, 15))
        im3=np.fromfunction(lambda i, j: 200*np.sin(j), (15, 15))
        a, b = np.meshgrid(np.linspace(-1,1,pixX), np.linspace(-1,1,pixY),sparse=False)
        im4 = 200*np.sqrt(a**2+b**2)
        imgs = [im1,im2,im3,im4]
        imgs_manim= []
        for val, i in enumerate(imgs):
            i = ImageMobject(np.uint8(i)).shift(5*LEFT)
            if val >= 1:
                i.next_to(imgs_manim[-1])
            imgs_manim.append(i)
        self.add(*imgs_manim)
        self.wait(2)

if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p  -l -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"change"
    os.system(command_A + command_B)