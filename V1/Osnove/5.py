import matplotlib.pyplot as plt


def pravac_i_graf(x1, y1, x2, y2, spremi=False, ime=None): 
    if x1 == x2:
        print("Vertikalni pravac: x =", x1)
        x = [x1, x1]
        y = [y1, y2]
    else:
        n = (y2 - y1) / (x2 - x1)
        b = y1 - n * x1
        print(f"Jednadžba pravca: y = {n}x + {b}")

        # generiranje x vrijednosti za crtanje pravca
        x = [x1, x2]
        y = [b * i + b for i in x]


    plt.figure()
    plt.plot(x, y, label="Pravac")
    plt.scatter([x1, x2], [y1, y2], color='red', label="Točke")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Pravac kroz dvije točke")
    plt.legend()
    plt.grid()


    if spremi:
        plt.savefig(ime)
        print(f"Graf spremljen kao: {ime}")
    else:
        plt.show()


x1 = float(input("Unesi x1: "))
y1 = float(input("Unesi y1: "))
x2 = float(input("Unesi x2: "))
y2 = float(input("Unesi y2: "))


izbor = input("Upiši 'p' za prikaz ili 's' za spremanje u PDF: ")


if izbor.lower() == 's':
    im = input("Unesi ime datoteke (npr. graf.pdf): ")
    pravac_i_graf(x1, y1, x2, y2, spremi=True, ime=im)

else:
    pravac_i_graf(x1, y1, x2, y2)