import importlib

def dynamic_import_example():
	module_name = input("Enter the module name to import: ")
	try:
		module = importlib.import_module(module_name)
		function_name = input("Enter the function name to call: ")
		function = getattr(module, function_name)
		result = function()
		print(f"Result: {result}")
	except ImportError as e:
		print(f"Import Error: {e}")
	except AttributeError as e:
		print(f"Attribute Error: {e}")

if __name__ == "__main__":
	dynamic_import_example()
