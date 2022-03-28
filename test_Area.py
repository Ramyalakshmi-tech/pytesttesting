import Area
import pytest

def test_area_square():
    side=3
    result=Area.area_square(side)
    assert result == side * side

@pytest.mark.perimeterarearec
def test_perimeter_rect():
    l=2
    w=3
    result=Area.perimeter_rect(l,w)
    assert result == 2*(l+w)

@pytest.mark.perimeterarearec
def test_area_rect():
    l=3
    b=2
    result=Area.area_rect(l,b)
    assert result == l*b

