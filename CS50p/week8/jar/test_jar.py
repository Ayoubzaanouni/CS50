import pytest
from jar import Jar

def test_init():
    jar = Jar()

def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    with pytest.raises(ValueError):
        jar.deposit(30)

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(4)
    assert str(jar) == "🍪🍪🍪🍪🍪"


def test_withdraw():
    jar = Jar()
    jar.deposit(8)
    jar.withdraw(5)
    assert jar.size == 3
    with pytest.raises(ValueError):
        jar.withdraw(55)
