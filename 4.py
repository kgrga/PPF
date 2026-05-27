import matplotlib.pyplot as plt
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


srednja_svih = np.mean(mase)
med_svih = medijan(mase)

mase_ociscene = [x for x in mase if 1.5 < x < 3.0]

srednja_ociscena = np.mean(mase_ociscene)
med_ociscen = medijan(mase_ociscene)

print(f"Sa pogreškama - srednja: {srednja_svih:.4f}, medijan: {med_svih:.4f}")
print(f"Bez pogrešaka - srednja: {srednja_ociscena:.4f}, medijan: {med_ociscen:.4f}")
print(f"\nPromjena srednje vrijednosti: {abs(srednja_svih - srednja_ociscena):.4f}")
print(f"Promjena medijana: {abs(med_svih - med_ociscen):.4f}")
print("\nZaključak: Medijan se gotovo nije promijenio.")

plt.figure(figsize=(10, 6))
plt.hist(
    mase, bins=15, color="slategray", edgecolor="white", alpha=0.6, label="Sva mjerenja"
)

plt.axvline(
    srednja_svih,
    color="crimson",
    linewidth=2.5,
    label=f"Srednja (sve) = {srednja_svih:.3f}",
)
plt.axvline(
    med_svih,
    color="orange",
    linewidth=2.5,
    linestyle="--",
    label=f"Medijan (sve) = {med_svih:.3f}",
)
plt.axvline(
    srednja_ociscena,
    color="navy",
    linewidth=2.5,
    label=f"Srednja (očišćeno) = {srednja_ociscena:.3f}",
)
plt.axvline(
    med_ociscen,
    color="dodgerblue",
    linewidth=2.5,
    linestyle="--",
    label=f"Medijan (očišćeno) = {med_ociscen:.3f}",
)

plt.xlabel("Masa (Sirius A)")
plt.ylabel("Frekvencija")
plt.title("Zadatak 4: Utjecaj grubih pogrešaka na srednju vrijednost i medijan")
plt.legend(fontsize=9, loc="upper right")
plt.grid(axis="y", linestyle=":", alpha=0.5)
plt.tight_layout()
plt.savefig("4.png", dpi=150)
plt.show()