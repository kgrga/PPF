import math
import statistics

podaci = [1.2, 2.5, 3.8, 4.1, 5.9, 6.3, 7.7, 8.2, 9.4, 10.0] 

#a) Ručno računanje

n = len(podaci)
sredina = sum(podaci) / n

suma_kvad_raz = sum((x - sredina)**2 for x in podaci)
st_devijacija = math.sqrt(suma_kvad_raz / (n * (n - 1)))

print(f"3a) Ručno -> Sredina: {sredina:.4f}, St. Dev: {st_devijacija:.4f}")

#b) Korištenje modula

sredina_modul = statistics.mean(podaci)
print(f"3b) Modul -> Sredina: {sredina_modul:.4f}")