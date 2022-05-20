import logging


# Create a base class
class LoggingHandler:
    def __init__(self, *args, **kwargs):
        self.log = logging.getLogger(self.__class__.__name__)


# Create test class A that inherits the base class
class testclassa(LoggingHandler):
    def testmethod1(self):
        # call self.log.<log level> instead of logging.log.<log level>
        self.log.error("error from test class A")


# Create test class B that inherits the base class
class testclassb(LoggingHandler):
    def testmethod2(self):
        # call self.log.<log level> instead of logging.log.<log level>
        self.log.error("error from test class B")


testclassa().testmethod1()
testclassb().testmethod2()

