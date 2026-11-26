"""Модуль реалізації класів чисельного інтегрування."""


class BaseIntegrator:
    """Базовий клас для чисельного обчислення визначених інтегралів."""

    order = 1
    method_name = "Базовий метод"


    def __init__(self, func, a, b):
        """Ініціалізує підінтегральну функцію та межі інтегрування."""
        self.validate_bounds(a, b)
        self.func = func
        self.a = a
        self.b = b

    @classmethod
    def from_dict(cls, func, params):
        """Альтернативний конструктор для створення інтегратора зі словника."""
        return cls(func, params["a"], params["b"])

    @staticmethod
    def validate_bounds(a, b):
        """Перевіряє коректність меж інтегрування."""
        if a >= b:
            raise ValueError("a має бути менше за b")

    def integrate(self, n):
        """Обчислює наближене значення інтеграла для n розбиттів."""
        raise NotImplementedError

    def adaptive_integrate(self, eps=1e-4, initial_n=2):
        """Знаходить інтеграл із заданою точністю eps за правилом Рунге."""
         # Початкова кількість розбиттів
        n = initial_n
        previous = self.integrate(n)
        while True:
            n *= 2
            current = self.integrate(n)

            # Обчислення поправки Річардсона та оцінки похибки Рунге
            correction = (current - previous) /(2 ** self.order - 1)
            error = abs(correction)

            # Перевірка досягнення заданої точності
            if error <= eps:
                return current + correction, n, error

            previous = current


    def __str__(self):
        """Повертає рядкове представлення об'єкта інтегратора."""
        return f"{self.method_name} на [{self.a}; {self.b}]"

class RectangleIntegrator(BaseIntegrator):
    """Обчислення інтеграла складеною формулою середніх прямокутників."""

    order = 2
    method_name = "Формула прямокутників"

    def __init__(self, func, a, b):
        super().__init__(func, a, b)        

    def integrate(self, n):

        # Визначення кроку інтегрування
        h = (self.b - self.a) / n
        result = 0

        # Обчислення суми значень функції в серединах відрізків
        for i in range(n):
            x = self.a + (i + 0.5) * h
            result += self.func(x)

        return result * h



class TrapezoidIntegrator(BaseIntegrator):
    """Обчислення інтеграла складеною формулою трапецій."""

    order = 2
    method_name = "Формула трапецій"

    def __init__(self, func, a, b):
        super().__init__(func, a, b)

    def integrate(self, n):
        h = (self.b - self.a) / n
        result = (self.func(self.a) + self.func(self.b)) / 2 # Врахування значень функції на кінцях відрізка

        for i in range(1, n):
            x = self.a + i * h
            result += self.func(x)

        return result * h

class SimpsonIntegrator(BaseIntegrator):
    """Обчислення інтеграла складеною формулою Сімпсона."""

    order = 4
    method_name = "Формула Сімпсона"

    def __init__(self, func, a, b):
        super().__init__(func, a, b)

    def integrate(self, n):

        # Перевірка коректності кількості розбиттів
        if n < 2 or n % 2 != 0:
            raise ValueError("n має бути парним і не меншим за 2")
        h = (self.b - self.a) / n
        result = (self.func(self.a) + self.func(self.b))
        for i in range(1, n):
            x = self.a + i * h

            if i % 2 == 0:
                result += 2 * self.func(x)
            else:
                result += 4 * self.func(x)

        return result * h / 3
