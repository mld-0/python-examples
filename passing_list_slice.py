
#   'list(x)' and 'x[:]' both produce a shallow copy of the list
#   (use 'copy.deepcopy' to perform a deep copy)

def set_elements_i(container, new_value):
    for i in range(len(container)):
        container[i] = new_value

x = list(range(10))
print("x=(%s)" % x)

set_elements_i(x[:], 12)
print("x=(%s)" % x)

set_elements_i(list(x), 504)
print("x=(%s)" % x)

set_elements_i(x, 27)
print("x=(%s)" % x)

