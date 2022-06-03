#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   }}}1
import sys
import os
import logging
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
#   {{{2

import typing

#   mypy is a tool for <checking/enforcing> type hints:
#   install:    pip3 install mypy
#   usage:      python3 -m mypy <script>


#   Syntax (function):
def f(x: float) -> float:
    y = x ** 2
    return y


#   Forward references:
#   To use a class that is not available as a type hint, specify it as a string
class A:
    def make_B(self) -> 'B':
        return B()
class B:
    def recieve_A(self, a: 'A'):
        pass
    def recieve_B(self, b: 'B'):
        pass

#   alternatively, using NewType <(doesn't work with mypy?)>
#Blah = typing.NewType("Blah", None) 


#   List
#   Any
#   Callable
#   Mapping
#   Set
#   Dict
#   Iterable
#   NoReturn
#   Optional
#   Union
#   TypeVar
#   Generic
#   NewType
#   cast


#   LINK: https://peps.python.org/pep-0484/
#   {{{
#   }}}

a1 = A()
b1 = B()
b2 = B()

b1.recieve_A(a1)
b1.recieve_B(b2)

print(f(5))
print(f(10))

