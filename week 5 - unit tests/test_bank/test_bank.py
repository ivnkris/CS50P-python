from bank import value


def test_hello():
    assert value("hello") == 0


def test_starts_with_h():
    assert value("hola") == 20


def test_starts_with_something_else():
    assert value("jo napot") == 100


def test_capital():
    assert value("HELLO") == 0