import os
path = os.getcwd()
files = []
# r=root, d=directories, f = files\n",
for r, d, f in os.walk(path):\n",
    for file in f:\n",
        if '.mp4' in file:\n",
            files.append(file)\n",
