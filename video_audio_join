import moviepy.editor as mpe

recordings = ['root_call_id']

for recording in recordings:
    vid = f'{recording}_video.avi'
    aud = f'{recording}_beeped.wav'
    my_clip = mpe.VideoFileClip(vid)
    audio_background = mpe.AudioFileClip(aud)
    final_clip = my_clip.set_audio(audio_background)
    final_clip.write_videofile(f'{recording}_final.mp4',fps=15)
