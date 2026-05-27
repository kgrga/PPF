import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
mase_ciste = np.random.normal(loc=2.06, scale=0.05, size=57).tolist()

sred = np.mean(mase_ciste)
med = np.median(mase_ciste)

print(f"Aritmetička sredina: {sred:.4f}")
print(f"Medijan: {med:.4f}")

plt.figure(figsize=(8, 5))
counts, bins, patches = plt.hist(
    mase_ciste, bins=10, color="slategray", edgecolor="white", label="Frekvencija"
)

print("\nFrekvencije po razredima (za usporedbu):")
print(counts.astype(int).tolist())

plt.axvline(
    sred,
    color="palevioletred",
    linewidth=2.5,
    linestyle="-",
    label=f"Srednja = {sred:.3f}",
)
plt.axvline(
    med,
    color="darkorange",
    linewidth=2.5,
    linestyle="--",
    label=f"Medijan = {med:.3f}",
)

plt.xlabel("Masa (Sirius A)")
plt.ylabel("Frekvencija")
plt.title("Zadatak 2: Gotov modul s linijama središnjih tendencija")
plt.legend()
plt.grid(axis="y", linestyle=":", alpha=0.6)
plt.tight_layout()
plt.savefig("2.png", dpi=150)
plt.show()