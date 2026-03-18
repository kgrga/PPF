def pravac(x1, y1, x2, y2):
    if x1 == x2:
        print("Pravac je vertikalan:")
        print(f"x = {x1}")
    else:
        n = (y2 - y1) / (x2 - x1)
        b = y1 - n * x1
        print(f"Jednadžba pravca je: y = {n}x + {b}")


x1 = float(input("Unesi x1: "))
y1 = float(input("Unesi y1: "))
x2 = float(input("Unesi x2: "))
y2 = float(input("Unesi y2: "))


pravac(x1, y1, x2, y2)