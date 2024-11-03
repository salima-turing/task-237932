import inspect


# Example class
class SomeClass:
    def __init__(self, x):
        self.x = x

    def some_method(self):
        print(f"Running method: {self.x}")


# Reflection usage
obj = SomeClass(42)
method_name = 'some_method'
method = getattr(obj, method_name)
method()  # Output: Running method: 42

# Inspecting attributes
print(inspect.getmembers(
    obj))  # Output: [('x', 42), ('__init__', <function SomeClass.__init__ at 0x7f33da94a840>), ('some_method', <function SomeClass.some_method at 0x7f33da94a950>)]
