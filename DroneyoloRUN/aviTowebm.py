import moviepy.editor as mp
def avi2webm(s):
    clip = mp.VideoFileClip(s)
    clip.write_videofile("static/output.webm")