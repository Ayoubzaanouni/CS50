from numb3rs import validate

def test_validate():
    assert validate("cs50") == False
    assert validate("7.7.7.7") == True
    assert validate("1.212.2000.0") == False
    assert validate("1.212.700.300") == False