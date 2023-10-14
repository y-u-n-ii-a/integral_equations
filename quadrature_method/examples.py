import math

from quadrature_method.base import BaseIntegralEquation


class EquationOne(BaseIntegralEquation):
    def K(self, i, j):
        return math.e ** (-(self.x[i] - self.x[j]))

    def A(self, i, j):
        if j == 0 or i == j:
            return self.h / 2
        return self.h

    def f(self, i):
        return math.e ** (-self.x[i])

# todo we have a solution to this ie (y === 1)


class EquationTwo(BaseIntegralEquation):
    def K(self, i, j):
        return 1 + self.x[i] - self.x[j]

    def A(self, i, j):
        if j == 0 or i == j:
            return self.h / 2
        return self.h

    def f(self, i):
        return 3 * (math.e ** (-2*self.x[i])) + 2 * self.x[i] + 1

# todo we have a solution to this ie (page 48)
