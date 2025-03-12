# Backpack problem.

import numpy as np
import random
import matplotlib.pyplot as grafic

def fitness(v, c, CMax, x):
    #value = the value of the object.
    #cost = the dimension/space occupied in the backpack.
    #x = binary list/array where x[i] = 1 means the item is included, and x[i] = 0 means the item is not included.
    #CMax is total capacity.
    value = np.dot(v, x)
    cost = np.dot(c, x)
    
    return value, cost <= CMax

def generate(fis_v, fis_c, CMax, dim):
    #generate a random solution.
    v = np.genfromtxt(fis_v)
    c = np.genfromtxt(fis_c)

    n = len(v)
    population = []
    i = 0
    while i < dim:
        x = random.choices([0,1], k=n)
        val_x, feasible_x = fitness(v, c, CMax, x)
        if feasible_x:
            x.append(val_x)
            population.append(x)
            i+=1
    draw(population, dim)
    return population

def draw(population, dim):
    OX = [i for i in range(dim)]
    OY = [population[i][-1] for i in range(dim)]

    grafic.plot(OX, OY, "rs", markersize=10)
    grafic.show()

if __name__=='__main__':
    p = generate("valoare.txt", "cost.txt", 45, 10)
    for i in p:
        print(f"Individul {i[:-1]} cu fitness {i[-1]}")


