import pytest
from mathers.adder import Adder

expected_op = "+"

test_l1 = 5
test_r1 = 7
expected_result1 = test_l1 + test_r1
expected_msg1 = "%s %s %s = %s" % (test_l1, expected_op, test_r1, expected_result1)

test_l2 = "abc"
test_r2 = "def"
expected_result2 = test_l2 + test_r2
expected_msg2 = "%s %s %s = %s" % (test_l2, expected_op, test_r2, expected_result2)

def test_init():
    with pytest.raises(Exception):
        x1 = Adder()
    with pytest.raises(Exception):
        x2 = Adder(test_l1)
    x3 = Adder(test_l1, test_r1)
    assert (x3.l, x3.r) == (test_l1, test_r1)
    x4 = Adder(test_l2, test_r2)
    assert (x4.l, x4.r) == (test_l2, test_r2)

def test_op_str():
    x = Adder(test_l1, test_r1)
    assert x._op_str() == expected_op

def test_result():
    x1 = Adder(test_l1, test_r1)
    assert x1.result() == expected_result1
    x1 = Adder(test_r1, test_l1)
    assert x1.result() == expected_result1
    x2 = Adder(test_l2, test_r2)
    assert x2.result() == expected_result2
    x2 = Adder(test_r2, test_l2)
    assert x2.result() != expected_result2

def test_msg():
    x1 = Adder(test_l1, test_r1)
    assert x1._msg() == expected_msg1
    x2 = Adder(test_l2, test_r2)
    assert x2._msg() == expected_msg2

def test_print(capsys):
    x1 = Adder(test_l1, test_r1)
    x1.print()
    assert capsys.readouterr().out == expected_msg1 + "\n"

