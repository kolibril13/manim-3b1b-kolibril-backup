from big_ol_pile_of_manim_imports import *

class music(Scene):

    def MuseMobject(self):
        FOLDER = "/home/jan-hendrik/python/projects/manim-new/projects_hendrik/music_template/"
        FILE = "tex_template_music.tex"
        os.system("cd " + FOLDER + "&& latex -shell-escape " + FILE)
        temp1 = "out1.svg"
        os.system("cd " + FOLDER +" && eps2svg out-abc.eps " + temp1)
        temp2=  "out2.svg"
        os.system("cd " + FOLDER + "&& cairosvg "+ temp1 +" -f svg -o " + temp2)
        dat = FOLDER + temp2
        t = SVGMobject(dat) # or stroke_width = 2
        t.scale(2)
        self.add(t)
    def construct(self):
        self.MuseMobject()
        self.wait(2)

if __name__ == "__main__": 
    module_name = os.path.basename(__file__)
    command = "python3.7 -m manim  -a -p  -s " + module_name
    os.system(command) 