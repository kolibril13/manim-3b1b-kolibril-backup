from manimlib.imports import *
# from active_projects.ode.part2.shared_constructs import *
from active_projects.diffyq.part2.shared_constructs import *
from hendrik_active.resusable_hendrik.histograms import *
from hendrik_active.resusable_hendrik.image_pro import *
class Ex1(ThreeDScene):

    global pixel_len
    pixel_len = 5

    def empty_k_space(self):
        PIXELS = pixel_len*pixel_len
        square_ALL = [Square(fill_opacity=1, side_length=1) for i in range(0, PIXELS)]
        j = 0
        for i, square_to_move in enumerate(square_ALL):
            if i % np.sqrt(PIXELS) == 0:
                j += 1
            k = i - j * np.sqrt(PIXELS)
            square_to_move.move_to((LEFT * k + j * DOWN) )
        term = VGroup(*[square for square in square_ALL])
        print(term.get_center())

        return term

    def fill_k_space(self, term, img_array):
        t_objects = [t for t in term.submobjects]
        #create color gradient
        colors = [BLACK, WHITE]
        colors = color_gradient(colors, 256)
        img_array=img_array.flatten()
        #create dots array
        dots= []
        vert_line = []

        #make the settings for each pixel
        for i, el in enumerate(t_objects):
            wanted_color = colors[img_array[i]]
            wanted_opacity = img_array[i] / 255
            wanted_height = wanted_opacity *2

            #set height
            dot= Dot()
            dot.move_to(el.get_center())
            dot.set_z(wanted_height)
            #set color
            dot.set_color(wanted_color)
            el.set_color(wanted_color)

            #make line
            line=Line(dot.get_center(),
                      [ dot.get_x(),dot.get_y(),0],
                      color=wanted_color)
            #set opacity
            # line.set_opacity(wanted_opacity + 0.2)
            # dot.set_opacity(wanted_opacity + 0.2)
            # el.set_opacity(wanted_opacity + 0.2)
            # append the pixels
            dots.append(dot)
            vert_line.append(line)

        return VGroup(*vert_line), VGroup(*dots)

    def update_k_space_image(self, image,scale_factor):
        term = self.empty_k_space()
        term.move_to(ORIGIN)
        # first image
        line, dots = self.fill_k_space(term, image)
        all1 = VGroup(term, line, dots).scale_about_point(scale_factor, ORIGIN)
        return all1
    def construct(self):
        speed=4
        scale_factor= 1.5
        axes = ThreeDAxes()

        #camera settings
        #self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        self.set_camera_orientation(phi=0 * DEGREES, theta=0 * DEGREES)
        self.begin_ambient_camera_rotation(rate=1/(speed))  # Start move camera


        #make the image:
        img_array1= np.uint8(np.random.randint(1, 255, (pixel_len, pixel_len)))
        all1= self.update_k_space_image(img_array1,scale_factor)
        # #second image
        img_array2= np.uint8(np.random.randint(1, 255, (pixel_len, pixel_len)))
        all2= self.update_k_space_image(img_array2,scale_factor)
        #third image
        all3= self.update_k_space_image(img_array1,scale_factor)

        all1.set_shade_in_3d(True)
        all2.set_shade_in_3d(True)
        all3.set_shade_in_3d(True)
        self.add(all1)
        self.play(Transform(all1,all2),run_time=PI*speed)
        self.play(Transform(all1,all3),run_time=PI*speed)
if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim  -p -s  -c '#1C758A' --video_dir ~/Downloads/  "
    command_B = module_name + " " + "Ex1"
    os.system(command_A + command_B)