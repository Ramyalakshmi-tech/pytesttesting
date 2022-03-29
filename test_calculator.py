import calculator
import pytest

@pytest.mark.parametrize('a,b,c',[(3,2,1),(5,1,6),(8,2,10)])
def test_add2numbers(a,b,c):

    res=calculator.add2numbers(a,b)
    assert res==a+b
@pytest.mark.parametrize('a,b,c',[(3,2,1),(5,1,6),(8,2,10)])
def test_sub2numbers(a,b,c):

    res=calculator.sub2numbers(a,b)
    assert res==a-b
@pytest.mark.parametrize('a,b,c',[(3,2,1),(5,1,6),(8,2,10)])
def test_mul2numbers(a,b,c):

    res=calculator.mul2numbers(a,b)
    assert res==a*b
@pytest.mark.parametrize('a,b,c',[(3,2,1),(5,1,6),(8,2,10)])
def test_div2numbers(a,b,c):

    res=calculator.div2numbers(a,b)
    assert res==a/b