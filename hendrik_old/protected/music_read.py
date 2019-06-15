from big_ol_pile_of_manim_imports import *

class music(Scene):

    def MuseMobject(self):

        FOLDER = "/home/jan-hendrik/python/projects/manim-new/projects_hendrik/music_template/"
        FILE = "tex_template_music.tex"
        os.system("cd " + FOLDER + "&& latex -shell-escape " + FILE)
        temp1 = "out1.svg"
        os.system("cd " + FOLDER + " && eps2svg out-abc.eps " + temp1)
        temp2 = "out2.svg"
        os.system("cd " + FOLDER + "&& cairosvg " + temp1 + " -f svg -o " + temp2)
        dat = FOLDER + temp2
        t = SVGMobject(dat) # or stroke_width = 2
        print(dir(t))

        ### check for streight lines
        streight_line_check = []
        for index,element in enumerate(t.submobjects):
            s=element.path_string
            s2 = s.split(" ")
            # print(s2)
            new = []
            for element in s2:
                try:
                    new.append(float(element))
                except ValueError:
                    pass
            print(new)
            if new[0] == new[2]:
                t.submobjects[index].set_stroke(width=3)
                t.submobjects[index].set_color(color=LIGHT_BROWN)
            if new[1] == new[3]:
                t.submobjects[index].set_stroke(width=2)
                t.submobjects[index].set_color(color=BLUE)
        for j in streight_line_check:
            t.submobjects[j].set_stroke(width=2)
            t.submobjects[j].set_color(color= BROWN)
        self.add(t)

    def construct(self):
        self.MuseMobject()
        self.wait(2)

if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command = "python3.7 -m manim  -a -p -s " + module_name
    os.system(command) 