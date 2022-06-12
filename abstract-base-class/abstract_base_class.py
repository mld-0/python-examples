#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import abc

#   As taken from: clean-code/03-functions

class EmployeeRecord:
#   {{{
    def __init__(self):
        self.kind = None
#   }}}
class Employee(abc.ABC):
#   {{{
    @abc.abstractmethod
    def isPayday(self):
        raise NotImplementedError()
    @abc.abstractmethod
    def calculatePay(selfj):
        raise NotImplementedError()
    @abc.abstractmethod
    def delieverPay(self, pay: 'Money'):
        raise NotImplementedError()
#   }}}
class FullTimeEmployee(Employee):
#   {{{
    def isPayday(self):
        return False
    def calculatePay(self):
        return 53
    def delieverPay(self, pay: 'Money'):
        pass
#   }}}
class PartTimeEmployee(Employee):
#   {{{
    def isPayday(self):
        return False
    def calculatePay(self):
        return 27 
    def delieverPay(self, pay: 'Money'):
        pass
#   }}}
class HourlyEmployee(Employee):
#   {{{
    def isPayday(self):
        return False
    def calculatePay(self):
        return 12 
    def delieverPay(self, pay: 'Money'):
        pass
#   }}}
def EmployeeFactory(r: 'EmployeeRecord'):
    if r.kind is FullTimeEmployee:
        return FullTimeEmployee(r)
    elif r.kind is PartTimeEmployee:
        return PartTimeEmployee(r)
    elif r.kind is HourlyEmployee:
        return HourlyEmployee(r)
    else:
        raise Exception("Invalid employee kind=(%s)" % str(r.kind))

