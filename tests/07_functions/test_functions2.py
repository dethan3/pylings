import importlib.util
import sys
import os
import inspect

def test_functions2():
    file_path = os.path.abspath("exercises/07_functions/functions2.py")
    spec = importlib.util.spec_from_file_location("functions2", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    vars = module.practice()
    
    assert "add" in vars, "Function 'add' is not defined"
    assert inspect.isfunction(vars["add"]), "'add' should be a function"
    assert vars["add"](10, 20) == 30, "Function 'add(10, 20)' should return 30"
    assert vars.get("result") == 8, "Variable 'result' should be 8 (5 + 3)"
