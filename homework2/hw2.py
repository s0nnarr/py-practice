# Tema ~ Seminariile 4-7
import numpy as np

# 1.
def functie_obiectiv(p):
    n = len(p)
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if p[i] == j + 1 and p[j] == i + 1:
                count += 1
    return count

# Avem o populatie (e.g [3, 1, 2, 5])
# Functia obiectiv / fitness (p[i] = j; p[j] = i, sau ex. p[0] = 3 && p[3] = 0, in cazul asta avem o pereche.)
# Cu cat mai multe perechi, cu atat este mai mare maximul.

def generatie_populatie(dim, n):
    pop = []
    for _ in range(dim): 
        perm = np.random.permutation(n) + 1
        fitness = functie_obiectiv(perm)
        individ = np.append(perm, fitness)
        # Individ este un array pentru a tine cont de permutatie + fitness ul permutatiei.
        pop.append(individ)
    return np.array(pop, dtype=int)

def mutatie_inserare(pop, pm):
    #pm = probabilitatea mutatiei
    popm = pop.copy()
    dim = pop.shape[0]
    n = pop.shape[1] - 1
    

    for i in range(dim):
        if np.random.uniform(0, 1) <= pm:
            individ = popm[i, :-1] # Excludem fitness-ul
            poz1, poz2 = np.random.choice(n, 2, replace=False)
            val = individ[poz2]
            individ = np.delete(individ, poz2)
            individ = np.insert(individ, poz1, val)

            fitness = functie_obiectiv(individ)
            popm[i, :-1] = individ # Actualizam cromozomul
            popm[i, -1] = fitness # Recalculam fitness-ul.
    
    return popm

if __name__ == "__main__":
    dim = 5 # Nr. indivizi
    n = 6 # Lungimea permutarii
    pm = 0.2 # Probabilitatea de mutatie
    pop = generatie_populatie(dim, n)
    print(f"Populatia initiala: \n{pop}")

    popm = mutatie_inserare(pop, pm)
    print(f"Pop. dupa mutatie: \n{popm}")

