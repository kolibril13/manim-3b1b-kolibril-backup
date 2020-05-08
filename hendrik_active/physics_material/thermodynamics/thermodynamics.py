from manimlib.imports import *

class Graph(GraphFromData, ZoomedScene):
    CONFIG = {
        "y_max": 25,
        "y_axis_label": "$T$",
        "x_axis_label": "$V$",
        "y_tick_frequency": 110,
        "zoom_factor": 0.3,
        "zoomed_display_height": 1,
        "zoomed_display_width": 6,
        "image_frame_stroke_width": 20,
        "zoomed_camera_config": {
            "default_frame_stroke_width": 3,
        },
    }

    def setup(self):
        MovingCameraScene.setup(self)
        ZoomedScene.setup(self)

    def construct(self):
        self.setup_axes()

        # 1. Grafik
        x = [2, 3, 4, 5, 6, 7, 8]
        y = [6, 12, 20, 25, 22, 10, 5]
        coords = [[px, py] for px, py in zip(x, y)]
        points = self.get_points_from_coords(coords)

        #graph = SmoothGraphFromSetPoints(points, color=RED)
        dots = self.get_dots_from_coords(coords, 0.001)
        dots.set_color(BLACK)

        # 2. Grafik
        x1 = [1, 2, 3, 4, 5, 6, 6.5, 6.8, 7.8, 8.8]
        y1 = [4, 8, 12, 12, 12, 12, 12, 12, 16, 20]
        coords2 = [[px, py] for px, py in zip(x1, y1)]
        points2 = self.get_points_from_coords(coords2)

        #graph2 = DiscreteGraphFromSetPoints(points2, color=GREEN)
        dots2 = self.get_dots_from_coords(coords2, 0.001)
        dots2.set_color(BLACK)
        graphs = Group(graph, graph2)
        self.add(dots, dots2)
        self.play(ShowCreation(graphs, run_time=5.5))
        self.wait(3)

        ###########

        input_tracker_p1 = ValueTracker(3)
        input_tracker_p2 = ValueTracker(6.8)

        #
        input_triangle_p1 = RegularPolygon(n=3, start_angle=TAU / 4)
        output_triangle_p1 = RegularPolygon(n=3, start_angle=0)
        for triangle in input_triangle_p1, output_triangle_p1:
            triangle.set_fill(WHITE, 1)
            triangle.set_stroke(width=0)
            triangle.scale(0.1)

        #
        input_triangle_p2 = RegularPolygon(n=3, start_angle=TAU / 4)
        output_triangle_p2 = RegularPolygon(n=3, start_angle=0)
        for triangle in input_triangle_p2, output_triangle_p2:
            triangle.set_fill(WHITE, 1)
            triangle.set_stroke(width=0)
            triangle.scale(0.1)

        output_triangle_p3 = output_triangle_p2.copy()

        def get_x_value(input_tracker):
            return input_tracker.get_value()

        def get_y_value(input_tracker):
            return input_tracker.get_value()

        def get_x_point(input_tracker):
            return self.coords_to_point(get_x_value(input_tracker), 0)

        def get_y_point(input_tracker):
            return self.coords_to_point(0, get_y_value(input_tracker) * 1.7647)

        def get_graph_point(input_tracker):
            return self.coords_to_point(get_x_value(input_tracker), get_y_value(input_tracker) * 1.7647)

        def get_v_line(input_tracker):
            return DashedLine(get_x_point(input_tracker), get_graph_point(input_tracker), stroke_width=2)

        def get_h_line(input_tracker):
            return DashedLine(get_graph_point(input_tracker), get_y_point(input_tracker), stroke_width=2)

        ######################################

        def get_x_value_2(input_tracker):
            return input_tracker.get_value()

        def get_y_value_2(input_tracker):
            return input_tracker.get_value()

        def get_x_point_2(input_tracker):
            return self.coords_to_point(get_x_value_2(input_tracker), 0)

        def get_y_point_2(input_tracker):
            return self.coords_to_point(0, get_y_value_2(input_tracker) * 4)

        def get_graph_point_2(input_tracker):
            return self.coords_to_point(get_x_value_2(input_tracker), get_y_value_2(input_tracker) * 4)

        def get_v_line_2(input_tracker):
            return DashedLine(get_x_point_2(input_tracker), get_graph_point_2(input_tracker), stroke_width=2)

        def get_h_line_2(input_tracker):
            return DashedLine(get_graph_point_2(input_tracker), get_y_point_2(input_tracker), stroke_width=2)

        #################################

        # V Ekseni
        x_label_p1 = TexMobject("{ V }_{ f }").scale(0.5).set_color(YELLOW)
        x_label_p2 = TexMobject("{ V }_{ g }").scale(0.5).set_color(YELLOW)

        v_line_p1 = get_v_line_2(input_tracker_p1).set_color(BLUE)
        v_line_p2 = get_v_line(input_tracker_p2).set_color(BLUE)
        h_line_p1 = get_h_line_2(input_tracker_p1).set_color(BLUE)
        h_line_p2 = get_h_line(input_tracker_p2).set_color(BLUE)
        graph_dot_p1 = Dot(color=PURPLE_A)
        graph_dot_p2 = Dot(color=PURPLE_A)

        # T Ekseni
        y_label_p1 = TexMobject("{ T }_{ sat }").scale(0.5).set_color(YELLOW)
        y_label_psat = TexMobject("{ P }_{ sat }").scale(0.5).set_color(YELLOW)

        # reposition mobjects
        x_label_p1.next_to(v_line_p1, DOWN)
        x_label_p2.next_to(v_line_p2, DOWN)
        y_label_p1.next_to(h_line_p1, LEFT)
        input_triangle_p1.next_to(v_line_p1, DOWN, buff=0)
        input_triangle_p2.next_to(v_line_p2, DOWN, buff=0)
        output_triangle_p1.next_to(h_line_p1, LEFT, buff=0)
        output_triangle_p2.next_to(h_line_p2, LEFT, buff=0)
        output_triangle_p3.next_to(output_triangle_p2, UP, buff=2)
        graph_dot_p1.move_to(get_graph_point_2(input_tracker_p1))
        graph_dot_p2.move_to(get_graph_point(input_tracker_p2))

        g1 = TextMobject("Sıkıştırılmış Sıvı Bölgesi").scale(0.45).move_to(LEFT * 2.7 + UP * 0.5)
        g2 = TextMobject("Doymuş Sıvı-Buhar Bölgesi").scale(0.45).move_to(DOWN * 1.5)
        g3 = TextMobject("Kızgın Buhar Bölgesi").scale(0.45).move_to(RIGHT * 3 + UP * 0.2)
        g4 = TextMobject("Doymuş Buhar").scale(0.6).move_to(RIGHT * 2.6 + UP * 3.5).set_color(PURPLE_A)
        g5 = TextMobject("Doymuş Sıvı").scale(0.6).move_to(LEFT * 3 + DOWN * 3.5).set_color(PURPLE_A)

        arrow1 = Arrow(graph_dot_p1.get_bottom(), g5.get_top(), buff=0.01).set_color(GREY_BROWN).scale(0.7)
        arrow2 = Arrow(graph_dot_p2.get_top(), g4.get_bottom(), buff=0.01).set_color(GREY_BROWN).scale(0.7)

        self.add_foreground_mobject(graph_dot_p1)
        self.add_foreground_mobject(graph_dot_p2)
        self.play(
            DrawBorderThenFill(input_triangle_p1),
            Write(x_label_p1),
            Write(y_label_p1),
            ShowCreation(v_line_p1),
            GrowFromCenter(graph_dot_p1),
            ShowCreation(h_line_p1),
            DrawBorderThenFill(output_triangle_p1),
            DrawBorderThenFill(input_triangle_p2),
            Write(x_label_p2),
            ShowCreation(v_line_p2),
            GrowFromCenter(graph_dot_p2),
            ShowCreation(h_line_p2),
            run_time=3
        )

        self.wait(15)

        self.play(
            Write(g1),
            Write(g2),
            Write(g3)
        )
        self.wait(10)
        self.play(
            ReplacementTransform(graph_dot_p1.copy(), g5, run_time=2),
            GrowArrow(arrow1, run_time=2)
        )
        self.wait(10)
        self.play(
            ReplacementTransform(graph_dot_p2.copy(), g4, run_time=2),
            GrowArrow(arrow2, run_time=2)
        )
        self.wait(10)

        self.play(ShowCreationThenFadeAround(x_label_p1),
                  ShowCreationThenFadeAround(g5))
        self.wait(10)
        self.play(ShowCreationThenFadeAround(x_label_p2),
                  ShowCreationThenFadeAround(g4))
        self.wait(10)

        self.play(
            FadeOutAndShift(g4, UP),
            FadeOutAndShift(g5, DOWN),
            FadeOutAndShift(arrow1, LEFT),
            FadeOutAndShift(arrow2, RIGHT)

        )