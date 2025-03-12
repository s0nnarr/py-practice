import numpy as np
L=[1, 2, 3, 4]

print(L)
L.append(7) # Adds to the back of the list.
print(L)
L.insert(1, 100) # Inserts element 100 at index 1
print(L)

# Extindere
L.extend([1, 1, 1, 1]) # Aceeasi forma cu L=L+[x, y, z]
L=L+[2,2,2]

print(L)

L.clear() # Stergere completa
print(L)

# Generare aleatoare 
import random
L = random.choices([0, 1, 2, 3], k=10)
print(L)

# Accesarea primelor 9 si a ultimului
A=L[:-1]
ultim = L[-1]

print(A)
print(ultim)

val_max = max(L)
poz_max=L.index(val_max)

print(val_max)
print(poz_max)

L.clear()

L = random.choices([0,1,2,3], k=20)
maxim=max(L)
Poz_max=[poz for poz, element in enumerate(L) if element==maxim] # Toate pozitiile elementului maxim din L
print(L)
print(maxim)
print(Poz_max)

L1 = random.choices([0, 1, 2, 3], k=10)
L2 = random.choices([0, 1, 2, 3], k=10)

dot_L1L2 = sum([x*y for x, y in zip(L1,L2)])

print(L1)
print(L2)


