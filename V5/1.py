#a) Oduzimanje

ocekivano = 0.065
dobiveno = 5.0 - 4.935

print(f"1a) Očekivano: {ocekivano}")
print(f"    Dobiveno:  {dobiveno}")

#b) Suma 0.1, 0.2, 0.3

suma = 0.1 + 0.2 + 0.3
test = (suma == 0.6)

print(f"1b) Suma 0.1+0.2+0.3: {suma}")
print(f"    Je li jednako 0.6? {test}")

# OBJAŠNJENJE:
# Računala koriste binarni sustav. Neki decimalni brojevi (poput 0.1) 
# nemaju konačan prikaz u binarnom sustavu (kao 1/3 u dekadskom), 
# što rezultira malim pogreškama u preciznosti (floating-point error).