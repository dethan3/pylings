import importlib.util
import sys
import os

def test_variables1():
    # Load the student's code
    file_path = os.path.abspath("exercises/01_variables/variables1.py")
    spec = importlib.util.spec_from_file_location("variables1", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    # Run the practice function
    variables = module.practice()
    
    assert "x" in variables, "Variable 'x' is missing"
    assert variables["x"] == 5, "Variable 'x' should be 5"
    
    assert "y" in variables, "Variable 'y' is missing"
    assert variables["y"] == 10, "Variable 'y' should be 10"
