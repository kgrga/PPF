def izracunaj_iteracije(N):
    broj = 5.0
    for _ in range(N):
        broj += 1/3
    for _ in range(N):
        broj -= 1/3
    return broj

iteracije = [200, 2000, 20000]
print("2) Rezultati za N iteracija:")
for N in iteracije:
    rezultat = izracunaj_iteracije(N)
    print(f"   N={N:5d} -> Rezultat: {rezultat:.20f}")

# OBJAŠNJENJE:
# Teoretski bi rezultat uvijek trebao biti 5.0. 
# Međutim, što je N veći, to se više "floating-point" pogrešaka nakuplja, 
# pa se konačni rezultat sve više udaljava od broja 5.