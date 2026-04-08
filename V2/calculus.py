from typing import Callable, List, Tuple

def _validate_method(method: str) -> str:
    method = method.lower().strip()
    allowed = {"three-step", "two-step"}

    if method not in allowed:
        raise ValueError(
            f"Nepoznata metoda: '{method}'. Dozvoljeno: {allowed}")

    return method


def derivative_at(
    func: Callable[[float], float],
    x: float,
    epsilon: float = 1e-5,
    method: str = "three-step") -> float:
    
    if epsilon <= 0:
        raise ValueError("epsilon mora biti pozitivan broj.")

    method = _validate_method(method)

    if method == "three-step":
        return (func(x + epsilon) - func(x - epsilon)) / (2 * epsilon)

    return (func(x + epsilon) - func(x)) / epsilon    # method == "two-step"


def derivative_range(
    func: Callable[[float], float],
    x_min: float,
    x_max: float,
    num_points: int = 200,
    epsilon: float = 1e-5,
    method: str = "three-step") -> Tuple[List[float], List[float]]:
    
    if x_min >= x_max:
        raise ValueError("Mora vrijediti x_min < x_max.")
    if num_points < 2:
        raise ValueError("num_points mora biti barem 2.")
    if epsilon <= 0:
        raise ValueError("epsilon mora biti pozitivan broj.")

    _validate_method(method)

    step = (x_max - x_min) / (num_points - 1)
    points = [x_min + i * step for i in range(num_points)]
    derivatives = [
        derivative_at(func, x, epsilon=epsilon, method=method)
        for x in points]

    return points, derivatives


def integral_rectangles(
    func: Callable[[float], float],
    x_min: float,
    x_max: float,
    num_steps: int = 100) -> Tuple[float, float]:

    if x_min >= x_max:
        raise ValueError("Mora vrijediti x_min < x_max.")
    if num_steps < 1:
        raise ValueError("num_steps mora biti >= 1.")

    dx = (x_max - x_min) / num_steps

    lower = 0.0
    upper = 0.0

    for i in range(num_steps):
        x1 = x_min + i * dx
        x2 = x1 + dx

        f1 = func(x1)
        f2 = func(x2)

        lower += min(f1, f2) * dx
        upper += max(f1, f2) * dx

    return lower, upper


def integral_trapezoid(
    func: Callable[[float], float],
    x_min: float,
    x_max: float,
    num_steps: int = 100) -> float:

    if x_min >= x_max:
        raise ValueError("Mora vrijediti x_min < x_max.")
    if num_steps < 1:
        raise ValueError("num_steps mora biti >= 1.")

    dx = (x_max - x_min) / num_steps
    total = 0.0

    for i in range(num_steps):
        x1 = x_min + i * dx
        x2 = x1 + dx

        total += (func(x1) + func(x2)) * dx / 2

    return total