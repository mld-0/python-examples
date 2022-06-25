import pytest
from animals.bird import Bird

test_name = "wal"
test_type = Bird
expected_sound = "chirp"
expected_walk = "*swoop*\n"

def test_init():
    with pytest.raises(Exception):
        a1 = test_type()
    a2 = test_type(test_name)
    assert a2.name == test_name

def test_sound():
    a = test_type(test_name)
    assert a._sound() == expected_sound

def test_walk(capsys):
    a = test_type(test_name)
    a.walk()
    assert capsys.readouterr().out == expected_walk

def test_speak(capsys):
    a = test_type(test_name)
    a.speak()
    assert capsys.readouterr().out == "%s, I am %s\n" % (expected_sound, test_name)

