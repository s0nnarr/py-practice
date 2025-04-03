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
    return c1, c2


# Crossover permutari
# Operatorul PMX
# I: permutarile x, y de dimensiune n
# E: copii rezultati c1, c2

def crossover_PMX(x, y, n):
    # Generarea secventei de crossover
    poz = np.random.randint(0, n, 2)
    while poz[0] == poz[1]:
        poz = np.random.randint(0, n, 2)
    
    p1 = np.min(poz)
    p2 = np.max(poz)

    c1 = PMX(x, y, n, p1, p2)
    c2 = PMX(y, x, n, p1, p2)
    return c1, c2

# Aplica PMX pe x, y de dimensiune n, cu secventa de recombinare (p1, p2)
def PMX(x, y, n, p1, p2):
    # Initializare copil - un vector cu toate elementele - 1, valori care s = sa nu fie in 0,...,n-1
    c = -np.ones(n, dtype=int)
    # Copiaza secventa comuna in copilul c
    c[p1:p2+1] = x[p1:p2+1]
    # Analiza secventei comune - in permutarea y
    for i in range(p1, p2+1):
        # Plasarea alelei a 
        a = y[i]
        if a not in c:
            curent = i
            plasat = False
            while not plasat:
                b = x[curent]
                # poz = pozitia in care se afla b in y
                [poz] = [j for j in range(n) if y[j] == b]
                if c[poz] == -1:
                    c[poz] = a
                    plasat = True
                else:
                    curent = poz

    # z = vectorul alelelor din y inca necopiate in c
    z = [y[i] for i in range(n) if y[i] not in c]
    # poz - vectorul pozitiilor libere in c - cele cu valori - 1
    poz = [i for i in range(n) if c[i] == -1]
    # Copierea alelelor inca necopiate din y in c
    m = len(poz)
    for i in range(m):
        c[poz[i]] = z[i]
    return c 

# Operatorul OCX
# I: permutarile x, y, de dimensiune n
# E: copii rezultati c1, c2
def crossover_OCX(x, y, n):
    # Generarea secventei de crossover
    poz = np.random.randint(0, n, 2)
    while poz[0] == poz[1]:
        poz = np.random.randint(0, n, 2)
    p1 = np.min(poz)
    p2 = np.max(poz)
    c1 = OCX(x, y, n, p1, p2)
    c2 = OCX(y, x, n, p1, p2)

    return c1, c2


# Aplica OCX pe x, y, de dimensiune n, cu secventa de recombinare p1, p2
def OCX(x, y, n, p1, p2):
    # Copiaza secventa comuna in c2
    c2 = [x[i] for i in range(p1, p2+1)]
    # Calculeaza z pe baza lui y: componentele incepand cu p2 pana la n si apoi de la 0 la p2-1, excluzant elementele care au fost deja copiate
    z1 = [y[i] for i in range(p2, n) if y[i] not in c2]
    z2 = [y[i] for i in range(p2) if y[i] not in c2]
    z = np.append(z1, z2)

    # Calculeaza secventa finala a individului rezultat - din z de la 0 la n-p2
    c3 = [z[i] for i in range(n-p2-1)]

    # Calculeaza secventa de inceput a individului rezultat - din z de la n-p2...len(z)
    c1 = [z[i] for i in range(n-p2-1, len(z))]
    c = np.append(c1, c2)
    c = np.append(c, c3)
    return c

# Operatorul CX
# I: permutarile x, y, de dimensiune n - completate cu fitnessul
# E: copii rezultati c1, c2
def crossover_CX(x, y, n):
    ciclu = cicluri(x, y, n)
    c1 = x.copy()
    c2 = y.copy()
    for i in range(n):
        cat, rest = np.divmod(ciclu[i], 2)
        # Sunt inteschimbate alelele din cicluri pare
        # Primul ciclu este etichetat cu 1
        if not rest:
            c1[i] = y[i]
            c2[i] = x[i]
    return c1, c2

# Calculul ciclurilor din
# I: x, y, de dimensiune n
# E: vectorul ciclu, unde ciclu[i] = nr. ciclului din care fac parte x[i] si y[i]
def cicluri(x, y, n):
    
