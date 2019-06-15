from big_ol_pile_of_manim_imports import *

class music(Scene):

    def MuseMobject(self, MUSIC):

        FOLDER = "/home/jan-hendrik/python/projects/manim-new/projects_hendrik/music_template/"
        FILE = "tex_template_music.tex"
        TEX_TEXT_TO_REPLACE= MUSIC
        with open(FOLDER+FILE, "r") as infile:
            TEMPLATE_TEXT_FILE_BODY = infile.read()
            TEMPLATE_TEX_FILE_BODY = TEMPLATE_TEXT_FILE_BODY.replace(
                "NOTES_FROM_PYTHON",
                TEX_TEXT_TO_REPLACE,
            )
        new_body= TEMPLATE_TEX_FILE_BODY
        temporary_tex_doc= "music_temporary.tex"
        temp_tex= FOLDER + temporary_tex_doc
        with open(temp_tex, "w", encoding="utf-8") as outfile:
            outfile.write(new_body)

        res= os.system("cd " + FOLDER + "&& latex -shell-escape " + temp_tex)
        temp1 = "out1.svg"
        exit_code = os.system("cd " + FOLDER + " && eps2svg out-abc.eps " + temp1)
        # temp2 = "out2.svg"
        # os.system("cd " + FOLDER + "&& cairosvg " + temp1 + " -f svg -o " + temp2)
        dat = FOLDER + temp1
        t = SVGMobject(dat)

        ### check for streight lines
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
            # print(new)
            if new[0] == new[2]:
                t.submobjects[index].set_stroke(width=3)
                t.submobjects[index].set_color(color=LIGHT_BROWN)
            if new[1] == new[3]:
                t.submobjects[index].set_stroke(width=2)
                t.submobjects[index].set_color(color=BLUE)
        return t

    def construct(self):
        MUSIC = "c'agc|f(bg)c"
        Dot()
        mu=self.MuseMobject(MUSIC)
        mu.scale(2)
        # for element in mu.submobjects:
        term = VGroup(*[element for element in mu.submobjects])
        self.play(FadeInFromDown(term),lag_ratio=10, run_time= 10, rate_func=linear)
        # self.play(Transform(original_square, term), lag_ratio=0.2)
        for i in mu.submobjects:
            print(i)
            breakpoint()
        self.wait()


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command = "python3.7 -m manim  -a -p -s " + module_name
    os.system(command) 