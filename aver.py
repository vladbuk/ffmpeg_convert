import os
import sys
import subprocess

def convert_video(video_input, video_output):
    cmds = ['ffmpeg', '-i', video_input, '-vf', 'scale=640:360, setdar=dar=16/9', video_output]
    print(' '.join(cmds))
    subprocess.run(cmds)
    # subprocess.Popen(cmds)
    # p = subprocess.Popen(cmds)
    # p.terminate()

directory = os.path.dirname(os.path.realpath('IN'))

for subdir, dirs, files in os.walk(directory):
    for filename in files:
        if filename.find('.mpg') > 0:
            subdirectoryPath = os.path.relpath(subdir, directory)
            filePath = os.path.join(subdirectoryPath, filename)
            newFilePath = filePath.replace(".mpg",".mp4")
            
            outdir = os.path.join('OUT', os.path.basename(subdirectoryPath))
            
            if not os.path.exists(outdir):
                os.makedirs(outdir)
            
            outFileName = os.path.join(outdir, os.path.basename(newFilePath))
    
            print(outFileName)

            convert_video(filePath, outFileName)


