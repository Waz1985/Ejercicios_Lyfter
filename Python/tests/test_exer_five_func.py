from functions.exer_five_func import find_upper_lower
import pytest

# Ejercicio #5: find_upper_lower - 3 unit tests
# Caso #1 test con un texto pequeño
def test_find_upper_and_lower_characters_from_short_text():
    #arrange
    my_string = "Hola Mundo."
    #act
    result = find_upper_lower(my_string)
    #assert
    assert result == f"There are 2 upper cases and 9 lower cases"

# Caso #2 test con un texto largo
def test_find_upper_and_lower_characters_from__long_text():
    #arrange
    my_string = "Actualmente, esto también pasa en el periodismo. Las pautas de escritura pensadas en atraer clicks se basan " \
    "en reducir y fragmentar los textos lo más posible, llenar de negritas, subtítulos, fotos y de todos los recursos visuales habidos " \
    "y por haber para hacer que el lector no se agote, que no pierda la atención entre tanta palabra. No se puede ya escribir “mucho " \
    "texto”, así que allí estamos los periodistas intentando con un título que venda captar esa audiencia dispersa para no quedar sin " \
    "lectores, sin trabajo. Esto ha afectado especialmente a la prensa escrita, que hoy se basa en la fórmula del título anzuelo tipo " \
    "Un meteorito podría chocar con la tierra en 100 años o El consumo de las papas fritas produce depresión,  seguido de una bajada " \
    "sensacionalista que todo sugiere y nada explica, para terminar en un texto decorado con flores y fuegos artificiales que aunque " \
    "poco dice, espera con fe que alguien lo lea hasta final. El problema de esto es que casi nadie llega a ese final."
    #act
    result = find_upper_lower(my_string)    
    #assert
    assert result == "There are 7 upper cases and 986 lower cases"

# Caso #3 test con un parametro que no sea texto
def test_find_upper_and_lower_characters_from_no_string_parameter_exception_expected():
    #arrange
    no_string = 5
    #act & assert
    with pytest.raises(TypeError):
        find_upper_lower(no_string)