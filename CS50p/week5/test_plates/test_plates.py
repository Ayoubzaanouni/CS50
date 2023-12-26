import pytest
from plates import is_valid

def test_valid():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("P") == False
    assert is_valid("CD9.26") == False
    assert is_valid("hshshshsshsshsh") == False
    assert is_valid("CCC77C") == False
    assert is_valid("77BD") == False
    assert is_valid("77") == False