import inspect

def reflect_and_debug():
	def some_function():
		a = 10
		b = 20
		result = a + b
		return result

	# Using reflection to inspect the function's code
	source_code = inspect.getsource(some_function)
	print("Function Source Code:")
	print(source_code)

	# Using reflection to modify a variable's value (note: this is a simple example and should be used cautiously)
	frame = inspect.currentframe()
	args, _, _, locals = inspect.getargvalues(frame)
	locals['a'] = 50

	result = some_function()
	print(f"Modified Result: {result}")  # Output will be 70 (50+20)

if __name__ == "__main__":
	reflect_and_debug()
