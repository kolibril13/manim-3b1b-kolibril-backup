from manimlib.imports import *


class FLOWER(VMobject):
    def __init__(self,a_deg, **kwargs):
        self.a_deg= a_deg%360
        VMobject.__init__(self, **kwargs)
        col = color_gradient([BLUE, RED],360)
        dot= Dot(fill_color= col[int(self.a_deg)]).scale(4)
        self.add(dot)
    def __str__(self):
        return f'FLOWER({self.a_deg})'

d=FLOWER(10)
# breakpoint()
d=FLOWER(20)
# breakpoint()
