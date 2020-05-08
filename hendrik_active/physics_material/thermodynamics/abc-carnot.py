GraphFromData
class PV(GraphScene):
    CONFIG = {

        "x_min": -1,
        "x_max": 10,
        "x_axis_width": 9,
        "x_tick_frequency": 1,
        "x_leftmost_tick": 2,  # Change if different from x_min
        "x_labeled_nums": None,
        "x_axis_label": "$V$",
        "y_min": -1,
        "y_max": 10,
        "y_axis_height": 6,
        "y_tick_frequency": 1,
        "y_bottom_tick": 2,  # Change if different from y_min
        "y_labeled_nums": None,
        "y_axis_label": "$P$",
        "axes_color": GREY,
        "graph_origin": 2.5 * DOWN + 4 * LEFT,
        "exclude_zero_label": True,
        "num_graph_anchor_points": 25,
        "default_graph_colors": [BLUE, GREEN, YELLOW],
        "default_derivative_color": GREEN,
        "default_input_color": YELLOW,
        "default_riemann_start_color": BLUE,
        "default_riemann_end_color": GREEN,
        "area_opacity": 0.8,
        "num_rects": 50,
        "init_dx": 0.5,
        "x_label_decimal": 0,
        "y_label_decimal": 0,
        "y_label_direction": LEFT,
        "x_label_direction": DOWN
    }

    def construct(self):
        self.grafik()

    def grafik(self):

        self.setup_axes()

        def func(V):
            return V

        graph = self.get_graph(func, V_min=2, V_max=7, color=RED)
        kwargs = {
            "x_min": 2,
            "x_max": 7,
            "fill_opacity": 0.75,
            "stroke_width": 0.25,
        }

        input_tracker_p1 = ValueTracker(2)
        input_tracker_p2 = ValueTracker(7)

        def get_x_value(input_tracker):
            return input_tracker.get_value()

        def get_y_value(input_tracker):
            return graph.underlying_function(get_x_value(input_tracker))

        def get_x_point(input_tracker):
            return self.coords_to_point(get_x_value(input_tracker), 0)

        def get_y_point(input_tracker):
            return self.coords_to_point(0, get_y_value(input_tracker))

        def get_graph_point(input_tracker):
            return self.coords_to_point(get_x_value(input_tracker), get_y_value(input_tracker))

        def get_v_line(input_tracker):
            return DashedLine(get_x_point(input_tracker), get_graph_point(input_tracker), stroke_width=2)

        def get_h_line(input_tracker):
            return DashedLine(get_graph_point(input_tracker), get_y_point(input_tracker), stroke_width=2)

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

        # V Ekseni
        x_label_p1 = TexMobject("{ V }_{ 1 }")
        x_label_p2 = TexMobject("{ V }_{ 2 }")

        v_line_p1 = get_v_line(input_tracker_p1)
        v_line_p2 = get_v_line(input_tracker_p2)
        h_line_p1 = get_h_line(input_tracker_p1)
        h_line_p2 = get_h_line(input_tracker_p2)
        graph_dot_p1 = Dot(color=WHITE)
        graph_dot_p2 = Dot(color=WHITE)

        # P Ekseni
        y_label_p1 = TexMobject("{ P }_{ 1 }")
        y_label_p2 = TexMobject("{ P }_{ 2 }")

        # reposition mobjects
        x_label_p1.next_to(v_line_p1, DOWN)
        x_label_p2.next_to(v_line_p2, DOWN)
        y_label_p1.next_to(h_line_p1, LEFT)
        y_label_p2.next_to(h_line_p2, LEFT)
        input_triangle_p1.next_to(v_line_p1, DOWN, buff=0)
        input_triangle_p2.next_to(v_line_p2, DOWN, buff=0)
        output_triangle_p1.next_to(h_line_p1, LEFT, buff=0)
        output_triangle_p2.next_to(h_line_p2, LEFT, buff=0)
        graph_dot_p1.move_to(get_graph_point(input_tracker_p1))
        graph_dot_p2.move_to(get_graph_point(input_tracker_p2))

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
            Write(y_label_p2),
            ShowCreation(v_line_p2),
            GrowFromCenter(graph_dot_p2),
            ShowCreation(h_line_p2),
            DrawBorderThenFill(output_triangle_p2),
            run_time=3
        )

        flat_rectangles = self.get_riemann_rectangles(
            self.get_graph(lambda x: 0),
            dx=self.init_dx,
            start_color=invert_color(PURPLE),
            end_color=invert_color(ORANGE),
            **kwargs
        )
        riemann_rectangles_list = self.get_riemann_rectangles_list(
            graph,
            6,
            max_dx=self.init_dx,
            power_base=2,
            start_color=DARK_BLUE,
            end_color=YELLOW,
            **kwargs
        )
        graph.scale(0.45)

        self.play(Write(graph), run_time=4)
        # Show Riemann rectangles
        self.play(ReplacementTransform(flat_rectangles, riemann_rectangles_list[0]))
        self.wait()
        for r in range(1, len(riemann_rectangles_list)):
            self.transform_between_riemann_rects(
                riemann_rectangles_list[r - 1],
                riemann_rectangles_list[r],
                replace_mobject_with_target_in_scene=True,
            )
        self.wait(18)


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p  -l -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"PV"
    os.system(command_A + command_B)