import os
from pathlib import Path
file_name = "video"
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
