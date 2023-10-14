from abc import abstractmethod


class BaseIntegralEquation:
    def __init__(self, a: float, b: float, n: int):
        self.n = n
        self.h = (b - a) / (n - 1)
        self.x = [self.h * i for i in range(0, n)]

    @abstractmethod
    def K(self, i, j):
        raise NotImplementedError()

    @abstractmethod
    def A(self, i, j):
        raise NotImplementedError()

    @abstractmethod
    def f(self, i):
        raise NotImplementedError()
