#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
#   Ongoings:
#   {{{
#   Ongoing: 2022-06-23T23:57:13AEST how __main__.py should handle imports from within package (runnable with/without installing?) (also needed for tests) [...]
#   Ongoing: 2022-06-24T00:09:24AEST should package be runnable without 'installing' (either adding to python-path, or using 'pip install') anyway? (recall: don't try and <trick/hack> 'import')
#   Ongoing: 2022-06-24T00:11:32AEST does lack of '__main__.py' denote a python package 'not executable' (can we not set a run-package command in some config file?)
#   }}}
from sandpit_package.mathers.adder import Adder
from sandpit_package.mathers.multiplier import Multiplier

from sandpit_package.animals.animal import Animal
from sandpit_package.animals.cat import Cat
from sandpit_package.animals.bird import Bird
from sandpit_package.animals.dog import Dog

#   File executed when we run our package directly:
#       python3 -m sandpit_package

#   Allows package to also be 'run' with:
#       sandpit_package.main()
def main():

    birb = Bird("Wal")
    birb.speak()
    birb.walk()

    cat = Cat("Larry")
    cat.speak()
    cat.walk()

    dog = Dog("Patch")
    dog.speak()
    dog.walk()
    print()

    a = Adder(3,4)
    a.print()

    b = Multiplier(56,9)
    b.print()
    print()

    return 0


if __name__ == '__main__':
    main()

