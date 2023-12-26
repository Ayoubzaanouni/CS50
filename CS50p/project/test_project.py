
from main import newPipe, get_highest_score, update_highest_score

def test_newPipe():
    pipe = newPipe()
    assert pipe == None

def test_get_highest_score_empty():
    update_highest_score(0)
    score = get_highest_score()
    assert score == 0

def test_update_highest_score():
    update_highest_score(50)
    score = get_highest_score()
    assert score == 50

def test_update_highest_score_twice():
    update_highest_score(50)
    update_highest_score(100)
    score = get_highest_score()
    assert score == 100
