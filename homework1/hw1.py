"""
1. Scrieți o funcție Python pentru implementarea funcției de maxim
𝑓: {(𝑥, 𝑦, 𝑧) 𝑥, 𝑦, 𝑧 ∈ [−2,7], 𝑥 + 𝑦 + 𝑧 < 10⁄ } → ℝ
𝑓(𝑥, 𝑦, 𝑧) = 𝑥2 − 2𝑦 ∙ 𝑧
Generați 20 elemente din spațiul soluțiilor (candidați la soluție), evaluați-le și afișați valorile obținute.

"""

import random

# Def f(x, y, z)
def f(x, y, z):
    return x**2 - 2 * y * z

candidates=[] #generate 20 sol.
while len(candidates) < 20:
    x = random.uniform(-2, 7)
    y = random.uniform(-2, 7)
    z = random.uniform(-2, 7)

    if x + y + z < 10:
        candidates.append((x, y, z))

for i, (x,y,z) in enumerate(candidates):
    result = f(x,y,z)
    print(f"Solutia {i+1}: x={x:.2f}, y={y:.2f}, z={z:.2f} -> f(x,y,z)={result:.2f}")



"""

"""