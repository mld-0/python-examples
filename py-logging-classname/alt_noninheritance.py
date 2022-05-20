import logging


def log(className):
    return logging.getLogger(className)


class testclassa:
    def testmethod1(self):
        log(self.__class__.__name__).error("error from test class A")


class testclassb:
    def testmethod2(self):
        log(self.__class__.__name__).error("error from test class B")


testclassa().testmethod1()
testclassb().testmethod2()

