import librosa

#скрипта улаз/излаз, говори о фајлу који се учитава и који тип фајла може да се учита

class IO:
    FILE_PATH = ''  #пут до фајла
    SAMPLE_RATE = 44100

    def __init__(self,file_path):
        self.FILE_PATH = file_path

    def load(self):
        if ".wav" in self.FILE_PATH:
            import wave
            #кад импортујемо wave, тиме се омогућује рад са WAV датотекама
            #WAV датотеке не подржавају компресију/декомпресију, али подржавају моно/стерео звуке(један извор/више извора звука)
            
            #WAV (waveform audio file) датотеке служе за чување аудио тока битова на рачунарима
            with wave.open(self.FILE_PATH,'rb') as wav:
                self.SAMPLE_RATE = wav.getframerate()
        try:
            y, sr = librosa.load(self.FILE_PATH,sr=self.SAMPLE_RATE)
            #librosa.load - учитава аудио фајл као временску секвенцу с помичним зарезом
            return (y, sr)
        except:
            print("Greška pri učitavanju datoteke: %s"%self.FILE_PATH)

    def dump(self,file_name, n_arr, sr):
        try:
            librosa.output.write_wav(file_name,n_arr,sr)
            #као излаз добија се временски низ као wav датотека
        except:
            print("Greška pri kopiranju datoteke: %s"%file_name)

