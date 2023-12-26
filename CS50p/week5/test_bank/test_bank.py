import pytest
from bank import value

def test_bank():
    assert(value("hello"))== 0
    assert(value("hmid"))== 20
    assert(value("ahds"))== 100
    assert(value("HELLO"))== 0