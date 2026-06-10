from plates import is_valid

def test_valid():
    assert is_valid("CS50") == True
    assert is_valid("KARL18") == True
    assert is_valid("HI900") == True
    assert is_valid("HELLO") == True
    
def test_not_valid():
    assert is_valid("1234") == False
    assert is_valid("CS05") == False
    assert is_valid("HELLO?") == False
    assert is_valid("U") == False
    assert is_valid("KARLHANNOUSH") == False
    assert is_valid("") == False
    assert is_valid("NOT9Y") == False
