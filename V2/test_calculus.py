import math
import matplotlib.pyplot as plt
import calculus as calculus

# Test funkcije i derivacije

def cubic(x: float) -> float:
    return x**3


def cubic_derivative(x: float) -> float:
    return 3 * x**2


def trig(x: float) -> float:
    return math.sin(x)


def trig_derivative(x: float) -> float:
    return math.cos(x)

# Pomoćna funkcija za crtanje

def plot_function_derivative(
    func,
    exact_derivative,
    x_min,
    x_max,
    title,
    epsilons,
    method,
    num_points=400):

    points, _ = calculus.derivative_range(
        func,
        x_min,
        x_max,
        num_points=num_points,
        epsilon=epsilons[0],
        method=method)

    exact_values = [exact_derivative(x) for x in points]

    plt.figure(figsize=(10, 6))
    plt.plot(points, exact_values, label="Analitička derivacija", linewidth=2)

    for eps in epsilons:
        points_num, values_num = calculus.derivative_range(
            func,
            x_min,
            x_max,
            num_points=num_points,
            epsilon=eps,
            method=method)
        plt.plot(
            points_num,
            values_num,
            label=f"Numerička ({method}, ε={eps})",
            linestyle="--")

    plt.title(title)
    plt.xlabel("x")
    plt.ylabel("f'(x)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

# Test integrala


def square(x: float) -> float:
    return x**2


def square_integral(x: float) -> float:
    return x**3 / 3

print("\n--- Integracija test ---")

lower, upper = calculus.integral_rectangles(square, 0, 3, 50)
trap = calculus.integral_trapezoid(square, 0, 3, 50)

exact = square_integral(3) - square_integral(0)

print("Analitički:", exact)
print("Pravokutnici donja:", lower)
print("Pravokutnici gornja:", upper)
print("Trapezna:", trap)

def plot_integral_test():
    steps = [5, 10, 20, 50, 100, 200]
    rect_lower = []
    rect_upper = []
    trapez = []
    exact = []

    for n in steps:
        l, u = calculus.integral_rectangles(square, 0, 3, n)
        t = calculus.integral_trapezoid(square, 0, 3, n)
        rect_lower.append(l)
        rect_upper.append(u)
        trapez.append(t)
        exact.append(square_integral(3) - square_integral(0))

    plt.figure(figsize=(10,6))
    plt.plot(steps, exact, label="Analitički", linewidth=2)
    plt.plot(steps, rect_lower, "--", label="Pravokutna donja")
    plt.plot(steps, rect_upper, "--", label="Pravokutna gornja")
    plt.plot(steps, trapez, "--", label="Trapezna")
    plt.xlabel("Broj koraka")
    plt.ylabel("Vrijednost integrala")
    plt.legend()
    plt.grid(True)

# Glavni dio programa

if __name__ == "__main__":
    # Brzi ispis jedne točke
    print("Kubna funkcija f(x) = x^3")
    print("f'(2) analitički =", cubic_derivative(2))
    print("f'(2) numerički, three-step =", calculus.derivative_at(cubic, 2))
    print("f'(2) numerički, two-step   =", calculus.derivative_at(cubic, 2, method="two-step"))
    print()

    print("Trigonometrijska funkcija f(x) = sin(x)")
    print("f'(0) analitički =", trig_derivative(0))
    print("f'(0) numerički, three-step =", calculus.derivative_at(trig, 0))
    print("f'(0) numerički, two-step   =", calculus.derivative_at(trig, 0, method="two-step"))

    epsilons = [1e-1, 1e-2, 1e-4]

    # Kubna funkcija - three-step
    plot_function_derivative(
        cubic,
        cubic_derivative,
        x_min=-3,
        x_max=3,
        title="f(x) = x^3  |  Derivacija  |  three-step",
        epsilons=epsilons,
        method="three-step")

    # Kubna funkcija - two-step
    plot_function_derivative(
        cubic,
        cubic_derivative,
        x_min=-3,
        x_max=3,
        title="f(x) = x^3  |  Derivacija  |  two-step",
        epsilons=epsilons,
        method="two-step")

    # Trigonometrijska funkcija - three-step
    plot_function_derivative(
        trig,
        trig_derivative,
        x_min=-2 * math.pi,
        x_max=2 * math.pi,
        title="f(x) = sin(x)  |  Derivacija  |  three-step",
        epsilons=epsilons,
        method="three-step")

    # Trigonometrijska funkcija - two-step
    plot_function_derivative(
        trig,
        trig_derivative,
        x_min=-2 * math.pi,
        x_max=2 * math.pi,
        title="f(x) = sin(x)  |  Derivacija  |  two-step",
        epsilons=epsilons,
        method="two-step")

    plot_integral_test()
    
    plt.show()

