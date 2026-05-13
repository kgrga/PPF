import math

M = [0.052, 0.124, 0.168, 0.236, 0.284, 0.336]
phi = [0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472]

n = len(M)


xy_mean = sum(m * p for m, p in zip(phi, M)) / n
x2_mean = sum(p**2 for p in phi) / n

a = xy_mean / x2_mean  #ovo je Dt

y2_mean = sum(m**2 for m in M) / n
sigma_a = math.sqrt((1/n) * ((y2_mean / x2_mean) - a**2))

print(f"4) Modul torzije Dt (parametar a): {a:.4f} Nm/rad")
print(f"   Pogreška sigma_a: {sigma_a:.4f}")