from manimlib.imports import *
from PIL import Image
from pathlib import Path

class VideoMobject:
    def __init__(self, folder_name: str):
        self.frames= self.init_frames(folder_name)
        self.current_frame_num = 0
        self.image_canvas = self.get_image(self.current_frame_num)
        self.frames_length= len(self.frames)

    def get_image(self,frame_num):
        image_path = self.frames[frame_num]
        image = Image.open(str(image_path))
        return ImageMobject(np.array(image)).scale(3)

    def init_frames(self,name):
        file_name = name
        path =  Path.home() / 'Downloads' / file_name
        if not path.is_dir():
            print ("File not exist")
            path.mkdir(parents=True, exist_ok=True)
            print( path )
            # first one is the Downloads/video.mp4, second one is Downloads/video/video_001.png
            command= f"ffmpeg -i '{path}.mp4'  {path/ file_name}_%03d.png"
            os.system(command)
        else:
            print ("File exist")

        frames = []
        path =  Path.home() / 'Downloads' / file_name
        for filename in sorted(path.glob('*.png')):
            frames.append(filename)

        if (len(frames)==0):
            raise Exception("""Video not found! Please save the video in the Download folder and call VideoMobject("videoname") without exention""")

        return frames

    def to_fist_frame(self):
        self.image_canvas.become(self.get_image(0))
    def to_last_frame(self):
        self.image_canvas.become(self.get_image(self.frames_length - 1))

    def play(self):
        self.image_canvas.add_updater(self.frame_updater)

    def pause(self):
        self.image_canvas.remove_updater(self.frame_updater)

    def frame_updater(self, mob, dt):
        self.current_frame_num += 1
        if (self.frames_length > self.current_frame_num):
            self.image_canvas.become(self.get_image(self.current_frame_num))


class VideoScene(Scene):
    def construct(self):
        video_canvas = VideoMobject("FriedelCraftsAlkylation") ## for the file vibrown_motion.mp4
        self.add(video_canvas.image_canvas)
        video_canvas.play()
        self.play(video_canvas.image_canvas.move_to, RIGHT)
        self.wait(1)
        video_canvas.pause()
        self.wait(1)
        video_canvas.play()
        self.wait(1)


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim  -p -l  -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name + " " + "VideoScene"
    os.system(command_A + command_B)
