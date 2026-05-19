import numpy as np

#Dijametri 2R [mm]
promjeri_mm = np.array([
    [19.98, 20.18, 20.10, 20.08, 19.74],  #Valjak 1
    [19.92, 18.82, 19.96, 19.98, 19.88],  #Valjak 2
    [24.96, 24.98, 24.98, 24.92, 24.94]   #Valjak 3
])

#Duljine L [mm]
duljine_mm = np.array([
    [49.80, 49.00, 50.48, 49.80, 49.96],  #Valjak 1
    [52.56, 52.50, 52.62, 52.58, 52.54],  #Valjak 2
    [55.34, 55.40, 55.30, 55.44, 55.48]   #Valjak 3
])

#Mase m [g]
mase_g = np.array([
    [138.92, 138.98, 139.20, 138.90, 138.92], #Valjak 1
    [128.65, 128.60, 128.65, 128.35, 128.50], #Valjak 2
    [71.89,  71.90,  71.79,  71.85,  71.70]   #Valjak 3
])

#Pretvaramo promjere u radijuse
radijusi_mm = promjeri_mm / 2.0

#Broj mjerenja
n = 5

#2. POMOĆNA FUNKCIJA ZA STATISTIKU
def izracunaj_statistiku(matrica_podataka):
    """Računa srednju vrijednost i standardnu devijaciju (Jednadžbe 1 i 2)"""
    #Srednja vrijednost po retcima (axis=1)
    srednja = np.mean(matrica_podataka, axis=1)
    st_dev_srednje = np.std(matrica_podataka, axis=1, ddof=1) / np.sqrt(n)
    return srednja, st_dev_srednje

#3. IZRAČUN SREDNJIH VRIJEDNOSTI I POGREŠKI
R_srednje, sigma_R = izracunaj_statistiku(radijusi_mm)
L_srednje, sigma_L = izracunaj_statistiku(duljine_mm)
m_srednje, sigma_m = izracunaj_statistiku(mase_g)

#4. ISPIS REZULTATA PO VALJCIMA
print("=" * 60)
print(f"{'REZULTATI OBRADE MJERENJA (Vježba 6)':^60}")
print("=" * 60)

for i in range(3):
    valjak_num = i + 1
    print(f"\n--- VALJAK {valjak_num} ---")
    print(f"Srednji radijus R:  {R_srednje[i]:.4f} ± {sigma_R[i]:.4f} mm")
    print(f"Srednja duljina L:  {L_srednje[i]:.4f} ± {sigma_L[i]:.4f} mm")
    print(f"Srednja masa m:     {m_srednje[i]:.4f} ± {sigma_m[i]:.4f} g")
    
    #5. VOLUMEN (Jednadžba 3)
    # V = R^2 * pi * L
    V = (R_srednje[i]**2) * np.pi * L_srednje[i] # u mm^3
    # Pretvorba u cm^3 (jer je masa u gramima, pa želimo gustoću u g/cm^3)
    V_cm3 = V / 1000.0 
    
    #6. PROPAGACIJA POGREŠKE ZA VOLUMEN (Jednadžba 4)
    dV_dR = 2 * R_srednje[i] * np.pi * L_srednje[i]
    dV_dL = (R_srednje[i]**2) * np.pi
    
    #sigma_V u mm^3
    sigma_V = np.sqrt((dV_dR * sigma_R[i])**2 + (dV_dL * sigma_L[i])**2)
    sigma_V_cm3 = sigma_V / 1000.0
    
    print(f"Volumen V:          {V_cm3:.4f} ± {sigma_V_cm3:.4f} cm³")
    
    #7. GUSTOĆA (Jednadžba 5)
    rho = m_srednje[i] / V_cm3 # u g/cm^3

    #8. PROPAGACIJA POGREŠKE ZA GUSTOĆU (Jednadžba 4)
    drho_dm = 1.0 / V_cm3
    drho_dV = -m_srednje[i] / (V_cm3**2)
    
    sigma_rho = np.sqrt((drho_dm * sigma_m[i])**2 + (drho_dV * sigma_V_cm3)**2)
    
    print(f"Gustoća ρ:          {rho:.4f} ± {sigma_rho:.4f} g/cm³")

print("\n" + "=" * 60)
