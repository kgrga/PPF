import numpy as np

np.random.seed(42)
mase_ciste = np.random.normal(loc=2.06, scale=0.05, size=57).tolist()
mase = mase_ciste + [6.0, 1.2, 3.2, 4.5, 8.5, 7.8, 0.08, 0.02]


def medijan(podaci):
    sortirani = sorted(podaci)
    n = len(sortirani)
    if n % 2 != 0:
        return sortirani[n // 2]
    else:
        return (sortirani[n // 2 - 1] + sortirani[n // 2]) / 2.0


a = [3, 1, 4, 1, 5, 9, 2, 6]
b = [3, 1, 4, 1, 5, 9, 2, 6, 5]

print(f"Medijan a: {medijan(a)} | numpy: {np.median(a)}")
print(f"Medijan b: {medijan(b)} | numpy: {np.median(b)}")
print(f"Medijan mase: {medijan(mase):.4f} | numpy: {np.median(mase):.4f}")