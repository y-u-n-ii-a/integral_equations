from quadrature_method.examples import EquationOne, EquationTwo
from quadrature_method.method import QuadratureMethod

if __name__ == "__main__":
    # todo compare results with different n
    print(QuadratureMethod(EquationOne(0, 0.1, 6)).run())
    print(QuadratureMethod(EquationTwo(0, 1, 11)).run())
