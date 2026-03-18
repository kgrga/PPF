def k(unos): #provjerava je li unos kordinate broj
    while True:
        try:
            v=float(input(unos))
            return v
        except ValueError:
            print("Pogrešan unos! Molim upiši broj.")


print("Unesi koordinate prve točke:")
x1 = k("x1: ")
y1 = k("y1: ")


print("Unesi koordinate druge točke:")
x2 = k("x2: ")
y2 = k("y2: ")


if x1 == x2:
    print("Pravac je vertikalan i nema oblik y = mx + b.")
    print(f"x = {x1}")

else:
    n = (y2 - y1) / (x2 - x1)
    b = y1 - n * x1
    print(f"Jednadžba pravca je: y = {n}x + {b}")