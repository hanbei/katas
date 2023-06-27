from katas import evilcorp


def test_censor_empty():
    assert evilcorp.censor("") == ""


def test_censor_nice_as_word():
    assert evilcorp.censor("You are a nice person") == "You are a XXXX person"


def test_censor_nice_not_as_word():
    assert evilcorp.censor("You are a niceperson") == "You are a XXXXXXXXXX"


def test_censor_nice_different_Case():
    assert evilcorp.censor("We are going to Nice") == "We are going to Nice"


def test_censor_multiple_words():
    assert evilcorp.censor_multiple_words("Such a nice day with a bright sun, makes me happy",
                                          ["nice", "pony", "sun", "light", "fun", "happy", "funny",
                                           "joy"]) == "Such a XXXX day with a bright XXX, makes me XXXXX"


def test_censor_multiple_words_empty_list():
    assert evilcorp.censor_multiple_words("Such a nice day with a bright sun, makes me happy",
                                          []) == "Such a nice day with a bright sun, makes me happy"


def test_censor_multiple_words_none_list():
    assert evilcorp.censor_multiple_words("Such a nice day with a bright sun, makes me happy",
                                          None) == "Such a nice day with a bright sun, makes me happy"
