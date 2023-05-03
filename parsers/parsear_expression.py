from sympy import Symbol, lambdify, Expr, sin
from sympy.parsing.sympy_parser import parse_expr, standard_transformations
from sympy.parsing.sympy_parser import implicit_multiplication, implicit_application, function_exponentiation


def str_to_exprsympy(expression: str) -> Expr:

    expression = expression.replace('^', '**')
    expression = expression.replace('cosx', 'cos(x)')
    local_dict = {'sen': sin}

    transformations = standard_transformations + \
        (implicit_multiplication, implicit_application, function_exponentiation)

    expression_sympy = parse_expr(
        expression, local_dict=local_dict, transformations=transformations)

    return expression_sympy


def exprsympy_to_function(expression_sympy: Expr, variables) -> callable:

    symbols = [Symbol(var) for var in variables]

    function = lambdify(symbols, expression_sympy, "numpy")

    return function


def str_to_function(expression: str, variables=['x']) -> callable:

    expr_sympy = str_to_exprsympy(expression)

    function = exprsympy_to_function(expr_sympy, variables)

    return function
