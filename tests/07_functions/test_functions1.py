import importlib.util
import sys
import os
import inspect

def test_functions1():
    file_path = os.path.abspath("exercises/07_functions/functions1.py")
    spec = importlib.util.spec_from_file_location("functions1", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    vars = module.practice()
    
    assert "greet" in vars, "Function 'greet' is not defined"
    assert inspect.isfunction(vars["greet"]), "'greet' should be a function"
    assert vars["greet"]() == "Hello!", "Function 'greet' should return 'Hello!'"
    assert vars.get("greeting") == "Hello!", "Variable 'greeting' should contain the result of calling 'greet'"
