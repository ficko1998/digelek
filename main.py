import ui,autotune
import iscrtavanje
import sys #овај модул садржи константе, функције и методе Пајтон интерпретера

def viewHelp():
    print('\nAutomatska korekcija visine tona')
    print('\tOvo je mali pokušaj mene kao studenta softverskog inženjerstva da napravim autotjun, koji se danas masovno koristi u muzičkoj industriji.')
    print('\tU ovom programu kao ulaz treba da se koristi wav datoteka i potom se datoteka podešava na ulaznu skalu.')
    print('\nKako radi sve ovo...')
    print('\tOvaj moj pokušaj autotjuna radi kroz nekoliko sledećih koraka:')
    print('\t1. Uzima se samo mali deo podataka. Uglavnom ovo traje manje od sekunde po podatku.')
    print('\t2. U koraku 2 prebacuje podatak u frekvencijski domen koristeći kratkoročnu Furijeovu transformaciju ')
    print('\t3. Pronalazi maksimalnu amplitudu i to će biti dominantna frekvencija.')
    print('\t4. Usklađuje tu frekvenciju sa najbližom frekvencijom na skali.')
    print('\t5. Premešta trenutnu frekvenciju na dobijenu frekvenciju. Dodaje to izlaznom talasu.')
    print('\t6. Prelazi na sledeći podatak, ponavlja postupak za celu frekvencu.')
    

def start(ip,op,scale):
    io = ui.IO(ip)
    y, sr = io.load()
    
    auto = autotune.Autotune(y,sr,scale)
    print('Započinje korekcija visine talasa.')
    yT = auto.correct()
    print('Visina talasa korigovana.')

    input('Pritisnite bilo koje dugme da biste videli izlaz.')
    print('Izračunavanje izlaza')
    plt = iscrtavanje.Plotter(y,sr,yT,sr)
    plt.plot()

    #print('Puštamo izlaz na %s...'%op,end='')
    io.dump(op,yT,sr)
    print('Završeno.')

if __name__ == '__main__':
    if len(sys.argv) < 3:
        viewHelp()
        sys.exit(0) #стандардни начин за излаз
    else:
        op = 'output.wav'
        if sys.argv[1] == '-h' or sys.argv[1] == '--help':
            #sys.argv[1] је први аргумент који се шаље програму
            #sys.argv[0] је име програма који се позива
            
            #ако се никакво име скрипте не проследи Пајтон интерпретатору, sys.argv ће бити празан стринг
            viewHelp()
            sys.exit(0)
        else:
            ip = sys.argv[1]
            scale = int(sys.argv[2])
            if sys.argv[3] is not None:
                op = sys.argv[3]
            start(ip,op,scale)
            print('Napuštanje...')

