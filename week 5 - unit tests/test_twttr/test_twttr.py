from twttr import shorten


def test_word_with_vowels():
    assert shorten("hello") == "hll"


def test_word_without_vowels():
    assert shorten("xyz") == "xyz"


def test_multiple_words():
    assert shorten("hello world") == "hll wrld"


def test_capitals():
    assert shorten("HELLO") == "HLL"


def test_numbers():
    assert shorten("no 1") == "n 1"


def test_punctuation():
    assert shorten("hello world!") == "hll wrld!"