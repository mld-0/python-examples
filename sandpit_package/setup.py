#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
#   {{{
#   Ongoing: 2022-06-26T02:07:22AEST Use of a 'src/' directory?
#   Ongoing: 2022-06-26T02:11:37AEST 'tests_require' is deprecated?
#   Ongoing: 2022-06-26T02:19:45AEST to have 'mathers' / 'animals' / ect. not be available for top-level import (do we need to) place them in 'sandpit_package/sandpit_package/*'?
#   Ongoing: 2022-06-26T02:22:01AEST 'entry_points' vs '__main__.py'
#   }}}

from setuptools import setup, find_packages

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
    name = "sandpit_package",
    version = "0.0",
    description = "An example of (how to setup) a python package",
    long_description = long_description,
    author_email = "mld.0@protonmail.com",
    #packages = [ 'sandpit_package' ],
    packages = find_packages(include=['sandpit_package', 'sandpit_package.*']),
    install_requires = [],
    tests_require = [ 'pytest' ],
    #   data files?
    #   <>
)

