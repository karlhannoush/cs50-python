from bank import value

def test_h():
    assert value("hi") == 20
    assert value("hi there") == 20
    assert value("How are you today?") == 20
    assert value("HEY!!") == 20

def test_hello():
    assert value("hello") == 0
    assert value("hello, how are you?") == 0
    assert value("HELLO!!!") == 0

def test_else():
    assert value("Good morning") == 100
    assert value("Great to see you") == 100
    assert value("What time is it?") == 100
