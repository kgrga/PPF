import matplotlib.pyplot as plt
import numpy as np

# Generiranje podataka iz vježbe
np.random.seed(42)
mase_ciste = np.random.normal(loc=2.06, scale=0.05, size=57).tolist()


def hist(podaci, k):
    xmin = min(podaci)
    xmax = max(podaci)
    h = (xmax - xmin) / k

    # Stvaranje rubova razreda
    rub = [xmin + i * h for i in range(k + 1)]
    f = [0] * k

    for x in podaci:
        if x == xmax:
            f[-1] += 1  
        else:
            indeks = int((x - xmin) // h)
            if 0 <= indeks < k:
                f[indeks] += 1

    print("Tekstualni histogram:")
    for i in range(k):
        print(f"[{rub[i]:.2f}, {rub[i+1]:.2f}): {f[i]}")

    return rub, f


k_razreda = 10
rub, f = hist(mase_ciste, k=k_razreda)

sirina_stupca = rub[1] - rub[0]

plt.figure(figsize=(8, 5))

plt.bar(
    rub[:-1],
    f,
    width=sirina_stupca * 0.95,
    align="edge",
    color="slategray",
    edgecolor="black",
)

plt.xlabel("Masa (Sirius A)")
plt.ylabel("Frekvencija")
plt.title("Zadatak 1: Ručno izračunati histogram")

plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.savefig("1.png", dpi=150)
plt.show()