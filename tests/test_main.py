import pytest
from main import calculate_and_print

# Parameterize the test function to cover different operations and scenarios, including errors
@pytest.mark.parametrize("a_string, b_string, operation_string, expected_string", [
    ("8", "7", 'add', "The result of 8 add 7 is equal to 15"),
    ("8", "4", 'subtract', "The result of 8 subtract 4 is equal to 4"),
    ("3", "4", 'multiply', "The result of 3 multiply 4 is equal to 12"),
    ("10", "2", 'divide', "The result of 10 divide 2 is equal to 5"),
    ("10", "0", 'divide', "An error occurred: Cannot divide by zero"),  # Adjusted for the actual error message
    ("6", "3", 'unknown', "Unknown operation: unknown"),  # Test for unknown operation
    ("a", "4", 'add', "Invalid number input: a or 4 is not a valid number."),  # Testing invalid number input
    ("1", "b", 'subtract', "Invalid number input: 1 or b is not a valid number.")  # Testing another invalid number input
])
def test_calculate_and_print(a_string, b_string, operation_string,expected_string, capsys):
    calculate_and_print(a_string, b_string, operation_string)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_string