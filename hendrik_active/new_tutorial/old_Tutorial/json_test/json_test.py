from manimlib.imports import *


def func(t):
    return np.array((np.sin(2*t), np.sin(3*t),0))

func=ParametricFunction(func, t_max=TAU, fill_opacity=0)
x=func.points
d= {f"p{num}": tuple(el[0:2]) for num,el in enumerate(x)}

import json

with open("data.json","w") as write_file:
    json.dump(d, write_file,indent=2)

