import pytest
from twttr import shorten

def test_twtte():
    assert shorten("ayoOubB./1")=="ybB./1"
