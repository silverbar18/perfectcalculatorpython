import perfectcalculatorpython

def test_Impertaive_Negative():
    assert perfectcalculatorpython.isPerfectNumber_Imperative(-1) == False
    assert perfectcalculatorpython.isPerfectNumber_Imperative(-6) == False

def test_Impertaive_Positive_NotPerfect():
    assert perfectcalculatorpython.isPerfectNumber_Imperative(0) == False
    assert perfectcalculatorpython.isPerfectNumber_Imperative(1) == False
    assert perfectcalculatorpython.isPerfectNumber_Imperative(10) == False

def test_Impertaive_Positive_Perfect():
    assert perfectcalculatorpython.isPerfectNumber_Imperative(6) == True
    assert perfectcalculatorpython.isPerfectNumber_Imperative(28) == True

def test_Functional_Negative():
    assert perfectcalculatorpython.isPerfectNumber_Functional(-1) == False
    assert perfectcalculatorpython.isPerfectNumber_Functional(-6) == False

def test_Functional_Positive_NotPerfect():
    assert perfectcalculatorpython.isPerfectNumber_Functional(0) == False
    assert perfectcalculatorpython.isPerfectNumber_Functional(1) == False
    assert perfectcalculatorpython.isPerfectNumber_Functional(10) == False

def test_Functional_Positive_Perfect():
    assert perfectcalculatorpython.isPerfectNumber_Functional(6) == True
    assert perfectcalculatorpython.isPerfectNumber_Functional(28) == True
