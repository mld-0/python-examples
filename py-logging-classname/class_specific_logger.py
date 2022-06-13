import sys
import logging
import inspect
#   %(name)s becomes logger name, which is the class of the caller.
#LOGGING_FORMAT = logging.BASIC_FORMAT
LOGGING_FORMAT = "%(levelname)-8s %(name)s.%(funcName)s: %(message)s"
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG, format=LOGGING_FORMAT)
#logging.basicConfig(level=logging.DEBUG)

#   TODO: 2022-05-21T09:19:25AEST py-logging-classname/wrapping_logging, how to set stream/level/format settings per-logger (per thing returned by 'logging.getLogger(str)')

def log():
    try:
        stack = inspect.stack()
        #   Continue: 2022-05-21T09:01:23AEST include the caller function argument <names/types?> (whatever you can get?) 
        logger_classname = stack[1][0].f_locals["self"].__class__.__name__
        #   Continue: 2022-05-21T08:59:45AEST how to apply stream/level/format settings specific to each logger: use 'logging.BASIC_FORMAT' for non-class calls to log -> or just use 'logging.' instead of 'log().' outside classes(?)
        return logging.getLogger(logger_classname)
    except KeyError as ex:
        return logging.getLogger()

class Widget:
    def fab(self):
        log().debug("abcdef")
    def foo(self):
        log().warning("hijk")
    def bar(self):
        log().error("lmnop")
    def baz(self):
        log().info("qrstuv")

def make_calls_Widget(w: Widget):
    w.fab()
    w.foo()
    w.bar()
    w.baz()

def schenanigans():
    log().debug("123?")
    logging.debug("456?")

if __name__ == '__main__':
    w = Widget()
    make_calls_Widget(w)
    schenanigans()
    log().error("abc")

