from examples.base import BaseIntegralEquation


class QuadratureMethod:
    def __init__(self, ie: BaseIntegralEquation):
        """Initialize.

        :param ie: Integral equation
        """
        self.ie = ie
        self.y = []

    def resolve(self) -> list[float]:
        """Find a resolution."""
        for i in range(self.ie.n):
            self.y.append(self.next(i))
        return self.y

    def next(self, i: int) -> float:
        """Find value for the next point.

        :param i: Index of a point
        :return: Function value in a point with index i.
        """
        if i == 0:
            return self.ie.f(i)
        components = [
            self.ie.A(i, j) * self.ie.K(i, j) * self.y[j] for j in range(0, i)
        ]
        return ((1 - self.ie.A(i, i) * self.ie.K(i, i)) ** (-1)) * (
            self.ie.f(i) + sum(components)
        )
