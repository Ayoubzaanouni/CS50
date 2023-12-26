from um import count
def test1():
    result = count("hello, um,Cs50")
    assert result == 1

def test2():
    result = count("um, hello, um, CS50")
    assert result == 2

def test3():
    result = count("Um...")
    assert result == 1
def test4():
    result = count("CS50")
    assert result == 0
    assert count("um") == 1
    assert count('yummy') == 0
    assert count("Um, welcom, um...") == 2