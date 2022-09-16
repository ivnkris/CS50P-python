from plates import is_valid


def test_aphabetical():
    assert is_valid("HELLO") == True
    assert is_valid("H3LLO") == False
    assert is_valid("50") == False


def test_length():
    assert is_valid("TOOLONG") == False


def test_number_placement():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False


def test_zero():
    assert is_valid("AAA202") == True
    assert is_valid("AAA022") == False


def test_not_alphanumeric():
    assert is_valid("HE.LLO") == False