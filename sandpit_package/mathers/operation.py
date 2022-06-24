from abc import ABC, abstractmethod

class Operation(ABC):

    def __init__(self, l, r):
        self.l = l
        self.r = r

    def print(self):
        print(self._msg())

    def _msg(self):
        return "%s %s %s = %s" % (self.l, self._op_str(), self.r, self.result())

    @abstractmethod
    def _op_str(self):
        ...

    @abstractmethod
    def result(self):
        ...

