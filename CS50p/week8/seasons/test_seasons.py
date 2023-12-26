import pytest
from seasons import text

def test_seasons():
    assert text("524400") == "Five hundred twenty-four thousand, four hundred minutes"