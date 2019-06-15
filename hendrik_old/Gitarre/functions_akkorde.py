def get_intervals(list,notes,Startton="C"):
    return [notes.get(interval%12) for interval in list]

def get_intervals_additiv(notes,list):
    l2=[]
    for item in list:
        l2.append(item+sum(l2))

    return [notes.get(interval%12) for interval in l2]



notes= {
    0:"C",
    1: "Cis",
    2:"D",
    3:"Dis",
    4:"E",
    5:"F",
    6:"Fis",
    7:"G",
    8:"Gis",
    9:"A",
    10:"Ais",
    11:"H"
}
Prime=  0
Sekunde=2
Terz=   4
Quarte= 5
Quinte= 7
Sexte = 9
Siebte= 11
Oktave= 12
