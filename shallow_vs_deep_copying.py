#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import copy

#   LINK: https://realpython.com/copying-python-objects/
#   LINK: https://www.pythonforthelab.com/blog/deep-and-shallow-copies-of-objects/

origional_list = [ x for x in range(10) ]
origional_dict = { x:x for x in range(10) }
origional_set = { x for x in range(10) }

#   A shallow copy is only one level deep: the new object is populated with references to the same child objects
#   A deep copy is recursive: the new object is populated with copies of the child objects 

#   Python's built in mutable types like list/dict/set can be shallow copied by calling their factory functions on an existing object
new_list = list(origional_list)
new_dict = dict(origional_dict)
new_set = set(origional_set)

#   Slice notation also makes a shallow copy of a list
new_list = origional_list[:]

#   Shallow/deep copy using 'copy' library
#   These functions also work <(as one would expect)> for custom classes.
new_list = copy.copy(origional_list)
new_list = copy.deepcopy(origional_list)

#   Note that only mutable objects are deep copied. 
#   In python, two immutable objects with the same value will also have the same id.
#   The distinction between shallow/deep copy is not meaningful for immutable types.
x1 = 'x'
x2 = ['x']
print(x1 is copy.deepcopy(x1))        #   True
print(x2 is copy.deepcopy(x2))        #   False


#   Customize shallow copy behaviour for a custom class with a '__copy__(self)' method.
#   This must return a new shallow copy of the current object.
#   In this example we use the '__dict__' attribute as shorthand for the object's data.
class Point1:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.other = [1, 2, 3]
    def __copy__(self):
        new_instance = Point1(self.x, self.y)
        new_instance.__dict__.update(self.__dict__)
        new_instance.other = copy.deepcopy(self.other)
        return new_instance

#   Customize deep copy for a custom class with a '__deepcopy__(self, memodict={})' method.
#   'memodict' stores objects that have already been copied, preventing infinite recursion.
class Point2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.other = [1, 2, 3]
    def __deepcopy__(self, memodict={}):
        new_instance = Point2(self.x, self.y)
        new_instance.__dict__.update(self.__dict__)
        new_instance.x = copy.deepcopy(self.x, memodict)
        new_instance.y = copy.deepcopy(self.y, memodict)
        return new_instance

