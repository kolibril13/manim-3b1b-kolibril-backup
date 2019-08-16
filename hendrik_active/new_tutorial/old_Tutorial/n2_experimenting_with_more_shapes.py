from manimlib.imports import *
class Shapes(Scene):
    def construct(self):
        dot1 = Dot()
        dot2 = Dot()
        dot_end = Dot()

        circle1 = Circle( radius = 2, fill_color= GREEN , arc_center = np.array((2., 0, 0.)))
        circle2 = Circle( radius = 2, fill_color= GREEN , arc_center = np.array((-2., 0, 0.)))
        self.add(dot1)
        self.add(dot2)
        # self.wait(1)
        self.play(Transform(dot1,circle1), Transform(dot2,circle2))
        self.play(Rotating(dot1, about_point= np.array((0, 0, 0.)) , run_time=1),
                  Rotating(dot2, about_point=np.array((0, 0, 0.)), run_time=1)
                  )

        self.play(Transform(dot1,dot_end), Transform(dot2,dot_end))
        self.play(ChangeProbability(dot1))
        self.wait(0.3)
if __name__ == "__main__":
    os.system("python3.7 -m manim -pl  n2_experimenting_with_more_shapes.py Shapes --leave_progress_bars ")  # Does not play files




class MoreShapesxx(Scene):
    # A few more simple shapes
    def construct(self):
        circle = Circle(color=PURPLE_A)
        square = Square(fill_color=GOLD_B, fill_opacity=1, color=GOLD_A)
        square.move_to(UP + LEFT)
        circle.surround(square)
        rectangle = Rectangle(height=2, width=3)
        ellipse = Ellipse(width=3, height=1, color=RED)
        ellipse.shift(2 * DOWN + 2 * RIGHT)
        pointer = CurvedArrow(2 * RIGHT, 5 * RIGHT, color=MAROON_C)
        arrow = Arrow(LEFT, UP)
        arrow.next_to(circle, DOWN + LEFT)
        rectangle.next_to(arrow, DOWN + LEFT)
        ring = Annulus(inner_radius=.5, outer_radius=1, color=BLUE)
        ring.next_to(ellipse, RIGHT)
        self.add(pointer)
        self.play(FadeIn(square))
        self.play(Rotating(square), FadeIn(circle))
        self.play(GrowArrow(arrow))
        self.play(GrowFromCenter(rectangle), GrowFromCenter(ellipse), GrowFromCenter(ring))
