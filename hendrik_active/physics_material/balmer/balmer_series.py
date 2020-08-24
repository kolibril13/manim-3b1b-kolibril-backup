from manim import *

class Balmer(Scene):



    def construct(self):
        normal_red= "#FF1900"
        def balmer(n):
            Z=1
            a_0=1
            scale_fac= 0.13
            return scale_fac* n**2/Z*a_0
        trans_colmap = {
                        "t32" : "#ff0000",
                        "t42" :"#00efff",
                        "t52" :"#2800ff",
                        "t62" :"#7e00db",
                        "t72" :"#8100a9"
                        }
        trans_wavelengths = {
            "t32" : r" \text{\"Ubergang 3} \rightarrow \text{2}: \lambda = 656\,\text{nm}" ,
            "t42" : r" \text{\"Ubergang 4} \rightarrow \text{2}: \lambda = 486\,\text{nm}" ,
            "t52" : r" \text{\"Ubergang 5} \rightarrow \text{2}: \lambda = 434\,\text{nm}" ,
            "t62" : r" \text{\"Ubergang 6} \rightarrow \text{2}: \lambda = 410\,\text{nm}" ,
            "t72" : r" \text{\"Ubergang 7} \rightarrow \text{2}: \lambda = 397\,\text{nm}" ,
        }

        trans_names = {
            "t32" : r"\alpha",
            "t42" : r"\beta",
            "t52" : r"\gamma",
            "t62" : r"\delta",
            "t72" : r"\epsilon"
        }
        levels= {"n1":balmer(1),
                "n2":balmer(2),
                "n3":balmer(3),
                "n4":balmer(4),
                "n5":balmer(5),
                "n6":balmer(6),
                "n7":balmer(7),
            }
        pos0=2.5
        offset=0.5
        core = Dot().set_color(normal_red).scale(1).move_to(BOTTOM + 2 * SMALL_BUFF * UP)
        tplus = TextMobject(r"\textbf{+}").move_to(core.get_center()).scale(0.2).set_color(BLACK).set_stroke(width=1.5)
        core = VGroup(core, tplus)
        arcs = [Arc(0.9*np.pi,- 2*np.pi, radius = lev, arc_center = core.get_center())  for lev in levels.values()]
        annot = [TexMobject(f"n={n}").shift(UP*n).scale(0.31) for n in range(1,1+ len(levels))]
        all_arcs = VGroup(*arcs).set_color(BLUE)
        all_annot = VGroup(*annot).set_color(interpolate_color(BLUE, BLACK, 0.6))
        [x.move_to(core.get_center()+y*UP+UP*SMALL_BUFF) for x,y in zip(all_annot.submobjects, levels.values())]


        self.play(FadeIn(core))
        self.play(FadeIn(all_arcs, core.get_center()),lag_ratio= 0.9 , run_time=1)
        self.play(FadeIn(all_annot),lag_ratio= 0.9 , run_time=2)
        self.wait(0.5)
        
        ## setup ready
        
        #first photon
        position_shift = pos0
        trans_id = "t32"
        levup = "n3"
        levdown= "n2"
        el1 = Dot().set_color(YELLOW).scale(2)
        el1.move_to(core.get_center()+UP*levels[levup])
        el1.rotate(position_shift*PI/10 ,about_point= core.get_center())
        t=TextMobject("-").set_color(BLACK).move_to(el1.get_center())
        elektron1 = VGroup(el1,t)

        el2 = Dot().set_color(YELLOW).scale(2)
        el2.move_to(core.get_center()+UP*levels[levdown])
        el2.rotate(position_shift*PI/10 ,about_point= core.get_center())
        t=TextMobject("-").set_color(BLACK).move_to(el2.get_center())
        elektron2 = VGroup(el2,t)
        veci = Line(el1,el2).get_vector()
        veci=veci/get_norm(veci)
        print(veci)
        CanvasNameObject= TexMobject(trans_names[trans_id]).scale(1.3).move_to(el1.get_center()-veci*0.3).set_color(trans_colmap[trans_id])
        path = VMobject().set_color(trans_colmap[trans_id])
        path.set_points_as_corners([el1.get_center(),el1.get_center()+UP*0.01])
        def update_path(path):
            previus_path = path.copy()
            previus_path.add_points_as_corners([el1.get_center()])
            path.become(previus_path)

        path.add_updater(update_path)

        pathSolid = Line(el1,el2).set_color(trans_colmap[trans_id])
        new_intepolated_color= interpolate_color(WHITE,trans_colmap[trans_id], 0.4)
        dotphoton= Dot().scale(4).set_color(new_intepolated_color)
        arc= Arc(-TAU/2, 3*TAU/2, radius=dotphoton.get_width()/2 , arc_center= dotphoton.get_center())
        arc.set_color(trans_colmap[trans_id])
        x = np.linspace(-PI,PI,100)
        y = 2*np.sin(2*x)
        sin_curve = VMobject()
        sin_curve.set_points_smoothly([[xi,yi,0]
                                       for xi, yi in zip(x,y) ] )
        sin_curve.scale(0.06).set_color(trans_colmap[trans_id])
        photon1 = VGroup(dotphoton,sin_curve,arc).move_to(Line(el1,el2).get_center()).shift(2*RIGHT)

        i1 = TexMobject(trans_wavelengths[trans_id], color= BLACK).scale(0.6)
        i1.to_corner(DR,buff=SMALL_BUFF).shift(1.5*LEFT)
        i1.background_rectangle = BackgroundRectangle(i1, color=WHITE, opacity= 0.2)

        self.add(path)
        self.play(FadeIn(elektron1))
        self.play(FadeIn(CanvasNameObject),run_time=0.4)
        self.play( elektron1.move_to,elektron2 , run_time= 0.5, rate_func= linear) #####
        self.add(i1.background_rectangle,i1)
        self.play(Transform(pathSolid, sin_curve), rate_func= linear, run_time=1 )

        self.add(photon1)
        self.play(VGroup(pathSolid,photon1).shift ,3*RIGHT, rate_func= linear, run_time= 1.5)
        self.play(FadeOutAndShift(VGroup(pathSolid,photon1) ,RIGHT, rate_func= linear, run_time= 0.5))
        self.play(FadeOut(elektron1),run_time=0.5)
        self.remove(i1.background_rectangle,i1)
        self.wait(0.5)
        path.remove_updater(update_path)

    #second photon
        position_shift = pos0-offset
        trans_id = "t42"
        levup = "n4"
        levdown= "n2"
        el1 = Dot().set_color(YELLOW).scale(2)
        el1.move_to(core.get_center()+UP*levels[levup])
        el1.rotate(position_shift*PI/10 ,about_point= core.get_center())
        t=TextMobject("-").set_color(BLACK).move_to(el1.get_center())
        elektron1 = VGroup(el1,t)

        el2 = Dot().set_color(YELLOW).scale(2)
        el2.move_to(core.get_center()+UP*levels[levdown])
        el2.rotate(position_shift*PI/10 ,about_point= core.get_center())
        t=TextMobject("-").set_color(BLACK).move_to(el2.get_center())
        elektron2 = VGroup(el2,t)
        veci = Line(el1,el2).get_vector()
        veci=veci/get_norm(veci)
        print(veci)
        CanvasNameObject= TexMobject(trans_names[trans_id]).scale(1.3).move_to(el1.get_center()-veci*0.3).set_color(trans_colmap[trans_id])
        path = VMobject().set_color(trans_colmap[trans_id])
        path.set_points_as_corners([el1.get_center(),el1.get_center()+UP*0.01])
        def update_path(path):
            previus_path = path.copy()
            previus_path.add_points_as_corners([el1.get_center()])
            path.become(previus_path)

        path.add_updater(update_path)

        pathSolid = Line(el1,el2).set_color(trans_colmap[trans_id])
        new_intepolated_color= interpolate_color(WHITE,trans_colmap[trans_id], 0.4)
        dotphoton= Dot().scale(4).set_color(new_intepolated_color)
        arc= Arc(-TAU/2, 3*TAU/2, radius=dotphoton.get_width()/2 , arc_center= dotphoton.get_center())
        arc.set_color(trans_colmap[trans_id])
        x = np.linspace(-PI,PI,100)
        y = 2*np.sin(2*x)
        sin_curve = VMobject()
        sin_curve.set_points_smoothly([[xi,yi,0]
                                       for xi, yi in zip(x,y) ] )
        sin_curve.scale(0.06).set_color(trans_colmap[trans_id])
        photon1 = VGroup(dotphoton,sin_curve,arc).move_to(Line(el1,el2).get_center()).shift(2*RIGHT)

        i1 = TexMobject(trans_wavelengths[trans_id], color= BLACK).scale(0.6)
        i1.to_corner(DR,buff=SMALL_BUFF).shift(1.5*LEFT)
        i1.background_rectangle = BackgroundRectangle(i1, color=WHITE, opacity= 0.2)

        self.add(path)
        self.play(FadeIn(elektron1))
        self.play(FadeIn(CanvasNameObject),run_time=0.4)
        self.play( elektron1.move_to,elektron2 , run_time= 0.5, rate_func= linear) #####
        self.add(i1.background_rectangle,i1)
        self.play(Transform(pathSolid, sin_curve), rate_func= linear, run_time=1 )

        self.add(photon1)
        self.play(VGroup(pathSolid,photon1).shift ,3*RIGHT, rate_func= linear, run_time= 1.5)
        self.play(FadeOutAndShift(VGroup(pathSolid,photon1) ,RIGHT, rate_func= linear, run_time= 0.5))
        self.play(FadeOut(elektron1),run_time=0.5)
        self.remove(i1.background_rectangle,i1)
        self.wait(0.5)
        path.remove_updater(update_path)

        #third
        position_shift = pos0-2*offset
        trans_id = "t52"
        levup = "n5"
        levdown= "n2"
        el1 = Dot().set_color(YELLOW).scale(2)
        el1.move_to(core.get_center()+UP*levels[levup])
        el1.rotate(position_shift*PI/10 ,about_point= core.get_center())
        t=TextMobject("-").set_color(BLACK).move_to(el1.get_center())
        elektron1 = VGroup(el1,t)

        el2 = Dot().set_color(YELLOW).scale(2)
        el2.move_to(core.get_center()+UP*levels[levdown])
        el2.rotate(position_shift*PI/10 ,about_point= core.get_center())
        t=TextMobject("-").set_color(BLACK).move_to(el2.get_center())
        elektron2 = VGroup(el2,t)
        veci = Line(el1,el2).get_vector()
        veci=veci/get_norm(veci)
        print(veci)
        CanvasNameObject= TexMobject(trans_names[trans_id]).scale(1.3).move_to(el1.get_center()-veci*0.3).set_color(trans_colmap[trans_id])
        path = VMobject().set_color(trans_colmap[trans_id])
        path.set_points_as_corners([el1.get_center(),el1.get_center()+UP*0.01])
        def update_path(path):
            previus_path = path.copy()
            previus_path.add_points_as_corners([el1.get_center()])
            path.become(previus_path)

        path.add_updater(update_path)

        pathSolid = Line(el1,el2).set_color(trans_colmap[trans_id])
        new_intepolated_color= interpolate_color(WHITE,trans_colmap[trans_id], 0.4)
        dotphoton= Dot().scale(4).set_color(new_intepolated_color)
        arc= Arc(-TAU/2, 3*TAU/2, radius=dotphoton.get_width()/2 , arc_center= dotphoton.get_center())
        arc.set_color(trans_colmap[trans_id])
        x = np.linspace(-PI,PI,100)
        y = 2*np.sin(2*x)
        sin_curve = VMobject()
        sin_curve.set_points_smoothly([[xi,yi,0]
                                       for xi, yi in zip(x,y) ] )
        sin_curve.scale(0.06).set_color(trans_colmap[trans_id])
        photon1 = VGroup(dotphoton,sin_curve,arc).move_to(Line(el1,el2).get_center()).shift(2*RIGHT)

        i1 = TexMobject(trans_wavelengths[trans_id], color= BLACK).scale(0.6)
        i1.to_corner(DR,buff=SMALL_BUFF).shift(1.5*LEFT)
        i1.background_rectangle = BackgroundRectangle(i1, color=WHITE, opacity= 0.2)

        self.add(path)
        self.play(FadeIn(elektron1))
        self.play(FadeIn(CanvasNameObject),run_time=0.4)
        self.play( elektron1.move_to,elektron2 , run_time= 0.5, rate_func= linear) #####
        self.add(i1.background_rectangle,i1)
        self.play(Transform(pathSolid, sin_curve), rate_func= linear, run_time=1 )

        self.add(photon1)
        self.play(VGroup(pathSolid,photon1).shift ,3*RIGHT, rate_func= linear, run_time= 1.5)
        self.play(FadeOutAndShift(VGroup(pathSolid,photon1) ,RIGHT, rate_func= linear, run_time= 0.5))
        self.play(FadeOut(elektron1),run_time=0.5)
        self.remove(i1.background_rectangle,i1)
        self.wait(0.5)
        path.remove_updater(update_path)

        #four
        position_shift = pos0-3*offset
        trans_id = "t62"
        levup = "n6"
        levdown= "n2"
        el1 = Dot().set_color(YELLOW).scale(2)
        el1.move_to(core.get_center()+UP*levels[levup])
        el1.rotate(position_shift*PI/10 ,about_point= core.get_center())
        t=TextMobject("-").set_color(BLACK).move_to(el1.get_center())
        elektron1 = VGroup(el1,t)

        el2 = Dot().set_color(YELLOW).scale(2)
        el2.move_to(core.get_center()+UP*levels[levdown])
        el2.rotate(position_shift*PI/10 ,about_point= core.get_center())
        t=TextMobject("-").set_color(BLACK).move_to(el2.get_center())
        elektron2 = VGroup(el2,t)
        veci = Line(el1,el2).get_vector()
        veci=veci/get_norm(veci)
        print(veci)
        CanvasNameObject= TexMobject(trans_names[trans_id]).scale(1.3).move_to(el1.get_center()-veci*0.3).set_color(trans_colmap[trans_id])
        path = VMobject().set_color(trans_colmap[trans_id])
        path.set_points_as_corners([el1.get_center(),el1.get_center()+UP*0.01])
        def update_path(path):
            previus_path = path.copy()
            previus_path.add_points_as_corners([el1.get_center()])
            path.become(previus_path)

        path.add_updater(update_path)

        pathSolid = Line(el1,el2).set_color(trans_colmap[trans_id])
        new_intepolated_color= interpolate_color(WHITE,trans_colmap[trans_id], 0.4)
        dotphoton= Dot().scale(4).set_color(new_intepolated_color)
        arc= Arc(-TAU/2, 3*TAU/2, radius=dotphoton.get_width()/2 , arc_center= dotphoton.get_center())
        arc.set_color(trans_colmap[trans_id])
        x = np.linspace(-PI,PI,100)
        y = 2*np.sin(2*x)
        sin_curve = VMobject()
        sin_curve.set_points_smoothly([[xi,yi,0]
                                       for xi, yi in zip(x,y) ] )
        sin_curve.scale(0.06).set_color(trans_colmap[trans_id])
        photon1 = VGroup(dotphoton,sin_curve,arc).move_to(Line(el1,el2).get_center()).shift(2*RIGHT)

        i1 = TexMobject(trans_wavelengths[trans_id], color= BLACK).scale(0.6)
        i1.to_corner(DR,buff=SMALL_BUFF).shift(1.5*LEFT)
        i1.background_rectangle = BackgroundRectangle(i1, color=WHITE, opacity= 0.2)

        self.add(path)
        self.play(FadeIn(elektron1))
        self.play(FadeIn(CanvasNameObject),run_time=0.4)
        self.play( elektron1.move_to,elektron2 , run_time= 0.5, rate_func= linear) #####
        self.add(i1.background_rectangle,i1)
        self.play(Transform(pathSolid, sin_curve), rate_func= linear, run_time=1 )

        self.add(photon1)
        self.play(VGroup(pathSolid,photon1).shift ,3*RIGHT, rate_func= linear, run_time= 1.5)
        self.play(FadeOutAndShift(VGroup(pathSolid,photon1) ,RIGHT, rate_func= linear, run_time= 0.5))
        self.play(FadeOut(elektron1),run_time=0.5)
        self.remove(i1.background_rectangle,i1)
        self.wait(0.5)
        path.remove_updater(update_path)
        #five
        position_shift = pos0-4*offset
        trans_id = "t72"
        levup = "n7"
        levdown= "n2"
        el1 = Dot().set_color(YELLOW).scale(2)
        el1.move_to(core.get_center()+UP*levels[levup])
        el1.rotate(position_shift*PI/10 ,about_point= core.get_center())
        t=TextMobject("-").set_color(BLACK).move_to(el1.get_center())
        elektron1 = VGroup(el1,t)

        el2 = Dot().set_color(YELLOW).scale(2)
        el2.move_to(core.get_center()+UP*levels[levdown])
        el2.rotate(position_shift*PI/10 ,about_point= core.get_center())
        t=TextMobject("-").set_color(BLACK).move_to(el2.get_center())
        elektron2 = VGroup(el2,t)
        veci = Line(el1,el2).get_vector()
        veci=veci/get_norm(veci)
        print(veci)
        CanvasNameObject= TexMobject(trans_names[trans_id]).scale(1.3).move_to(el1.get_center()-veci*0.3).set_color(trans_colmap[trans_id])
        path = VMobject().set_color(trans_colmap[trans_id])
        path.set_points_as_corners([el1.get_center(),el1.get_center()+UP*0.01])
        def update_path(path):
            previus_path = path.copy()
            previus_path.add_points_as_corners([el1.get_center()])
            path.become(previus_path)

        path.add_updater(update_path)

        pathSolid = Line(el1,el2).set_color(trans_colmap[trans_id])
        new_intepolated_color= interpolate_color(WHITE,trans_colmap[trans_id], 0.4)
        dotphoton= Dot().scale(4).set_color(new_intepolated_color)
        arc= Arc(-TAU/2, 3*TAU/2, radius=dotphoton.get_width()/2 , arc_center= dotphoton.get_center())
        arc.set_color(trans_colmap[trans_id])
        x = np.linspace(-PI,PI,100)
        y = 2*np.sin(2*x)
        sin_curve = VMobject()
        sin_curve.set_points_smoothly([[xi,yi,0]
                                       for xi, yi in zip(x,y) ] )
        sin_curve.scale(0.06).set_color(trans_colmap[trans_id])
        photon1 = VGroup(dotphoton,sin_curve,arc).move_to(Line(el1,el2).get_center()).shift(2*RIGHT)

        i1 = TexMobject(trans_wavelengths[trans_id], color= BLACK).scale(0.6)
        i1.to_corner(DR,buff=SMALL_BUFF).shift(1.5*LEFT)
        i1.background_rectangle = BackgroundRectangle(i1, color=WHITE, opacity= 0.2)

        self.add(path)
        self.play(FadeIn(elektron1))
        self.play(FadeIn(CanvasNameObject),run_time=0.4)
        self.play( elektron1.move_to,elektron2 , run_time= 0.5, rate_func= linear) #####
        self.add(i1.background_rectangle,i1)
        self.play(Transform(pathSolid, sin_curve), rate_func= linear, run_time=1 )

        self.add(photon1)
        self.play(VGroup(pathSolid,photon1).shift ,3*RIGHT, rate_func= linear, run_time= 1.5)
        self.play(FadeOutAndShift(VGroup(pathSolid,photon1) ,RIGHT, rate_func= linear, run_time= 0.5))
        self.play(FadeOut(elektron1),run_time=0.5)
        self.remove(i1.background_rectangle,i1)
        self.wait(0.5)
        path.remove_updater(update_path)


    
if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p -c WHITE --video_dir ~/Downloads/  "
    command_B = module_name +" " +"Balmer"
    os.system(command_A + command_B)