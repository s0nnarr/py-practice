import numpy as np

# Crossover vectori binari sau int

# Crossover unipunct intre x si y, vectori cu n componente
# I: x, y, n
# E: c1, c2 - cei doi copii - cu n componente

def crossover_unipunct(x, y, n):
    # Genereaza aleator punctul de crossover, intre 1 si n-1 pentru a avea efect
    # in pozitia n este calitatea
    i = np.random.randint(1, n-1)
    c1 = x.copy();
    c2 = y.copy();

    # Selectarea secventelor care compun primul copil
    c1[0:i] = x[0:i]
    c1[i:n] = y[i:n]

    # Selectarea secventelor care compun al doilea copil
    c2[0:i] = y[0:i]
    c2[i:n] = x[i:n]
    return c1, c2

# Crossover unfirom intre x si y, vectori cu n componente
# I: x, y, n
# E: c1, c2 - cei doi copii

def crossover_uniform(x, y, n):
    c1 = x.copy()
    c2 = y.copy()

    # Constructia copiilor
    for i in range(n):
        r = np.random.randint(0, 2)
        # Daca r == 1, interschimbam alelele din i
        if r == 1:
            c1[i] = y[i]
            c2[i] = x[i]
            