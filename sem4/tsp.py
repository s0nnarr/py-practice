# Travelling salesman problem. 

# Given a list of nodes, what is the shortest possible route that visits each node exactly once and returns to the origin node?
# costuri.txt contains a matrix of values, i and j representing the nodes, and x[i][j] the cost between node i and node j
from cProfile import label
import numpy as np
import matplotlib.pyplot as grafic

def fitness(p, c):
    # This checks the quality of the solution.
    n = p.size
    cost = c[p[n-1], p[0]]
    # c[p[n-1], p[0]] -> cost from the last node to the initial node.
    
    for i in range(n-1):
        cost += c[p[i], p[i+1]]
    return 100/cost

def generare(nume_fis, dimensiune):
    c = np.genfromtxt(nume_fis)
    n = c.shape[0] # Returns the dimension of the first line
    populatie = np.zeros([dimensiune, n], dtype="int") # Creates an empty population with zeroes, of type int
    calitati = np.zeros(dimensiune)
    for i in range(dimensiune):
        populatie[i] = np.random.permutation(n)
        calitati[i] = fitness(populatie[i], c) # Verifies the random permutation's fitness/quality + the cost of the permutation.

    # Graph
    OX = [i for i in range(dimensiune)]
    OY = calitati

    # OY axis will be used to display the quality marks of the current solution.
    # OX will represent the nodes (1, 2, 3, etc...)

    grafic.plot(OX, OY, "gs", markersize=12, label="Initial") 
    return populatie, calitati, c

def mutatie_populatie(copii, calitati_copii, c, probabilitate_mutatie):
    copii_mutati = copii.copy()
    calitati_copii_mutati = calitati_copii.copy()
    dim = copii.shape[0]
    for i in range(dim):
        raspuns = np.random.uniform(0, 1)
        if raspuns <= probabilitate_mutatie:
            print(f"Individul ales {copii[i]} calitatea {calitati_copii[i]:.3f}")
            copii_mutati[i] = mutatie_inversiune(copii[i])
            calitati_copii_mutati[i] = fitness(copii_mutati[i], c)
            print(f"Individul rezultat {copii[i]} calitatea {calitati_copii_mutati[i]:.3f}")
    
    # Graph
    OX = [i for i in range(dim)]
    OY = calitati_copii_mutati
    grafic.plot(OX, OY, "rs", markersize=10, label="Dupa mutatie")
    
    return copii_mutati, calitati_copii_mutati

def mutatie_inversiune(individ):
    n = individ.size
    i = np.random.randint(0, n-1) # returns random integers from the "discrete uniform" distribution
    j = np.random.randint(i+1, n)
    print(f"Pozitiile {i} {j}")
    rezultat = individ.copy()
    rezultat[i:j+1] = [individ[k] for k in range(j, i-1, -1)]
    return rezultat
 
if __name__=="__main__":
    dim = 14
    P_init, C_init, c = generare("costuri.txt", dim)
    for i in range(dim):
        print(f"Individ {P_init[i]} calitate {C_init[i]:.3f}")

    P_mutat, C_mutat = mutatie_populatie(P_init, C_init, c, 0.15)
    grafic.legend()
    grafic.show()

"""
Algorithm explication:
1. We create a random initial solution population.
2. We evaluate the quality of every route using the fitness function.
3. We apply mutations to explore new solutions.
4. We display graphs with the evolution of each solution.
"""