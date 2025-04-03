# script pentru testul selectiei generatiei urmatoare - selectia de tip elitist
import numpy as np
from FunctiiSelectii import elitism
import generare_init as gi
import matplotlib.pyplot as grafic

def elitism(pop_curenta, cal_curente, copii_m, cal_copii_m, dimensiune):
    gen_urmatoare = copii_m.copy()
    cal_urmatoare = cal_copii_m.copy()

    max_curent = max(cal_curente)
    max_copii_m = max(cal_copii_m)

    if max_curent > max_copii_m:
        index_max = np.argmax(cal_curente)
        index_inlocuit = np.random.randint(0, dimensiune)
        gen_urmatoare[index_inlocuit] = pop_curenta[index_max].copy()
        cal_urmatoare[index_inlocuit] = cal_copii_m[index_max]
    return gen_urmatoare, cal_urmatoare




#generarea aleatoare a doua populatii
dim=6
n=16
p1=gi.gen(n,dim)
p2=gi.gen(n,dim)
genu,valori=elitism(p1[:,:n],p1[:,n],p2[:,:n],p2[:,n],dim)
#constituirea populatiei rezultate
rez=np.zeros([dim,n+1],dtype='int')
rez[:,:n]=genu.copy()
rez[:,n]=valori.copy()
print('populatia1')
print(p1)
print('populatia2')
print(p2)
print('selectat:')
print(rez)

x=[i for i in range(dim)]
grafic.plot(x,p1[:,n],"go",markersize=18,label='Populatia curenta')
grafic.plot(x,p2[:,n],"bo",markersize=14,label='Copiii eventual mutati')
grafic.plot(x,rez[:,n],"ro",markersize=10,label='Generatia urmatoare')
grafic.legend()
grafic.show()
