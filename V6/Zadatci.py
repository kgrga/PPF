import numpy as np


dijametri = {
    "Valjak 1": [19.98, 20.18, 20.10, 20.08, 19.74],
    "Valjak 2": [19.92, 19.82, 19.96, 19.98, 19.88],
    "Valjak 3": [24.96, 24.98, 24.98, 24.92, 24.94]
}

# Tablica 2: Duljine L [mm]
duljine = {
    "Valjak 1": [49.80, 49.00, 50.48, 49.80, 49.96],
    "Valjak 2": [52.56, 52.50, 52.62, 52.58, 52.54],
    "Valjak 3": [55.34, 55.40, 55.30, 55.44, 55.48]
}

# Tablica 3: Mase m [g]
mase = {
    "Valjak 1": [138.92, 138.98, 139.20, 138.90, 138.92],
    "Valjak 2": [128.65, 128.60, 128.65, 128.35, 128.50],
    "Valjak 3": [71.89, 71.90, 71.79, 71.85, 71.70]
}


# ZADATAK 1: Srednja vrijednost i standardna devijacija srednje vrijednosti

print("=" * 25 + " ZADATAK 1 " + "=" * 25)

def srednja_vrijednost(podaci):
    return sum(podaci) / len(podaci)

def standardna_devijacija_srednje(podaci):
    x_sr = srednja_vrijednost(podaci)
    n = len(podaci)
    suma_kvadrata = sum((x - x_sr) ** 2 for x in podaci)
    return np.sqrt(suma_kvadrata / (n * (n - 1)))

rezultati_z1 = {}

for valjak in dijametri.keys():
    # Polumjer R računamo kao dijametar podijeljen s 2 (2R / 2)
    radijusi_mm = [d / 2.0 for d in dijametri[valjak]]
    L_mm = duljine[valjak]
    m_g = mase[valjak]
    
    R_bar = srednja_vrijednost(radijusi_mm)
    sigma_R = standardna_devijacija_srednje(radijusi_mm)
    
    L_bar = srednja_vrijednost(L_mm)
    sigma_L = standardna_devijacija_srednje(L_mm)
    
    m_bar = srednja_vrijednost(m_g)
    sigma_m = standardna_devijacija_srednje(m_g)
    
    rezultati_z1[valjak] = {
        "R_bar": R_bar, "sigma_R": sigma_R,
        "L_bar": L_bar, "sigma_L": sigma_L,
        "m_bar": m_bar, "sigma_m": sigma_m
    }
    
    print(f"{valjak}:")
    print(f"  Srednji polumjer R = {R_bar:.4f} ± {sigma_R:.4f} mm")
    print(f"  Srednja duljina L  = {L_bar:.4f} ± {sigma_L:.4f} mm")
    print(f"  Srednja masa m     = {m_bar:.4f} ± {sigma_m:.4f} g")


# ZADATAK 2: Volumen valjka i propagacija pogreške

print("\n" + "=" * 25 + " ZADATAK 2 " + "=" * 25)

def volumen_valjka(R, L):
    # R i L moraju biti u centimetrima, vraća cm^3
    return np.pi * (R ** 2) * L

def sigma_volumena(R, sigma_R, L, sigma_L):
    # Formula dobivena parcijalnim deriviranjem funkcije V = pi * R^2 * L
    V = volumen_valjka(R, L)
    return V * np.sqrt((2 * sigma_R / R) ** 2 + (sigma_L / L) ** 2)

rezultati_z2 = {}

for valjak, res in rezultati_z1.items():
    # Pretvorba srednjih vrijednosti i pogrešaka iz mm u cm (dijeljenje s 10)
    R_cm = res["R_bar"] / 10.0
    sigma_R_cm = res["sigma_R"] / 10.0
    L_cm = res["L_bar"] / 10.0
    sigma_L_cm = res["sigma_L"] / 10.0
    
    V = volumen_valjka(R_cm, L_cm)
    sig_V = sigma_volumena(R_cm, sigma_R_cm, L_cm, sigma_L_cm)
    
    rezultati_z2[valjak] = {"V": V, "sigma_V": sig_V}
    
    # Ispis u znanstvenom zapisu (.4e)
    print(f"{valjak}: V = {V:.4e} ± {sig_V:.4e} cm^3")


