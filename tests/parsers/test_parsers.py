from parsers.parsear_expression import str_to_function


def test_str_to_function_only_symbol():
    expr = "2*x + 1"
    function = str_to_function(expr)
    x = 5
    assert function(5) == 11


def test_str_to_function_multiple_symbol():
    expr = "2*x + 2y2*4 "
    function = str_to_function(expr, variables=['x', 'y2'])
    x = 5
    y = 2
    assert function(5,2) == 26
