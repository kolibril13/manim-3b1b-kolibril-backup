#old idea:

a=[1,1,1]
b=[0,1,0]
c=[0,0,1]
d= [1,0,0]
list=[a]
for i, opa in enumerate(list):
    if i>0:
        self.remove(self.mobjects[self.index_text])
    text = f"Opacity plane:{opa[0]}, dot:{opa[1]}, line:{opa[2]}"
    te = TextMobject(text).scale(2)
    te.to_corner(UL)
    self.add_fixed_in_frame_mobjects(te)
    self.index_text = len(self.mobjects) - 1
    my_plane.set_subobject_opacity(img,opa)
    self.wait(2)