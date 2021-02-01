from pydub import AudioSegment

# intended to be used as a loop with multiple inputs for t1 & t2

source_filename = ‘recording_id’
t1 = start_time_of_portion_to_beep
t2 = end_time_of_portion_to_beep
out_path = ‘your_directory_here’
out_filename = Source_filename + ‘_beeped’
beep_fname = ‘beep_fname.wav’

beep = AudioSegment.from_wav(Beep_fname)                   # build custom beep
beep = beep[:1] 						                               # millisecond beep
t1 = int(t1) * 1000  # Works in milliseconds
t2 = int(t2) * 1000
Fill_beep = Beep*((t2-t1)*1000)     
origAudio = AudioSegment.from_wav(source_filename + ".wav")
outAudio= origAudio[:t1] + fill_beep + origAudio[t2:]
outAudio.export(out_path + "\\" + out_filename + ".wav",
                      format="wav")  # Exports to a wav file in the current path.