# ZADATAK 3: Gustoća valjka i propagacija pogreške

print("\n" + "=" * 25 + " ZADATAK 3 " + "=" * 25)

def gustoca_valjka(m, V):
    return m / V

def sigma_gustoce(m, sigma_m, V, sigma_V):
    # Formula dobivena parcijalnim deriviranjem funkcije rho = m / V
    rho = gustoca_valjka(m, V)
    return rho * np.sqrt((sigma_m / m) ** 2 + (sigma_V / V) ** 2)

rezultati_z3 = {}

for valjak, res in rezultati_z1.items():
    m = res["m_bar"]
    sigma_m = res["sigma_m"]
    V = rezultati_z2[valjak]["V"]
    sigma_V = rezultati_z2[valjak]["sigma_V"]
    
    rho = gustoca_valjka(m, V)
    sig_rho = sigma_gustoce(m, sigma_m, V, sigma_V)
    
    rezultati_z3[valjak] = {"rho": rho, "sigma_rho": sig_rho}
    
    print(f"{valjak}: rho = {rho:.4f} ± {sig_rho:.4f} g/cm^3")



# ZADATAK 4: Određivanje materijala i relativna pogreška

print("\n" + "=" * 25 + " ZADATAK 4 " + "=" * 25)

# Standardne literaturne vrijednosti gustoća za najčešće metale u laboratoriju
literatura = {
    "Valjak 1": {"materijal": "Bakar (Cu)", "rho_lit": 8.96},
    "Valjak 2": {"materijal": "Željezo / Čelik (Fe)", "rho_lit": 7.86},
    "Valjak 3": {"materijal": "Aluminij (Al)", "rho_lit": 2.70}
}

for valjak, res in rezultati_z3.items():
    rho_calc = res["rho"]
    rho_lit = literatura[valjak]["rho_lit"]
    mat = literatura[valjak]["materijal"]
    
    # Formula za relativnu pogrešku
    rel_err = (abs(rho_calc - rho_lit) / rho_lit) * 100
    
    print(f"{valjak}:")
    print(f"  Izračunata gustoća: {rho_calc:.4f} g/cm^3")
    print(f"  Identificirani materijal: {mat} (literaturna gustoća: {rho_lit} g/cm^3)")
    print(f"  Relativna pogreška: {rel_err:.3f}%")



# ZADATAK 5: Analiza oblika standardne devijacije

print("\n" + "=" * 25 + " ZADATAK 5 " + "=" * 25)

malo_n = [99.8, 100.1, 99.9, 100.2, 100.0]

np.random.seed(42)
veliko_n = np.random.normal(loc=100.0, scale=0.2, size=10000).tolist()

def izracunaj_devijacije(podaci, naziv):
    n = len(podaci)
    sr_vrijednost = srednja_vrijednost(podaci)
    suma_kvadrata = sum((x - sr_vrijednost) ** 2 for x in podaci)
    
    sigma_n = np.sqrt(suma_kvadrata / n)
    s = np.sqrt(suma_kvadrata / (n - 1))
    sigma_x_bar = s / np.sqrt(n)
    
    print(f"{naziv} (n = {n}):")
    print(f"  sigma_n     = {sigma_n:.6f}")
    print(f"  s           = {s:.6f}")
    print(f"  sigma_x_bar = {sigma_x_bar:.6f}")
    return sigma_n, s

sig_n_m, s_m = izracunaj_devijacije(malo_n, "Mali skup")
sig_n_v, s_v = izracunaj_devijacije(veliko_n, "Veliki skup")

# Računanje relativne razlike između sigma_n i s
rel_razlika_malo = (abs(sig_n_m - s_m) / s_m) * 100
rel_razlika_veliko = (abs(sig_n_v - s_v) / s_v) * 100

print(f"\nRelativna razlika |sigma_n - s| / s:")
print(f"  Mali skup:  {rel_razlika_malo:.4f}%")
print(f"  Veliki skup: {rel_razlika_veliko:.4f}%")