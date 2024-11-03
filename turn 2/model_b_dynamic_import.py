# main.py
model_name = 'os'
module = __import__(model_name)
simulator = getattr(module, 'getcwd')()
simulator()
