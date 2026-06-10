from twttr import no_vowels

def test_lower():
    assert no_vowels("twitter") == "twttr"
    assert no_vowels("hello") == "hll"

def test_upper():
    assert no_vowels("KARL") == "KRL"
    assert no_vowels("CS50") == "CS50"


def test_both():
    assert no_vowels("Twitter") == "Twttr"
    assert no_vowels("AmAZing") == "mZng"

