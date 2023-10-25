import math

from examples.base import BaseIntegralEquation


class EquationOne(BaseIntegralEquation):
    def K(self, i, j):
        return math.e ** (-(self.x[i] - self.x[j]))

    def A(self, i, j):
        if j == 0 or i == j:
            return self.h / 2
        return self.h

    def f(self, i):
        return math.e ** (-self.x[i])


class ExactSolutionOne(EquationOne):
    def resolve(self):
        return [1 for _ in self.x]


class EquationTwo(BaseIntegralEquation):
    def K(self, i, j):
        return math.e ** (self.x[i] - self.x[j])

    def A(self, i, j):
        if j == 0 or i == j:
            return self.h / 2
        return self.h

    def f(self, i):
        return math.e ** (-self.x[i]) * math.sin(self.x[i])


class ExactSolutionTwo(EquationTwo):
    def resolve(self):
        return [
            0.1 * math.e ** (2 * x)
            - 0.1 * math.e ** (-x) * math.cos(x)
            + 0.7 * math.e ** (-x) * math.sin(x)
            for x in self.x
        ]
