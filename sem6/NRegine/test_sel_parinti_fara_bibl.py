# script pentru testul selectiei parintilor - selectia de tip ruleta cu distributie fps cu sigma-scalare
import numpy as np
from tensorflow.python.ops.gen_math_ops import cumulative_logsumexp

import generare_init as gi
import matplotlib.pyplot as grafic


def calcul_prob_cumulata(Calitati):
    fps = Calitati/sum(Calitati)
    dimensiune = Calitati.size
    medie = np.mean(Calitati)
    dev_std = np.std(Calitati) # standard deviation

    cal_sigma = [max(Calitati[i]-(medie-2*dev_std), 0) for i in range(dimensiune)]
    cal_sigma = np.array(cal_sigma)
    if sum(cal_sigma) > 0:
        fps_sigma = cal_sigma/sum(cal_sigma)
    else:
        fps_sigma = fps.copy()
    q = fps_sigma.copy()
    for i in range(1, dimensiune):
        q[i] = q[i-1] + fps_sigma[i] 
    return q

def ruleta(pop_curenta, cal_curente, dimensiune, n):
    parinti = pop_curenta.copy()
    cal_parinti = cal_curente.copy()
    q = calcul_prob_cumulata(cal_curente)
    for i in range(dimensiune):
        r = np.random.uniform(0, 1)
        pozitii = np.where(q>=r) # pozitiile unde q >= r
        index_selectat = pozitii[0][0]
        parinti[i] = pop_curenta[index_selectat].copy()
        cal_parinti[i] = cal_curente[index_selectat]
    return parinti, cal_parinti
    


#generarea aleatoare a unei populatii
dim=8
n=10
p=gi.gen(n,dim)
#populatia p este impartita in matricea indivizilor si vectorul calitatilor
# calculul parintilor si calitatii acestora utilizand selectia ruleta cu FPS cu sigma scalare
parinti,valori=ruleta(p[:,:n],p[:,n],dim,n)
#constituirea populatiei rezultate
rez=np.zeros([dim,n+1],dtype='int')
rez[:,:n]=parinti.copy()
rez[:,n]=valori.copy()
print("Populatia considerata curenta")
print(p)
print("Populatia de parinti")
print(rez)


x=[i for i in range(dim)]
grafic.plot(x,p[:,n],"go",markersize=16,label='Calitatile populatiei curente')
grafic.plot(x,rez[:,n],"ro",markersize=10,label='Calitatile parintilor')
grafic.legend()
grafic.show()

