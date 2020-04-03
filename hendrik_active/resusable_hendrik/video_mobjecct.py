from manimlib.imports import *

class VideoLoader():
    def __init__(self):
        self.all_frames=np.random.random((30,100,100))*250 # 30 images with shape 100x100

    def get_frames(self):
        return self.all_frames

class VideoScene(Scene):
    def construct(self):
        videoframes=VideoLoader()
        all_frames=videoframes.get_frames()
        dot = Dot()
        video=ImageMobject(np.zeros((100,100)))

        def update_frame(video):
            frame_pos=np.int(dot.get_x()*len(all_frames-1))
            print(frame_pos)
            frame = all_frames[frame_pos, :, :]
            frame=np.uint8(frame)
            video.become(ImageMobject(frame))

        video.add_updater(update_frame)
        dot.next_to(video,DOWN)
        self.add(video, dot)
        self.play(dot.shift, RIGHT, rate_func=linear)


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p   -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"VideoScene"
    os.system(command_A + command_B)