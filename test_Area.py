import menu_driven_task_pytesting
import pytest

def test_area_square():
    side=3
    result=menu_driven_task_pytesting.area_square(side)
    assert result == side * side

@pytest.mark.perimeterarearec
def test_perimeter_rect():
    l=2
    w=3
    result=menu_driven_task_pytesting.perimeter_rect(l,w)
    assert result == 2*(l+w)

@pytest.mark.perimeterarearec
def test_area_rect():
    l=3
    b=2
    result=menu_driven_task_pytesting.area_rect(l,b)
    assert result == l*b

