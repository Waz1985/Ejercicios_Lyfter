from functions.exer_six_func import order_string
import pytest

# Ejercicio #5: order_string - 3 unit tests
# Caso #1 test con un texto pequeño
def test_find_upper_and_lower_characters_from_short_text():
    #arrange
    my_string = "python-variable-funcion-computadora-monitor"
    #act
    result = order_string(my_string)
    #assert
    assert result == "computadora-funcion-monitor-python-variable"

# Caso #2 test con un texto largo
def test_find_upper_and_lower_characters_from__long_text():
    #arrange
    my_string = "python-variable-function-computer-monitor-keyboard-mouse-processor-memory-algorithm-data-structure-object-oriented-programming-testing-debugging-performance-optimization-software-development-version-control-git-github-continuous-integration-deployment-automation-virtual-environment-package-management"
    #act
    result = order_string(my_string)    
    #assert
    assert result == "algorithm-automation-computer-continuous-control-data-debugging-deployment-development-environment-function-git-github-integration-keyboard-management-memory-monitor-mouse-object-optimization-oriented-package-performance-processor-programming-python-software-structure-testing-variable-version-virtual"

# Caso #3 test con un parametro que no sea texto
def test_find_upper_and_lower_characters_from_no_string_parameter_exception_expected():
    #arrange
    no_string = []
    #act & assert
    with pytest.raises(TypeError):
        order_string(no_string)