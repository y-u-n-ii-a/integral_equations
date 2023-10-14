from quadrature_method.base import BaseIntegralEquation


class QuadratureMethod:
    def __init__(self, ie: BaseIntegralEquation):
        """Init.

        :param ie: Integral equation
        """
        self.ie = ie
        self.y = []

    def run(self) -> list[float]:
        for i in range(self.ie.n):
            self.y.append(self.next(i))
        return self.y

    def next(self, i: int) -> float:
        if i == 0:
            return self.ie.f(i)
        components = [
            self.ie.A(i, j) * self.ie.K(i, j) * self.y[j] for j in range(0, i)
        ]
        return ((1 - self.ie.A(i, i) * self.ie.K(i, i)) ** (-1)) * (
            self.ie.f(i) + sum(components)
        )
