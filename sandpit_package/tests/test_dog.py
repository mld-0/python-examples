import pytest
from sandpit_package.animals.dog import Dog

test_name = "patch"
test_type = Dog
expected_sound = "ruf"
expected_walk = "*this is the most fun ever*\n"

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

