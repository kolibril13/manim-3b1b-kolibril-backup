from manimlib.imports import *

class Shapes(Scene):
    CONFIG = {
        "pixel_values": np.arange(0,255)
    }
    def construct(self):
        print("Start")
        N=256
        MAX=22
        img_A= self.create_array(N,MAX)
        img1= ImageMobject(img_A,color= RED)
        img1.scale(2)
        IMG2= [ImageMobject(self.create_array(N,MAXI)) for
               MAXI in self.pixel_values]
        img1.next_to(LEFT_SIDE+np.array((3,0,0)))
        self.add(img1)
        for n, img2_element in enumerate(IMG2):
            img2_element.next_to(img1,RIGHT)
            img2_element.scale(2)
            self.add( img2_element)
            self.wait(0.01)
            print(n)
        self.play(GrowFromCenter(circle))

        self.wait(2)

    def create_array(self,n,max):
        img_A = np.zeros((n, n))
        for i in range(0, max):
            img_A[max - 1 - i] = i
        img_A = np.uint8(img_A)
        return img_A
if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command = "python3.7 -m manim -pl --leave_progress_bars " + module_name + " Shapes "
    os.system(command)

