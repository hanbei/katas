from katas import evilcorp


def test_censor_empty():
    assert evilcorp.censor("") == ""

def test_censor_nice_as_word():
    assert evilcorp.censor("You are a nice person") == "You are a XXXX person"

def test_censor_nice_not_as_word():
    assert evilcorp.censor("You are a niceperson") == "You are a XXXXperson"

def test_censor_nice_different_Case():
    assert evilcorp.censor("We are going to Nice") == "We are going to Nice"
