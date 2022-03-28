import calculator

def test_add2numbers():
    x=10
    y=20
    res=calculator.add2numbers(x,y)
    assert res==x+y

def test_sub2numbers():
    x=10
    y=20
    res=calculator.sub2numbers(x,y)
    assert res==x-y

def test_mul2numbers():
    x=10
    y=20
    res=calculator.mul2numbers(x,y)
    assert res==x*y

def test_div2numbers():
    x=10
    y=20
    res=calculator.div2numbers(x,y)
    assert res==x/y