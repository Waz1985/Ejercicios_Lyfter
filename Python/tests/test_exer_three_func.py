from functions.exer_three_func import sum_list
import pytest

# Ejercicio #3: sum_list - 3 unit tests
# Caso #1 test con una lista pequeña de unos 10 elementos
def test_sum_list_with_small_list():
    #arrange
    num_list = list(range(11))
    #act
    result = sum_list(num_list)
    #assert
    assert result == 55

# Caso #2 test con una lista grande, mas de 100 elementos
def test_sum_list_with_big_list():
    #arrange
    num_list = list(range(150))
    #act
    result = sum_list(num_list)
    #assert
    assert result == 11175

# Caso #3 test de fallo con un parametro que no sea un numero 
def test_sum_list_with_no_list_parameter():
    #arrange
    num_list = "list(range(150))"
    #act & assert
    with pytest.raises(TypeError):
        sum_list(num_list)
