from functions.exer_four_func import reverse_strings
import pytest

# Ejercicio #4: reverse_strings - 3 unit tests
# Caso #1 test con un texto pequeño
def test_reverse_string_with_short_text():
    #arrange
    short_string = "Hola mundo"
    #act
    result = reverse_strings(short_string)
    #assert
    assert result == "odnum aloH"

# Caso #2 test con un texto largo
def test_reverse_string_with_long_text():
    #arrange
    long_string = "Actualmente, esto también pasa en el periodismo. Las pautas de escritura pensadas en atraer clicks se basan " \
    "en reducir y fragmentar los textos lo más posible, llenar de negritas, subtítulos, fotos y de todos los recursos visuales habidos " \
    "y por haber para hacer que el lector no se agote, que no pierda la atención entre tanta palabra. No se puede ya escribir “mucho " \
    "texto”, así que allí estamos los periodistas intentando con un título que venda captar esa audiencia dispersa para no quedar sin " \
    "lectores, sin trabajo. Esto ha afectado especialmente a la prensa escrita, que hoy se basa en la fórmula del título anzuelo tipo " \
    "Un meteorito podría chocar con la tierra en 100 años o El consumo de las papas fritas produce depresión,  seguido de una bajada " \
    "sensacionalista que todo sugiere y nada explica, para terminar en un texto decorado con flores y fuegos artificiales que aunque " \
    "poco dice, espera con fe que alguien lo lea hasta final. El problema de esto es que casi nadie llega a ese final."
    #act
    result = reverse_strings(long_string)
    #assert
    assert result == ".lanif ese a agell eidan isac euq se otse ed amelborp lE .lanif atsah ael ol neiugla euq ef noc arepse ,ecid ocop euqnua euq selaicifitra sogeuf y serolf noc odaroced otxet nu ne ranimret arap ,acilpxe adan y ereigus odot euq atsilanoicasnes adajab anu ed odiuges  ,nóiserped ecudorp satirf sapap sal ed omusnoc lE o soña 001 ne arreit al noc racohc aírdop otiroetem nU opit oleuzna olutít led alumróf al ne asab es yoh euq ,atircse asnerp al a etnemlaicepse odatcefa ah otsE .ojabart nis ,serotcel nis radeuq on arap asrepsid aicneidua ase ratpac adnev euq olutít nu noc odnatnetni satsidoirep sol somatse ílla euq ísa ,”otxet ohcum“ ribircse ay edeup es oN .arbalap atnat ertne nóicneta al adreip on euq ,etoga es on rotcel le euq recah arap rebah rop y sodibah selausiv sosrucer sol sodot ed y sotof ,solutítbus ,satirgen ed ranell ,elbisop sám ol sotxet sol ratnemgarf y ricuder ne nasab es skcilc rearta ne sadasnep arutircse ed satuap saL .omsidoirep le ne asap néibmat otse ,etnemlautcA"

# Caso #3 test con un parametro que no sea texto
def test_reverse_string_with_no_string_parameter():
    #arrange
    no_string = 5
    #act & assert
    with pytest.raises(TypeError):
        reverse_strings(no_string)