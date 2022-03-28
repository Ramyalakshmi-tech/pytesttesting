import num

def test_div5():
    x=10
    res=num.div5(x)
    assert res=="Divisible by 5"

def test_div9():
    x=18
    res=num.div9(x)
    assert res=="Divisible by 9"

def test_div10():
    x=40
    res=num.div10(x)
    assert res=="Divisible by 10"

def test_div7():
    x=49
    res=num.div7(x)
    assert res=="Divisible by 7"

