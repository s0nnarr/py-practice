"""
1. Scrieți o funcție Python pentru implementarea funcției de maxim
𝑓: {(𝑥, 𝑦, 𝑧) 𝑥, 𝑦, 𝑧 ∈ [−2,7], 𝑥 + 𝑦 + 𝑧 < 10⁄ } → ℝ
𝑓(𝑥, 𝑦, 𝑧) = 𝑥2 − 2𝑦 ∙ 𝑧
Generați 20 elemente din spațiul soluțiilor (candidați la soluție), evaluați-le și afișați valorile obținute.

"""

import random

# Def f(x, y, z)
# def f(x, y, z):
#     return x**2 - 2 * y * z

# candidates=[] #generate 20 sol.
# while len(candidates) < 20:
#     x = random.uniform(-2, 7)
#     y = random.uniform(-2, 7)
#     z = random.uniform(-2, 7)

#     if x + y + z < 10:
#         candidates.append((x, y, z))

# for i, (x,y,z) in enumerate(candidates):
#     result = f(x,y,z)
#     print(f"Solutia {i+1}: x={x:.2f}, y={y:.2f}, z={z:.2f} -> f(x,y,z)={result:.2f}")



"""

2. Scrieți o funcție Python care generează o matrice (populație) cu 18 linii vectori cu 6 elemente: 5 biți
reprezentând un individ și un număr întreg reprezentând calitatea acestuia. Calitatea unui individ este
dată de numărul perechilor de valori consecutive diferite (de exemplu, calitatea lui [1,0,0,1,1] = 2).
Calculați și afișați indivizii cu cea mai mare valoare a funcției calitate.

"""

def generate_individual():
    individual = [random.choice([0, 1]) for _ in range(5)]
    quality = sum(1 for i in range(4) if individual[i] != individual[i+1])
    return individual, quality

def generate_population(size=18):
    # generate a matrix with 18 lines by default
    population = [generate_individual() for _ in range(size)]
    return population

def print_population(population):
    max_quality = max(q for _, q in population)

    print("\nGenerated population: ")
    for individual, quality in population:
        print(f"Individ: {individual} | Calitate: {quality}")

    print("\nIndivizii cu cea mai mare calitate: ");
    for individual, quality in population: 
        if quality == max_quality:
            print(f"Individ: {individual} | Calitate: {quality}")

population = generate_population()
print_population(population)


