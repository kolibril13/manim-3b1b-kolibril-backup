from manimlib.imports import *

class Ball(Circle):
    CONFIG = {
        "radius": 0.4,
        "fill_color": BLUE,
        "fill_opacity": 1,
        "color": BLUE
    }

    def __init__(self, ** kwargs):
        Circle.__init__(self, ** kwargs)
        self.velocity = np.array((10, 5, 0))

    def get_top(self):
        return self.get_center()[1] + self.radius

    def get_bottom(self):
        return self.get_center()[1] - self.radius

    def get_right_edge(self):
        return self.get_center()[0] + self.radius

    def get_left_edge(self):
        return self.get_center()[0] - self.radius

class Box(Rectangle):
    CONFIG = {
        "height": 6,
        "width": FRAME_WIDTH - 2,
        "color": GREEN_C
    }

    def __init__(self, ** kwargs):
        Rectangle.__init__(self, ** kwargs)  # Edges
        self.top = 0.5 * self.height
        self.bottom = -0.5 * self.height
        self.right_edge = 0.5 * self.width
        self.left_edge = -0.5 * self.width

class BouncingBall(Scene):
    def construct(self):
        box = Box()
        ball = Ball()
        self.play(FadeIn(box))
        self.play(FadeIn(ball))

        def update_ball(ball,dt):
            ball.acceleration = np.array((0, -2, 0))
            ball.velocity = ball.velocity + ball.acceleration * dt
            ball.shift(ball.velocity * dt)  # Bounce off ground and roof
            if ball.get_bottom() <= box.bottom or \
                    ball.get_top() >= box.top:
                ball.velocity[1] = -ball.velocity[1]
            # Bounce off walls
            if ball.get_left_edge() <= box.left_edge or \
                    ball.get_right_edge() >= box.right_edge:
                ball.velocity[0] = -ball.velocity[0]

        ball.add_updater(update_ball)
        self.add(ball)

        self.wait(25)
if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim  -l -s -p -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"BouncingBall"
    os.system(command_A + command_B)