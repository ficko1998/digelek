import librosa
import izracunavanje
import numpy as np

class Autotune: #osnovna klasa, ovde definišemo sve parametre
    def __init__(self, y, sr, scale):
        self.INPUT_WAVE = y #ulazni signal/talas
        self.INPUT_SR = sr #sampling rate - nivo uzorkovanja, da tako kažemo
        self.SCALE = scale #skaliranje
        self._note = izracunavanje.Izracunavanje(scale)
        
        self.NOTES = self._note.getScale() #getScale() vraća broj cifara desno od decimalne tačke u datoj koloni, slična
                                           #istoimenoj funkciji u Javi
        self.OUTPUT_WAVE = np.empty(shape=self.INPUT_WAVE.shape)
        
        #np.empty pravi novi niz odredjenog tipa i oblika(dimenzije), ali se ne vrsi dodela vrednosti, 
        # tj.inicilizacija

        #kada stavimo svojstvo shape, time izražavamo da želimo da dobijemo trenutnu dimenziju matrice(dvodimenzionalnog ili višedimenzionalnog niza)
        
    def correct(self):
        step = int(self.INPUT_SR/20) #корак
        print('Detektovana frekvencija fq\tKorigovana frekvencija\tFaktor korekcije')
        
        for x in range(0,len(self.INPUT_WAVE),step):
            # проналази краткорочну Фуријеову трансформацију
            # прилагођава се најближој фреквенцији
            # врши се премештање
            # врши се додавање self.OUTPUT_WAVE
            # враћа излазни талас
            
            y = self.INPUT_WAVE[x:x+step]
            f = self._findStft(y)
            
            diff_array = [ np.abs(note - f) for note in self.NOTES ]
            note = np.argmin(diff_array)
            #np.argmax враћа индекс минималне вредности у низу/дуж осе
            print(f,end='\t')
            print(self.NOTES[note],end='\t')

            self.OUTPUT_WAVE[x:x+step] = self._transpose(y, f, self.NOTES[note])
           

            print('-------------------')
            return librosa.util.normalize(self.OUTPUT_WAVE)
        #librosa.util.normalize служи да нормализује низ дуж одабране осе
        #нпр. norm(S, axis=axis) == 1 нормализује сваки члан дводимензионалног низа
        #да смо ставили norm(S, axis=axis) == 2, вршила би се нормализација сваког другог члана низа, врши се скалирање
    
            def _findStft(self,y):
        # Ова функција користи краткорочну Фуријеову трансформацију и np.argmax да би пронашла највећу вредносту дуж осе

        yD = librosa.stft(y,n_fft=self.INPUT_SR)
        arr = np.argmax(yD,axis=0)
        #np.argmax враћа индекс максималнe вредности у низу/дуж осе
        
        
        
        #np.mean 
        
        
        
        fq = np.mean(arr)
        #израчунава аритметичку средину вредности у наведеном низу

        return self._note.normalize(fq)
    
    def _transpose(self, y, fold, fnew):
        # функција која израчунава потребан број корака за премештање на основу нових и старих фреквенција
        steps = self._note.getStep(fold,fnew)
        #getStep је генеричка метода, враћа информације о тренутном кораку
        print(steps)
        yT = librosa.effects.pitch_shift(y,self.INPUT_SR,steps)
        #librosa.effects.pitch_shift - pomera visinu talasa na osnovu broja koraka (steps)
        return yT
    
    
    
    
    
    
    
    
    

