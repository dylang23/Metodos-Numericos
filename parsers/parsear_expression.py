from sympy import Symbol, lambdify, Expr, sin
from sympy.parsing.sympy_parser import parse_expr, standard_transformations
from sympy.parsing.sympy_parser import implicit_multiplication, implicit_application, function_exponentiation


def str_to_exprsympy(expression: str) -> Expr:
    
    x = Symbol('x')
    
    expression = expression.replace('^', '**')
    expression = expression.replace('cosx', 'cos(x)')
    local_dict = {'x': x, 'sen': sin}
    
    transformations = standard_transformations + \
        (implicit_multiplication, implicit_application, function_exponentiation)

    expression_sympy = parse_expr(expression, local_dict=local_dict, transformations=transformations)

    return expression_sympy


def exprsympy_to_function(expression_sympy: Expr) -> callable:
    
    x = Symbol('x')
    
    function = lambdify(x, expression_sympy, "numpy")

    return function


def str_to_function(expression: str) -> callable:
    
    expr_sympy = str_to_exprsympy(expression)
    
    function = exprsympy_to_function(expr_sympy)

    return function

