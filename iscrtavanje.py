import librosa
import librosa.display as disp
import matplotlib.pyplot as plt

#скрипта у којој вршимо исцртавање
class Plotter:
    N_ROWS = 3
    N_COLUMNS = 3

    def __init__(self,y,sr,oy,osr):
        self.INPUT_WAVE = y
        self.INPUT_SR = sr
        self.OUTPUT_WAVE = oy
        self.OUTPUT_SR = osr

    def plot(self):
        '''Iscrtava talasni oblik, spektogram snage i hromogram.
        Leva kolona će prikazati ulazni talas, a desna kolona izlazni talas.
        '''
        
        plt.subplot(321) #subplot користимо кад хоћемо на једном графику да исцртамо више функција
        #321 значи да мрежа на графику буде 3х2, а 1 значи да је то први цртеж на заједничком графику
        #ово важи и за све остале графике испод, само што се мења задњи број-параметар у загради
        plt.title('Ulazn talasni oblik')
        self.plotWave(self.INPUT_WAVE,self.INPUT_SR)

        plt.subplot(322)
        plt.title('Izlazni talasni oblik')
        self.plotWave(self.OUTPUT_WAVE,self.OUTPUT_SR)

        plt.subplot(323)
        plt.title('Ulazni spektogram snage')
        self.plotSpec(self.INPUT_WAVE,self.INPUT_SR) 
        
        plt.subplot(324)
        plt.title('Izlazni spektogram snage')
        self.plotSpec(self.OUTPUT_WAVE,self.OUTPUT_SR) 

        plt.subplot(325)
        plt.title('Ulazni hromatograf')
        self.plotChroma(self.INPUT_WAVE,self.INPUT_SR) 

        plt.subplot(326)
        plt.title('Izlazni hromatograf')
        self.plotChroma(self.OUTPUT_WAVE,self.OUTPUT_SR) 

        plt.show() #приказује исцртану фигуру
        #ову команду треба да ставимо углавном само једном у току неке пајтон скрипте
        #ако се стави више пута, а пошто зависи од графичког backend-a рачунара, може да прави проблеме
        

        return

    def plotWave(self,y,sr):
        print('Iscrtavanje talasnog oblika',end='') #ово end само специфицира шта се исписује на крају
        disp.waveplot(y,sr)
        print('Završeno.')
        return

    def plotSpec(self,y,sr):
        print('Iscrtavanje spektograma snage',end="")
        #Спектрограм је визуелни приказ спектра фреквенција у звук или други сигнал који варира временом или неком другом променљивом. 
        yD = librosa.stft(y,n_fft=sr) #враћа матрицу комплексних вредности
        disp.specshow(librosa.amplitude_to_db(yD),y_axis='log',x_axis='time')
        print('Završeno.')
        return

    def plotChroma(self,y,sr):
        print('Iscrtavanje hromatografa',end='')
              
        cD = librosa.feature.chroma_stft(y,n_fft=sr)
        
        #librosa.feature je modul koji radi na bazi kratkorocne furijeove transf.
        disp.specshow(cD,y_axis='chroma',x_axis='time')
        print('Završeno.')
        return
