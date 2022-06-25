import pytest
import os
from sandpit_package.resource_reader import ResourceReader

#   Ongoing: 2022-06-26T03:09:20AEST something 'better' (produces a better error (for starters)) (pytest specific?) than 'assert'?

def test_read_lines():
    expected = get_lines()
    result = ResourceReader.read_lines()
    assert result == expected

def get_lines():
    return '\n'.join( ['line one', 'line two', 'line 3', 'line four', '' ] )

def test_read_allbytes():
    expected = get_allbytes()
    result = ResourceReader.read_allbytes()
    assert result == expected

def get_allbytes():
    return bytes( [ x for x in range(256) ] )

def test_open_lines():
    with ResourceReader.open_lines() as f:
        assert f.readable() and not f.writable()
        assert isinstance(f.read(0), str)
        assert os.path.isfile(f.name)

def test_open_allbytes():
    with ResourceReader.open_allbytes() as f:
        assert f.readable() and not f.writable()
        assert f.mode == 'rb'
        assert isinstance(f.read(0), bytes)
        assert os.path.isfile(f.name)

