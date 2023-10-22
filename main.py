from tabulate import tabulate

from quadrature_method.examples import (
    EquationOne,
    EquationTwo,
    ExactSolutionTwo,
    ExactSolutionOne,
)
from quadrature_method.method import QuadratureMethod

if __name__ == "__main__":
    examples = (
        (EquationOne, ExactSolutionOne, (0, 0.1, 6)),
        (EquationTwo, ExactSolutionTwo, (0, 1, 51)),
    )

    for equation_class, solution, input_data in examples:
        equation = equation_class(*input_data)
        approximate = QuadratureMethod(equation).resolve()
        exact = solution(*input_data).resolve()
        inaccuracy = [abs(ex - ap) for ex, ap in zip(exact, approximate)]
        print(
            tabulate(
                {
                    # A little issue with formatting
                    "x[i]": [f'\x1b[38;5;236m.\x1b[0m{i}' for i in equation.x],
                    "Exact": exact,
                    "Approximate": approximate,
                    "Inaccuracy": inaccuracy,
                },
                headers="keys",
                tablefmt="fancy_grid",
                floatfmt=".16",
            )
        )
