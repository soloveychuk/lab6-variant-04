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
        pass

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
        pass

    def __str__(self):
        """Повертає рядкове представлення об'єкта інтегратора."""
        pass


class RectangleIntegrator(BaseIntegrator):
    """Обчислення інтеграла складеною формулою середніх прямокутників."""

    order = 2
    method_name = "Формула прямокутників"

    def __init__(self, func, a, b):
        super().__init__(func, a, b)        

    def integrate(self, n):
        h = (self.b - self.a) / n
        result = 0
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
        result = (self.func(self.a) + self.func(self.b)) / 2

        for i in range(1, n):
            x = self.a + i * h
            result += self.func(x)

        return result * h

class SimpsonIntegrator(BaseIntegrator):
    """Обчислення інтеграла складеною формулою Сімпсона."""

    order = None
    method_name = "Формула Сімпсона"

    def __init__(self, func, a, b):
        pass

    def integrate(self, n):
        pass
