import sys

print("INTEGER")
print("0", sys.getsizeof(0))
print("1", sys.getsizeof(1))
print("1_000_000_000", sys.getsizeof(1_000_000_000))
print("10_000_000_000", sys.getsizeof(10_000_000_000))
print("sys.maxsize", sys.getsizeof(sys.maxsize))

print("\nBOOL")
print("True", sys.getsizeof(True))
print("False", sys.getsizeof(False))

print("\nSTRING")
print("a", sys.getsizeof("a"))
print("janek mowi", sys.getsizeof("janek mowi"))

print("\nFLOAT")
print("1.0", sys.getsizeof(1.0))
print("sys.float_info.max", sys.getsizeof(sys.float_info.max))
print("sys.float_info.min", sys.getsizeof(sys.float_info.min))

print("\nOTHER:")
print(isinstance(23, int))
print(isinstance(54, float))
print(isinstance(20.3, float))
print(isinstance(True, bool))
print(isinstance(True, int))
# isinstance(object, classinfo, /)
# Return True if the object argument is an instance of the classinfo argument,
# or of a (direct, indirect, or virtual) subclass thereof.
# If object is not an object of the given type, the function always returns False.
# If classinfo is a tuple of type objects (or recursively, other such tuples) or a Union Type of multiple types,
# return True if object is an instance of any of the types.
# If classinfo is not a type or tuple of types and such tuples, a TypeError exception is raised.
# TypeError may not be raised for an invalid type if an earlier check succeeds.
print(isinstance(1, "Hello", 5.6), bool)
print(isinstance(1, "Hello", 5.6), int)
