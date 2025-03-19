import numpy as np

def fitness(x):
    return sum(x)

def generare_populatie(dimensiune, n):
    populatie = np.zeros([dimensiune, n], dtype="int")
    calitati = np.zeros(dimensiune)
    for i in range(dimensiune):
        populatie[i] = np.random.choice([0,1], n)
        calitati[i] = fitness(populatie[i])
    return populatie, calitati

def mutatie_populatie(copii, calitati_copii, probabilitate_mutatie):
    copii_m = copii.copy()
    calitati_m = calitati_copii.copy()
    lines = copii.shape[0] 
    col = copii.shape[1]
    for i in range(lines):
        mutat = False
        for j in range(col):
            raspuns = np.random.uniform(0, 1)
            if raspuns <= probabilitate_mutatie:
                copii_m[i, j] = not(copii[i, j])
                mutat = True
            if mutat:
                calitati_m[i] = fitness(copii_m[i])
    return copii_m, calitati_m 

# In this case, copii_m means copii mutati, and calitati_m means calitati_copii_mutati.
if __name__ == "__main__":
    lines = 10
    col = 4
    populatie, calitati = generare_populatie(lines, col)

    print(populatie)
    print(calitati)

    populatie_mutata, calitati_copii_mutati = mutatie_populatie(populatie, calitati, 0.1)
    print(populatie_mutata)
    print(calitati_copii_mutati)

