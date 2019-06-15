import os
from manimlib.utils.tex_file_writing import dvi_to_svg
FOLDER = "/home/jan-hendrik/python/projects/manim-new/projects_hendrik/music_template/"
FILE = "tex_template_music.tex"
os.system( "cd " + FOLDER + "&& "
           "latex -shell-escape "  + FILE)
dvi_file=FOLDER + "tex_template_music.dvi"
result  = dvi_file.replace(".dvi" , ".svg")
epsfile = dvi_file.replace(".dvi" , ".eps")

commands = ["cd " + FOLDER + "&& "
            "eps2svg out-abc.eps"]
os.system(" ".join(commands))