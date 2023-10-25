from tabulate import tabulate

from examples.examples import (
    EquationOne,
    EquationTwo,
    ExactSolutionTwo,
    ExactSolutionOne,
)
from methods.quadrature_method import QuadratureMethod
from methods.simple_iteration_method import SimpleIterationMethod


def show_table(examples, method):
    # todo refactor method
    for equation_class, solution, input_data in examples:
        equation = equation_class(*input_data)
        approximate = method(equation).resolve()
        exact = solution(*input_data).resolve()
        inaccuracy = [abs(ex - ap) for ex, ap in zip(exact, approximate)]
        print(
            tabulate(
                {
                    # A little issue with formatting
                    "x[i]": [f"\x1b[38;5;236m.\x1b[0m{i}" for i in equation.x],
                    "Exact": exact,
                    "Approximate": approximate,
                    "Inaccuracy": inaccuracy,
                },
                headers="keys",
                tablefmt="fancy_grid",
                floatfmt=".16",
            )
        )


if __name__ == "__main__":
    examples = (
        (EquationOne, ExactSolutionOne, (0, 0.1, 6)),
        (EquationTwo, ExactSolutionTwo, (0, 1, 51)),
    )
    show_table(examples, QuadratureMethod)
    show_table(examples, SimpleIterationMethod)
