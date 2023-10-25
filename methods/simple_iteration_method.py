from examples.base import BaseIntegralEquation


class SimpleIterationMethod:
    def __init__(self, ie: BaseIntegralEquation, eps: float = 0.001):
        """Initialize.

        :param ie: Integral equation
        :param eps: Predetermined accuracy
        """
        self.ie = ie
        self.eps = eps
        self.y = []

    def is_stop(self, y1: list[float], y2: list[float]) -> bool:
        """Check if iteration process should be stopped.

        :param y1: Previous solution
        :param y2: Current solution
        :return: True if the distance is small enough, False otherwise.
        """
        inaccuracy = max([abs(i - j) for i, j in zip(y1, y2)]) / max([abs(i) for i in y2])
        return inaccuracy <= self.eps

    def resolve(self, k: int = 0) -> list[float]:
        """Find a resolution with a predetermined accuracy.

        Recursive method.
        :param k: Iteration.
        :return: Resolution with a predetermined accuracy
        """
        self.y.append(self.next(k))
        if k > 0 and self.is_stop(self.y[k - 1], self.y[k]):
            return self.y[k]
        return self.resolve(k + 1)

    def next(self, k) -> list[float]:
        """Find the next approximation of the desired function.

        :param k: Iteration
        :return: Next approximation in the specified points.
        """
        if k == 0:
            return [self.ie.f(i) for i in range(len(self.ie.x))]
        return [self.y_k_i(k, i) for i in range(len(self.ie.x))]

    def y_k_i(self, k, i) -> float:
        """Find function value for iteration k and x[i].

        :param k: Number of the function approximation
        :param i: Index of point which solution is calculation for
        :return: Function value on the k iteration in x[i].
        """
        ie = self.ie
        if i == 0:
            return ie.f(i)
        return (
            ie.f(i)
            + (ie.A(i, i))
            * (ie.K(i, 0) * self.y[k - 1][0] + ie.K(i, i) * self.y[k - 1][i])
            + sum([ie.A(i, j) * ie.K(i, j) * self.y[k - 1][j] for j in range(1, i - 1)])
        )
