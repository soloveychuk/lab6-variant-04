"""Головний модуль запуску чисельного інтегрування."""

import math

from integrators import (
    RectangleIntegrator,
    SimpsonIntegrator,
    TrapezoidIntegrator,
)


def target_function(x):
    """Підінтегральна функція згідно з індивідуальним варіантом."""
    return math.sin(x) * math.exp(-x**2)
def control_function(x):
    """Функція контрольного прикладу."""
    if abs(x) <= 1e-8:
        return -0.5
    return (math.cos(x) - 1) / x**2


def main():

    methods = [
        RectangleIntegrator,
        TrapezoidIntegrator,
        SimpsonIntegrator,
    ]

    for eps in (1e-5, 1e-6):
        print(f"\nВаріант №4, точність: {eps}")

        for method in methods:
            integrator = method(target_function, 0.0, 1.0)
            result, n, error = integrator.adaptive_integrate(1e-4)

            print(integrator)
            print(f"Уточнений інтеграл: {result:.7f}")
            print(f"Кількість розбиттів: {n}")
            print(f"Оцінка похибки: {error:.2e}\n")



if __name__ == "__main__":
    main()
