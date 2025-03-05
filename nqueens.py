# We have N number of queens, on an NxN chess board.
# Queens must be positioned in a way so that they cannot attack.
# Hill climbing method.

# Explanation: Queens attack if they are:
#     - In the same row (handled by permutation)
#     - In the same diagonal


import numpy as np

def calitate(p):
    # p is the arrangement of queens. p[i] represents the position of the queen.
    n = p.size
    valoare = int(n*(n-1)/2)

    for i in range (n-1):
        for j in range(i+1, n):
            if abs(i-j) == abs(p[i] - p[j]): # If two queens are on the same diagonal
                valoare = valoare - 1 # Reduce quality (they can attack)
    return valoare;

def vecini(p):
    # This generates all possible neighboring configurations by swapping two columns.
    n = p.size
    vecini_p = np.zeros([int(n*(n-1)/2), n], dtype="int") # Stores all neighbors
    calitati_p = np.zeros(int(n*(n-1)/2), dtype="int") # Stores qualities.

    counter = 0
    for i in range(n-1):
        for j in range(i+1, n):
            x = p.copy()
            x[i], x[j] = p[j], p[i] # Swaps two columns 
            vecini_p[counter] = x.copy()
            calitati_p[counter] = calitate(x)
            counter = counter + 1
    return vecini_p, calitati_p

def hillclimb(n):
    p = np.random.permutation(n)
    c = calitate(p)
    local = False
    while not local:
        v_p, c_vp = vecini(p)
        index = np.argmax(c_vp)
        best_v = v_p[index].copy()
        best_c = c_vp[index]

        if c < best_c:
            p = best_v.copy()
            c = best_c
        else:
            local = True
    return p, c

if __name__ == "__main__":
    n = 8
    configuratie, valoare = hillclimb(n)
    
    print("Config: ")
    print(configuratie)
    print("Nr. de aranjari gresite: ", int(n*(n-1)/2)-valoare)